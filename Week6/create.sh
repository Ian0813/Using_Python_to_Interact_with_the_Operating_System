#!/bin/bash

if [ "$#" -eq 1 ] ; then
if [ -f "$1".sh ]
then
	echo "The file already exist."
else
	echo "Create " $1 ".sh"
	echo "#!"$(which bash) >> $1.sh
	chmod +x $1.sh
fi
elif [ "$#" == 2 ] ; then
	echo "#!"$(which python3) >> $2.py
	chmod +x $2.py
fi

clean(){
	rm *.py *.sh
}

