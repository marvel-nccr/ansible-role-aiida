#!/bin/bash
source "{{ aiida_jupyter_venv }}/bin/activate"

jupyter lab --MultiKernelManager.default_kernel_name='aiida'
