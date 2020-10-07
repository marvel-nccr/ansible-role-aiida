[![Build Status](https://travis-ci.org/marvel-nccr/ansible-role-aiida.svg?branch=master)](https://travis-ci.org/marvel-nccr/ansible-role-aiida)
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

```
git clone https://github.com/marvel-nccr/ansible-role-aiida marvel-nccr.aiida
# Note: folder name marvel-nccr.aiida is required for running tests
cd marvel-nccr.aiida
pip install -r requirements.txt  # Installs molecule
molecule test  # runs tests
```

## License

MIT

## Contact

Please direct inquiries regarding Quantum Mobile and associated ansible roles to the [AiiDA mailinglist](http://www.aiida.net/mailing-list/).
