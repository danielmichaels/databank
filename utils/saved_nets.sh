#!/bin/bash
# needs to be chmod +x <name>
# run with sudo

declare -a networks #the array where we will store all saved networks
n=0
for network in /etc/NetworkManager/system-connections/*; do
    networks[$n]="$(basename "$network")"
    (( n++ ))
done

#list all networks in a line
echo "All nets in one line"
echo
echo ${networks[*]}
echo

#list networks one by one
for (( i=0; i<${#networks[@]}; i++ )) {
    echo ${networks[$i]}
}

unset networks
