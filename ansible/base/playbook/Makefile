INTERPRETER=-e 'ansible_python_interpreter=/usr/bin/python3'

docker_test:
	ansible-playbook deploy.yml -i inventories/hosts.yml $(INTERPRETER) --diff --check --tags docker

docker:
	ansible-playbook deploy.yml -i inventories/hosts.yml $(INTERPRETER) --tags docker

general_test:
	ansible-playbook deploy.yml -i inventories/hosts.yml $(INTERPRETER) --diff --check --tags general

general:
	ansible-playbook deploy.yml -i inventories/hosts.yml $(INTERPRETER) --tags general

golang_test:
	ansible-playbook deploy.yml -i inventories/hosts.yml $(INTERPRETER) --diff --check --tags golang

golang:
	ansible-playbook deploy.yml -i inventories/hosts.yml $(INTERPRETER) --tags golang
