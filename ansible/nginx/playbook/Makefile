INTERPRETER=-e 'ansible_python_interpreter=/usr/bin/python3'

nginx:
	ansible-playbook deploy.yml -i inventories/hosts.yml $(INTERPRETER) --diff --tags nginx
