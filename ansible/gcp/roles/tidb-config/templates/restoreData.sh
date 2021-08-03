#!/bin/bash

tiup br restore full --pd "{{ componentIPs['pd'] | first }}:2379" -s "local:///DATA/backup"
