#!/bin/sh

# Change this if you're using a remote server and are not me
REMOTE_SERVER="wwumc-xen.local"
# Change the 25565 to whatever port your server uses if not the default
CHECK_COMMAND="netstat -anlt | grep ':25565' | grep ESTABLISHED | wc -l"

# If Minecraft is running on the local server, use this
#clients=`$CHECK_COMMAND`

# If Minecraft is running on a different server, use this
# Make sure you have ssh keys set up for the proper local and remote user!
ping -q -c 1 $REMOTE_SERVER > /dev/null || exit 0
clients=`ssh $REMOTE_SERVER "$CHECK_COMMAND"`

# Regardless, 
exit $clients
