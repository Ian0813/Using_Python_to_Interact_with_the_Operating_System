#!/bin/bash  

for i in about contact footer header index ; do touch "$i".HTM ;done


clean(){
	rm *.html *.HTM
}

#clean
