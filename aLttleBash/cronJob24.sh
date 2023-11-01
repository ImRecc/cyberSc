#!/bin/bash

cd /var/spool/bandit24/foo
echo "Executing and deleting all scripts in /var/spool/bandit24/foo:"
for i in * .*;         //notice that * .* inclusively contained all files
do
	if ["$i" != '.' -a "$i" != ".."];      //little bit but I believe I will forgot them soon
	then 
		echo "Handling $i"
		owner="$(stat --format "%U" ./$i)"
		if [ "${owner}" = "bandit23" ]; then
			timeout -s 9 60 ./$i
		fi
		rm -f ./$i
	fi
done
