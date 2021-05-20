cassandra_test:
	ansible-playbook deploy.yml -i inventories/hosts.yml -e 'ansible_python_interpreter=/usr/bin/python3' --diff --check --tags cassandra

cassandra:
	ansible-playbook deploy.yml -i inventories/hosts.yml -e 'ansible_python_interpreter=/usr/bin/python3' --tags cassandra
