#!/bin/sh

TABLES="icingaweb_group icingaweb_group_membership icingaweb_user icingaweb_user_preference"
for name in $TABLES
do
  mysql -h {{ MYSQL_HOST }} -P {{ MYSQL_PORT }} -u icingaweb2 -picingaweb2 icingaweb2 -e "delete from ${name}"
  mysql -h {{ MYSQL_HOST }} -P {{ MYSQL_PORT }} -u icingaweb2 -picingaweb2 icingaweb2 -e "LOAD DATA LOCAL INFILE '/tmp/icingaweb2/data/${name}.csv' INTO TABLE ${name} FIELDS TERMINATED BY x'2c' ENCLOSED BY b'100010' LINES TERMINATED BY '\r\n' IGNORE 1 LINES"
done
