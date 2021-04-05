#!/bin/bash

if [ "$#" -ne 1 ] ; then
n=1

while [ $n -le 5 ] ; do
	echo "Iteration number $n"
	((n+=1))
	echo $(python3 random_exit.py)
done
else

n=0
command=$1

while ! $command && [ $n -le 5 ] ; do
	sleep $n  # why do we call the sleep command ?
		  # the idea here is that if the command we're calling is failing due to CPU usage, network or resource exhaustion.
		  # it might make sense to wait a bit before trying again
	((n+=1))
	echo "Retry #$n"
done;

fi

