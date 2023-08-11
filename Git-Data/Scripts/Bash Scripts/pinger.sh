#!/bin/bash

#List of IP addresses to test conectivity via Ping
IP_LIST=("8.8.8.8" "9.9.9.9" "10.10.10.10")

# For loop to ping each address in list. For increased accuracy but slower preformance you can add more icmp packets by changing the -c count. 
for IP in "${IP_LIST[@]}"
do
  ping -c 1 $IP > /dev/null

  #check the exit code in the response of ping command to identify if it was successful 
  if [$? -eq 0]
  then
    echo "$IP is up"
  else
    echo "$IP is down"
  fi
done
