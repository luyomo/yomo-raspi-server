servers:
	ansible-playbook -i inventories/hosts.yml servers.yml

zones:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "zones"

subnets:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "subnets"

gateway:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "gateway"

workstation:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "workstation,basic"

pd:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "pd,basic"

kv:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "kv,basic"

tidb:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "tidb,basic"

dm:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "dm,basic"

tidb-config:
	ansible-playbook -i inventories/hosts.yml tidb-config.yml

tiup:
	ansible-playbook -i inventories/hosts.yml tiup.yml --vault-password-file .passwd

wordpress:
	ansible-playbook -i inventories/hosts.yml wordpress.yml

start-dm:
	ansible-playbook -i inventories/hosts.yml start-dm.yml

add-kv:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "add-kv,basic"

backup:
	ansible-playbook -i inventories/hosts.yml -e 'ansible_python_interpreter=/usr/bin/python3' backup.yml
