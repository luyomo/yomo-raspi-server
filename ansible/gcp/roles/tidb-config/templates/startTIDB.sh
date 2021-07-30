#!/bin/bash

tiup cluster deploy dmmtest v5.1.0 /opt/ycsb/deploy.yml

tiup cluster start dmmtest
