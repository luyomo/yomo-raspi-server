#!/bin/bash

#data_folder_path="gs://tpch_benchmark/100/"
data_folder_path="/tmp/csv/"
dataset=mixi

tables="part supplier partsupp customer orders lineitem nation region"
part_schema=p_partkey:INTEGER,p_name:STRING,p_mfgr:STRING,p_brand:STRING,p_type:STRING,p_size:INTEGER,p_container:STRING,p_retailprice:FLOAT,p_comment:STRING
supplier_schema=s_suppkey:INTEGER,s_name:STRING,s_address:STRING,s_notionkey:INTEGER,s_phone:STRING,s_acctbal:FLOAT,s_comment:STRING
partsupp_schema=ps_partkey:INTEGER,ps_suppkey:INTEGER,ps_availqty:INTEGER,ps_supplycost:FLOAT,ps_comment:STRING
customer_schema=c_custkey:INTEGER,c_name:STRING,c_address:STRING,c_nationkey:INTEGER,c_phone:STRING,c_acctbal:FLOAT,c_mktsegment:STRING,c_comment:STRING
orders_schema=o_orderkey:INTEGER,o_custkey:INTEGER,o_orderstatus:STRING,o_totalprice:FLOAT,o_orderdate:DATE,o_orderpriority:STRING,o_clerk:STRING,o_shippriority:INTEGER,o_comment:STRING
lineitem_schema=l_orderkey:INTEGER,l_partkey:INTEGER,l_suppkey:INTEGER,l_linenumber:INTEGER,l_quantity:FLOAT,l_extendedprice:FLOAT,l_discount:FLOAT,l_tax:FLOAT,l_returnflag:STRING,l_linestatus:STRING,l_shipdate:DATE,l_commitdate:DATE,l_recieptdate:DATE,l_shipinstruct:STRING,l_shipmode:STRING,l_comment:STRING
nation_schema=n_nationkey:INTEGER,n_name:STRING,n_regionkey:INTEGER,n_comment:STRING
region_schema=r_regionkey:INTEGER,r_name:STRING,r_comment:STRING

for table in ${tables};
do
  schema_val=${table}_schema
  bq load --source_format=CSV -F '|' ${dataset}.${table} ${data_folder_path}${table}.tbl ${!schema_val}
done
