#!/bin/bash

DBHOST="{{ componentIPs['tidb'] | first }}"

mysql -h $DBHOST -u root -P 4000 tpch -e "alter table customer set tiflash replica 2"
mysql -h $DBHOST -u root -P 4000 tpch -e "alter table lineitem set tiflash replica 2"
mysql -h $DBHOST -u root -P 4000 tpch -e "alter table nation   set tiflash replica 2"
mysql -h $DBHOST -u root -P 4000 tpch -e "alter table orders   set tiflash replica 2"
mysql -h $DBHOST -u root -P 4000 tpch -e "alter table part     set tiflash replica 2"
mysql -h $DBHOST -u root -P 4000 tpch -e "alter table partsupp set tiflash replica 2"
mysql -h $DBHOST -u root -P 4000 tpch -e "alter table region   set tiflash replica 2"
mysql -h $DBHOST -u root -P 4000 tpch -e "alter table supplier set tiflash replica 2"
