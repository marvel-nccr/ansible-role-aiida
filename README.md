[![CI](https://github.com/marvel-nccr/ansible-role-aiida/workflows/CI/badge.svg)](https://github.com/marvel-nccr/ansible-role-aiida/actions)
[![Ansible Role](https://img.shields.io/ansible/role/25553.svg)](https://galaxy.ansible.com/marvel-nccr/aiida)
[![Release](https://img.shields.io/github/tag/marvel-nccr/ansible-role-aiida.svg)](https://github.com/marvel-nccr/ansible-role-aiida/releases)

# Ansible Role: marvel-nccr.aiida

An ansible role that installs and configures [AiiDA](http://www.aiida.net/) on Ubuntu, RHEL, CentOS and Fedora.

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

or use tox (see `tox.ini`).

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
