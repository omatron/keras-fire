#!/bin/bash

rc=0

for i in {160..1000}
do
	if [ $rc == 0 ]
	then
	python test_network_fire_alarm.py -m firev10.model -i frames/frame$i.jpg
	rc="$?"
	fi


done

