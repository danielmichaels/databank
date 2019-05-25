#!/bin/bash
# Script that generates Hugo metadata.
# Takes one CLI  argument of FILENAME.

DATA="
+++\n
title = \"\"\n
categories = [\"\"]\n
tags = [\"\"]\n
slug = \"\"\n
date = \"$(date +'%d %B %Y')\"\n
draft = \"true\"\n
+++\n
"

FILENAME=$1.md
FILE=$FILENAME

if [ -e $1.md ]; then
  echo "File Aleady Exists"
else
  touch $FILENAME
  echo -e $DATA > $FILE
fi
