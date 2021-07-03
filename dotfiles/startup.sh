#!/bin/bash

# set caps to control
setxkbmap -option ctrl:nocaps &

# set screen res and layout
xrandr --output DVI-D-0 --mode 1680x1050 --pos 0x390 --rotate normal --output HDMI-0 --off --output DP-0 --primary --mode 2560x1440 --pos 1688x0 --rotate normal --output DP-1 --off

# do not lock if sound running i.e. watching youtube
if [ $(grep -r "RUNNING" /proc/asound | wc -l) -eq 0 ]; then
  exec --no-startup-id xautolock -detectsleep -time 5 -locker "/usr/bin/betterlockscreen --lock" -corners 0-0- -cornersize 30
fi


