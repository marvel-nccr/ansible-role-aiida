import os
import re
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

all_vars = host.ansible.get_variables()
venv = all_vars['aiida_venv']
# "{{ aiida_computer_run_folder |  regex_replace('\\$\\{HOME}', current_user_home) }}"

def test_upf_families(host):
  pps = all_vars['aiida_pseudopotentials']

  installed_pps = host.run(venv + "/bin/verdi data upf listfamilies")
  for pp in pps:
      assert pp.name in installed_pps.stdout


