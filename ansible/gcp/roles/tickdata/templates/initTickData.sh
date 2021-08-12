#!/bin/bash

source /home/jay_zhang/.bashrc

/usr/local/go/bin/go get /opt/stock-api
/usr/local/go/bin/go run /opt/stock-api/mainGenerateData.go --db-host={{ tidb_gateway_ip  }} --db-port=4000 --db-user=tickuser --db-pass=tickuser --db-name=tickdata --threads=1 --rows=10 --count=1
