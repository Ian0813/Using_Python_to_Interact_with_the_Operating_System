#!/bin/bash
if [ -e "$1".py ];
then
	echo "$1.py already existed."
else
	echo "#!"`which python3` >> $1.py
fi
