#!/bin/bash
# Script that generates Hugo metadata.
# Takes one CLI  argument of FILENAME.

DATA="
+++
title = \"\"
categories = [\"\"]
tags = [\"\"]
slug = \"\"
date = \"$(date +'%d %B %Y')\"
draft = \"true\"
+++
"

FILENAME=$1.md
FILE=$FILENAME

if [ -e $1.md ]; then
  echo "File Aleady Exists"
else
  touch $FILENAME
  echo "$DATA" > $FILE
fi
