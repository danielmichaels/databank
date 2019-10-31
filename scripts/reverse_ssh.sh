#!/bin/sh

#set -x

####### VARIABLES #########
# User set viariables 
SERVER=""
SERVER_HOST="ubuntu"
PORT="8888"
SSHPORT="2220"
PRIV_KEY="/$HOME/.ssh/awsTC3G-db"
##### END VARIABLES #######

reverseSsh() {
# function will create a reverse tunnel to specified server
	if ssh -K 300 -I 110 -N -f -R $PORT:localhost:$SSHPORT -i $PRIV_KEY $SERVER_HOST@$SERVER ; then
	    echo -e "SSH Reverse shell created at $SERVER:$PORT $(date)" >> /var/log/reverseSsh.log
	else
	    echo -e "SSH Reverse tunnel FAILED $(date)"
	fi 
}

# ps ax looking for $SERVER and if not found execute reverseSsh function
if ps ax | grep -v 'grep' | grep "$SERVER" ; then
	echo -e "Tunnel exists. Nothing to do"
else
	reverseSsh
	echo -e "No Tunnel. Executing Reverse SSH Tunnel to $SERVER"
fi
