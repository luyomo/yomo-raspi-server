#!/bin/bash

HOSTS="178.80.1.219 178.80.2.212 178.80.3.68 178.80.1.135 178.80.2.23 178.80.3.149"

for host in $HOSTS
do
  ssh $host "sudo mkdir /DATA"
  ssh $host "sudo chown -R ec2-user:ec2-user /DATA"
done
