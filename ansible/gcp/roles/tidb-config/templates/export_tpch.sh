#!/bin/bash
TABLES="customer lineitem nation orders part partsupp region supplier"

DBNAME=tpch
mkdir /DATA/csvdata/${DBNAME}
gsutil mkdir /DATA/csvdata/tpch
for table in $TABLES
do
  echo "----- ----- ----- Table name: $table"
  dumpling -u root -P 4000 -h {{ componentIPs['externalIP']  }} --filetype csv -o /DATA/csvdata/${DBNAME} -t 8 -B ${DBNAME} -T ${DBNAME}.$table
  gsutil -m mv /DATA/csvdata/tpch/${DBNAME}.${table}.000000000.csv gs://tidbjaytest/tidbtest/${DBNAME}
  gsutil -m mv /DATA/csvdata/tpch/${DBNAME}.${table}-schema.sql gs://tidbjaytest/tidbtest/${DBNAME}
done
