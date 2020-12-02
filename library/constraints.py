#!/usr/bin/python
# -*- coding: utf-8 -*-

DOCUMENTATION = """
---
module: constraints
short_description: Create a pip constraints file
author: 
  - @chrisjsewell
options:
  src:
    description: Path to requirements file
    required: true
  dest:
    description: Path to write constraints file
    required: true

"""

EXAMPLES = """
- name: Create constraints
  constraints:
    src: /path/to/requirements.txt
    dest: /path/to/constraints.txt

"""

# RETURN = """
# output:
#     description: ...
#     returned: `changed == True`
#     type: dict
# """

import os
from pathlib import Path
from ansible.module_utils.basic import AnsibleModule


def _main():
    """Entrypoint."""
    module = AnsibleModule(
        argument_spec={
            "src": {"required": True, "type": "str"},
            "dest": {"required": True, "type": "str"},
        },
        supports_check_mode=True,
    )
    src = Path(os.path.expandvars(os.path.expanduser(module.params["src"])))
    dest = Path(os.path.expandvars(os.path.expanduser(module.params["dest"])))

    if not src.exists():
        module.fail_json(msg="src does not exist")
        return

    # get hash of current dest
    hashed = module.sha256(str(dest)) if dest.exists() else None

    # read requirements file
    lines = [
        line.strip()
        for line in src.read_text("utf8").splitlines()
        if (line.strip() and not line.strip().startswith("#"))
    ]

    # remove extras which are not allowed in constraints files, e.g. dep[extra]>0.1 -> dep>0.1
    constraints = []
    for line in lines:
        if "[" not in line or "]" not in line:
            constraints.append(line)
            continue
        start, end = line.split("[", 1)
        constraints.append(start + end.split("]", 1)[1])

    # write constraints file
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(constraints))

    # check if changed
    changed = module.sha256(str(dest)) != hashed if hashed else True

    module.exit_json(changed=changed)


if __name__ == "__main__":
    _main()
