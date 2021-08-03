#!/bin/bash

gsutil -m cp -r gs://tidbjaytest/tidbtest/backup /DATA/

KV_HOSTS="{{ componentIPs ['kv'] | join(' ')  }}"
for host in $KV_HOSTS
do
  rsync -r -a /DATA/backup $host:/DATA/
done
