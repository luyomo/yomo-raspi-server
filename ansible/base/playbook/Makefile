docker_test:
	ansible-playbook deploy.yml -i inventories/hosts.yml --diff --check --tags docker

docker:
	ansible-playbook deploy.yml -i inventories/hosts.yml --tags docker

general_test:
	ansible-playbook deploy.yml -i inventories/hosts.yml --diff --check --tags general

general:
	ansible-playbook deploy.yml -i inventories/hosts.yml --tags general
