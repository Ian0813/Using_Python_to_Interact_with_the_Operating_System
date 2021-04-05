#!/bin/bash

cd old_website
for file in *.HTM ; do
	name=$(basename "$file" .HTM)
	$(mv "$file" "$name".html)
done
cd ../
pwd
ls -l ./old_website
