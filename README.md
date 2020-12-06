[![CI (debian)](https://github.com/marvel-nccr/ansible-role-aiida/workflows/CI%20(debian)/badge.svg)](https://github.com/marvel-nccr/ansible-role-aiida/actions)
[![CI (redhat)](https://github.com/marvel-nccr/ansible-role-aiida/workflows/CI%20(redhat)/badge.svg)](https://github.com/marvel-nccr/ansible-role-aiida/actions)
[![Ansible Role](https://img.shields.io/ansible/role/25553.svg)](https://galaxy.ansible.com/marvel-nccr/aiida)
[![Release](https://img.shields.io/github/tag/marvel-nccr/ansible-role-aiida.svg)](https://github.com/marvel-nccr/ansible-role-aiida/releases)

# Ansible Role: marvel-nccr.aiida

An ansible role that installs and configures [AiiDA](http://www.aiida.net/) on Ubuntu, RHEL, CentOS and Fedora.

The role:

- Installs and starts the PostgreSQL and RabbitMQ services
- Installs a designated Python version
- Creates an 'aiida' Python virtual environment and installs aiida-core and plugins into it
- Creates a 'jupyter' Python virtual environment and installs Jupyter and Jupyter Lab into it, then links the virtual environment as a kernel.
- Adds [virtualenwrapper](https://virtualenvwrapper.readthedocs.io) for managing the virtual environments.
- Creates an AiiDA profile and starts the daemon
- Starts the AiiDA REST API
- Sets up localhost codes for the AiiDA plugins (where code paths are defined)
- Sets up pseudopotential families in the AiiDA profile

## Installation

`ansible-galaxy install marvel-nccr.aiida`

## Role Variables

See `defaults/main.yml`

## Example Playbook

```yaml
- hosts: servers
  roles:
  - role: marvel-nccr.aiida
```

For full use of JupyterLab, install nodejs, e.g. using [geerlingguy.nodejs](https://galaxy.ansible.com/geerlingguy/nodejs):

```yaml
- hosts: servers
  tasks:
  - include_role:
      name: geerlingguy.nodejs
    vars:
      nodejs_version: 12.x
      nodejs_install_npm_user: root
  - include_role:
      name: marvel-nccr.aiida
```

## Usage

Once run, the user can "activate" the aiida environment in the terminal using:

```console
$ workon aiida
(aiida) $ verdi status
verdi status
 ✔ config dir:  /root/.aiida
 ✔ profile:     On profile name-with-dashes
 ✔ repository:  /root/.aiida/repository/name-with-dashes
 ✔ postgres:    Connected as aiida@localhost:5432
 ✔ rabbitmq:    Connected as amqp://guest:guest@127.0.0.1:5672?heartbeat=600
 ✔ daemon:      Daemon is running as PID 9484 since 2020-11-30 21:51:30
```

To start a jupyter lab server:

```console
$ aiida-jupyterlab
...
    To access the notebook, open this file in a browser:
        file:///root/.local/share/jupyter/runtime/nbserver-14617-open.html
    Or copy and paste one of these URLs:
        http://localhost:8890/?token=a7086764cda7aba8488a767386d57121429958771a8bccb2
     or http://127.0.0.1:8890/?token=a7086764cda7aba8488a767386d57121429958771a8bccb2
```

## Development and testing

This role uses [Molecule](https://molecule.readthedocs.io/en/latest/#) and [Docker](https://www.docker.com/) for tests.

After installing [Docker](https://www.docker.com/):

Clone the repository into a package named `marvel-nccr.aiida` (the folder must be named the same as the Ansible Galaxy name)

```bash
git clone https://github.com/marvel-nccr/ansible-role-aiida marvel-nccr.aiida
cd marvel-nccr.aiida
```

Then run:

```bash
pip install -r requirements.txt  # Installs molecule
molecule test  # runs tests
```

or use tox (see `tox.ini`):

```bash
pip install tox
tox
```

To manually test the created docker container, first run:

```bash
tox converge
```

This will run the ansible role, leaving the container running.
The recommended way to interact with the container is then to use the [VS Code Docker extension](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker).
Using this you can then attach a visual studio code instance:

![VS Code Docker extension](./vscode.png)

Inside the container run `aiida-jupyterlab`, and you will be able to access the supplied URL from your local browser.

When you are finished with the container, destroy the container with:

```bash
tox destroy
```

## Code style

Code style is formatted and linted with [pre-commit](https://pre-commit.com/).

```bash
pip install pre-commit
pre-commit run -all
```

## Deployment

Deployment to Ansible Galaxy is automated *via* GitHub Actions.
Simply tag a release `vX.Y.Z` to initiate the CI and release workflow.
Note, the release will only complete if the CI tests pass.

## License

MIT

## Contact

Please direct inquiries regarding Quantum Mobile and associated ansible roles to the [AiiDA mailinglist](http://www.aiida.net/mailing-list/).
