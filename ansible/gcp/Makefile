servers: zones subnets gateway workstation pd kv tidb dm

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

ycsb:
	ansible-playbook -i inventories/hosts.yml ycsb.yml

tiup:
	ansible-playbook -i inventories/hosts.yml tiup.yml --vault-password-file .passwd

wordpress:
	ansible-playbook -i inventories/hosts.yml wordpress.yml

start-dm:
	ansible-playbook -i inventories/hosts.yml start-dm.yml

add-kv:
	ansible-playbook -i inventories/hosts.yml servers.yml --tags "add-kv,basic"
