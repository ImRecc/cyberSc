#!/bin/bash  //as we used at bandit wargame before, this is to specific which bash we are use

if [ ${1,,} = x3p ]; then
	echo "welcom"
elif [ ${1,,} = help ]; then
	echo "plz enter usr"
else
	echo "idk who you are"
fi
            // $  to specific instance and {1,,} are format ...

echo what is your name?
read Name

echo Hello $Name

echo hello $1 $2

          // in this case: ./bash.sh para1 para2 
      quiet like python but..
      less and simply but enough to walk thourgh the wargame... funny

	//a login bash concept for b14 or b27 wargame
case ${1,,} in
	x3p | admin )
		echo "hello"
		;;
	help)
		echo "plz entry usr"
		;;
	* )
		echo "idk who you are"
esac
