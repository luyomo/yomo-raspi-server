#!/bin/bash

/home/ec2-user/workstation/go-ycsb/bin/go-ycsb load tikv \
    -P /home/ec2-user/workstation/go-ycsb/workloads/workloadc \
    -p dropdata=false -p verbose=false -p debug.pprof=":6060" \
    -p tikv.pd="178.80.3.68:2379" -p tikv.type="raw" \
    -p tikv.conncount=128 -p tikv.batchsize=128 \
    -p operationcount=100000 -p recordcount=100000 \
    -p threadcount=10
