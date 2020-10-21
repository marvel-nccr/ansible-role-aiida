#!/usr/bin/env python
"""Script to convert aiida setup.json to pip constraints file.

Usage::

    python aiida-core-constraints.py path/to/setup.json extras1 extras2 ...
"""
import json
from pathlib import Path
import sys

def main(path, *extras):
    path = Path(path)
    data = json.loads(path.read_text("utf8"))

    output = ["# aiida-core requirements"]
    # output.append("aiida-core==" + data["version"])
    # extras are not allowed in constraints files, e.g. dep[extra] -> dep
    output.extend([req.split("[")[0] for req in data["install_requires"]])

    for extra in extras:
        output.append("# " + extra)
        output.extend([req.split("[")[0] for req in data["extras_require"][extra]])

    print("\n".join(output))

if __name__ == "__main__":
    assert len(sys.argv) > 1, "JSON path required"
    main(sys.argv[1], *sys.argv[2:])
