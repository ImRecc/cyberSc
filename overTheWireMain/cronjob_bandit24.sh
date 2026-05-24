#!/bin/bash

shopt -s nullglob
# shell options
# if there are no .txt file, *.txt will be processed as normal strings
# with nullglob on, * will be null

myname=$(whoami)

cd /var/spool/"$myname"/foo || exit
echo "Executing and deleting all scripts in /var/spool/$myname/foo:"
for i in * .*;
do
    if [ "$i" != "." ] && [ "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" "./$i")"
        if [ "${owner}" = "bandit23" ] && [ -f "$i" ]; then
        # -f file, 判断$i是不是普通文件，而不是快捷方式
        # POXIS不需要双等号
            timeout -s 9 60 "./$i"
            #timeout -s signalKILL 9
            #60s timeout
            #over more 60s, kill the task via signalkill 9
        fi
        rm -rf "./$i"
    fi
done
