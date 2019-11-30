#!/bin/bash

# chmod +x <script name> or
# sh <script name>

# VARIABLES
NAME="Roger Ramjet"
echo "$NAME"

# COMPARISON
NUM1=1
NUM3=3

# bash is white space aware:
# if ["$NUM1.. will fail without the space after [
if [ "$NUM1" -gt "$NUM3" ]
then
  echo "$NUM1 is greater than $NUM3"
else
  echo "$NUM1 is less than $NUM3"
fi

# FILE COMDITIONS
# -d file   True if the file is a directory
# -e file   True if the file exists
# -f file   True if the provided string is a file (pref over -e)
# -g file   True if the group id is set on a file
# -r file   True if the file is readable
# -s file   True if the file is a non-zero size
# -u        True if the user id is set on a file
# -w        True if the file is writable
# -x        True if the file is executable

FILE1="learn_bash.sh"
if [ -f "$FILE" ]
then
  echo "$FILE is a file"
else
  echo "$FILE is not a file"
fi

# CASE STATEMENTS
read -p "are you 18 or old? [yN]" ANSWER
case "$ANSWER" in 
  [yY] | [yY][eE][sS])
    echo "You are old enough to vote."
    ;; # ends case block
  [nN] | [nN][oO])
    echo "no voting for you"
    ;;
  *) # fall thru
    echo "Please enter Y/N only"
    ;;
esac

# LOOPS

## simple loop
NAMES="Brad Kevin Mickey Laura"
for NAME in $NAMES;
do
  echo "Hello $NAME"
done

## create some files
## checking if they exist already
FILES="test1.test test2.test test3.test"
for FILE in $FILES;
do
  if [ -f "$FILE" ]
  then
    echo "$FILE exists"
  else
    touch $FILE
    echo "$FILE created!"
  fi
done

## delete the files
for FILE in $FILES;
do
  if [ -f "$FILE" ]
  then
    echo "$FILE is being deleted..."
    rm $FILE
    echo "$FILE deleted!"
  else
    echo "Nothing to delete"
  fi
done

# WHILE LOOP
# read line by line of file
#LINE=1
#while read -r CURRENT_LINE
#do echo "$LINE: $CURRENT_LINE"
#  ((LINE++))
#done < "./learn_bash.sh"

# FUNCTIONS

function greet() {
  echo "Hello I am $1 and i am $2"
}
greet "Roger Ramjet" "22" # how to call parameters









