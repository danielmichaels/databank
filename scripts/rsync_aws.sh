#!/bin/sh
# TODO tidy up, look at changing this to dump into s3.
# This script will "push" contents of the logger to an ec2 instance

########## VARIABLES ############
SSHPORT="2220"
KEYFILE="/root/.ssh/<keyfile>"
SERVER="ec2-<ip>.ap-southeast-2.compute.amazonaws.com"
SERHOST="ubuntu"
LOCAL_DIR=""
REMOTE_DIR=""
######## END VARIABLES ###########

rsync -aPH -zz -e "ssh -p $SSHPORT -i $KEYFILE" $LOCAL_DIR $SERHOST@$SERVER:$REMOTE_DIR -h 2>&1 | awk '{ print strftime(), $0; fflush() }' >> /var/log/rsync.log
