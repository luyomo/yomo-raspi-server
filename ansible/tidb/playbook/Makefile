tiup:
	ansible-playbook deploy.yml -i inventories/hosts.yml --vault-password-file .passwd --tags bin
	#ansible-playbook deploy.yml -i inventories/hosts.yml -e 'ansible_python_interpreter=/usr/bin/python3' --vault-password-file .passwd --tags bin

init_test:
	ansible-playbook deploy.yml -i inventories/hosts.yml -e 'ansible_python_interpreter=/usr/bin/python3' --vault-password-file .passwd --diff --check --tags env

init:
	ansible-playbook deploy.yml -i inventories/hosts.yml -e 'ansible_python_interpreter=/usr/bin/python3'  --vault-password-file .passwd --tags env

local:
	ansible-playbook deploy.yml -i inventories/hosts.yml -e 'ansible_python_interpreter=/usr/bin/python3' --tags local

deploy:
	ansible-playbook deploy.yml -i inventories/hosts.yml -e 'ansible_python_interpreter=/usr/bin/python3' --vault-password-file .passwd --tags deploy

##Simple##########################################
minimal_simple_test:
	echo "tidb minimal simple test"
#	ansible-playbook deploy.yml -i inventories/hosts.yml -e 'ansible_python_interpreter=/usr/bin/python3' --diff --check --tags cassandra

minimal_simple:
	echo "tidb minimal simple"

minimal_complex_test:
	echo "tidb minimal complex test"

minimal_complex:
	echo "tidb mininal complex"

##tiflash##########################################
tiflash_simple_test:
	echo "tidb tiflash simple test"

tiflash_simple:
	echo "tidb tiflash simple"

tiflash_complex_test:
	echo "tidb tiflash complex test"

tiflash_complex:
	echo "tidb tiflash complex"

##ticdc##########################################
ticdc_simple_test:
	echo "tidb ticdc simple test"

ticdc_simple:
	echo "tidb ticdc simple"

ticdc_complex_test:
	echo "tidb ticdc complex test"

ticdc_complex:
	echo "tidb ticdc complex"

##binlog##########################################
binlog_simple_mysql_test:
	echo "tidb binlog simple mysql test"

binlog_simple_mysql:
	echo "tidb binlog simple mysql"

binlog_simple_file_test:
	echo "tidb binlog simple file test"

binlog_simple_file:
	echo "tidb binlog simple file"

binlog_complex_test:
	echo "tidb binlog complex test"

binlog_complex:
	echo "tidb binlog complex"

##tispark##########################################
tispark_simple_test:
	echo "tidb tispark simple test"

tispark_simple:
	echo "tidb tispark simple"

tispark_complex_test:
	echo "tidb tispark complex test"

tispark_complex:
	echo "tidb tispark complex"


##hybird##########################################
hybird_simple_test:
	echo "tidb hybird simple test"

hybird_simple:
	echo "tidb hybird simple"

hybird_complex_test:
	echo "tidb hybird complex test"

hybird_complex:
	echo "tidb hybird complex"

##hybird##########################################
geo:
	echo "tidb geo simple test"

geo_simple:
	echo "tidb geo simple"
