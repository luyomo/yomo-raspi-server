vpc:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "vpc"

zones:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "zones"

subnets:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "subnets"

gateway:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "gateway"

route_table:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "route_table"

security_group:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "security_group"

sshkeys:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "sshkeys"

workstation:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "workstation,basic"

pd:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "pd,basic"

kv:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "kv,basic"
