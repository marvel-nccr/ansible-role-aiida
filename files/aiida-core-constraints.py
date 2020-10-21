#!/usr/bin/env python
"""Script to convert aiida setup.json to pip constraints file.

Usage::

    python aiida-core-constraints.py path/to/setup.json extras1 extras2 ...
"""
import json
from pathlib import Path
import sys

def remove_extra(req):
    """Extras are not allowed in constraints files, e.g. dep[extra]>0.1 -> dep>0.1 """
    if "[" not in req or "]" not in req):
        return req
    return req.split("[")[0] + req.split("]")[-1]


def main(path, *extras):
    path = Path(path)
    data = json.loads(path.read_text("utf8"))

    output = ["# aiida-core requirements: v" + data["version"]]
    # we can't add this when using the file as a constraint file for actually installing aiida-core
    # output.append("aiida-core==" + data["version"])
    output.extend([remove_extra(req) for req in data["install_requires"]])

    for extra in extras:
        output.append("# " + extra)
        output.extend([remove_extra(req) for req in data["extras_require"][extra]])

    print("\n".join(output))

if __name__ == "__main__":
    assert len(sys.argv) > 1, "JSON path required"
    main(sys.argv[1], *sys.argv[2:])
