#!/bin/sh

CT=0

while [ True ]
do
	FNAME="pipic$CT.jpg"

	#Taking a snap and sending it to server
	raspistill -o "$FNAME"
	RESULT=$(curl -s -F "file=@$FNAME" http://192.168.43.22:8000/predict | grep -w "var result" | awk '{print $4}' | sed 's/.$//')
	echo "$FNAME uploaded..."

	#Getting result
	echo "RESULT = $RESULT"
	RESULT=$(echo $RESULT | sed s'/....$//')

	#Identifying Confidence from result
	CMP=$(awk 'BEGIN{ print "'$RESULT'"<"'0.9'" }')

	#Checking stress through confidence
	if [ "$CMP" -eq 1 ]
	then
		echo "SUBJECT IS UNDER STRESS"
		python buzz.py 1
		sudo python LED.py 1
	else
		echo "SUBJECT IS NOT UNDER STRESS"
		python buzz.py 0
		sudo python LED.py 0
	fi
	echo "\n"

	#Preparing for next cycle
	CT=$((CT+1))
	rm $FNAME
	sleep 2
done
