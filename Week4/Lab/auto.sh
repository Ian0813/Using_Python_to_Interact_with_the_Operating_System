#!/bin/bash


if [ ! -e errors_found.log ]
then
	./find_error.py fishy.log
#	echo "CRON ERROR Failed to start"
else
	rm errors_found.log 
fi


