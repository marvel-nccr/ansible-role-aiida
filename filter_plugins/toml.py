# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

try:
    import tomli
    HAS_TOMLI = True
except ImportError:
    HAS_TOMLI = False

from ansible.errors import AnsibleFilterError
from ansible.module_utils._text import to_text
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.module_utils.six import string_types


def from_toml(o):
    if not HAS_TOMLI:
        raise AnsibleFilterError("The 'from_toml' filter plugin requires the python 'tomli' library'")
    if not isinstance(o, string_types):
        raise AnsibleFilterError('from_toml requires a string, got %s' % type(o))
    return tomli.loads(to_text(o, errors='surrogate_or_strict'))


class FilterModule(object):
    def filters(self):
        return {
            'from_toml': from_toml
        }
