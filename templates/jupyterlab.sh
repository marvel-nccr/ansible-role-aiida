#!/bin/bash
source "{{ aiida_jupyter_venv }}/bin/activate"

if jupyter notebook list | grep localhost:${1:-{{ aiida_jupyter_port }}}; then
    url=`jupyter notebook list | grep -m1 localhost:${1:-{{ aiida_jupyter_port }}} | awk '{print $1}'`
    echo "already open at: $url"
    xdg-open $url
else
    jupyter lab --MultiKernelManager.default_kernel_name='{{ aiida_kernel_name }}' \
    {% if jupyter_ip is defined %}
    --ip="{{ jupyter_ip }}" \
    {% endif %}
    --port=${1:-{{ aiida_jupyter_port }}} {{ aiida_jupyter_extra_args | default('') }}
fi
