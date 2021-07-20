#!/bin/bash

/home/ec2-user/workstation/go-ycsb/bin/go-ycsb run tikv \
    -P /home/ec2-user/workstation/go-ycsb/workloads/workloadc \
    -p verbose=false -p debug.pprof=":6060" \
    -p tikv.pd="178.80.3.68:2379" -p tikv.type="raw" \
    -p operationcount=100000 -p recordcount=100000 \
    -p threadcount=500
