INTERPRETER=-e 'ansible_python_interpreter=/usr/bin/python3'

zsh_test:
	ansible-playbook deploy.yml -i inventories/hosts.yml $(INTERPRETER) --diff --check --tags zsh

zsh:
	ansible-playbook deploy.yml -i inventories/hosts.yml $(INTERPRETER) --tags zsh

tmux_test:
	ansible-playbook deploy.yml -i inventories/hosts.yml $(INTERPRETER) --diff --check --tags tmux

tmux:
	ansible-playbook deploy.yml -i inventories/hosts.yml $(INTERPRETER) --tags tmux

cht_test:
	ansible-playbook deploy.yml -i inventories/hosts.yml $(INTERPRETER) --diff --check --tags cht

cht:
	ansible-playbook deploy.yml -i inventories/hosts.yml $(INTERPRETER) --tags cht
