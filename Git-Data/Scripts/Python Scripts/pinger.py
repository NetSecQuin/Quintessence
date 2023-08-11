import os
import csv
hostname = os.getlogin()

#Create a directory for storing the results
os.system('mkdir /home/'+hostname+'/pinger')

#read in csv file of IPs to ping, change filepath to match CSV location
with open('/home/example/example.csv', newline='') as csvfile:
  reader = csv.DictReader(csvfile)

#For Loop that will cycle through each row of csv and ping 3 each 3 times
  for row in reader:
    pinger = os.system("ping " + row['IP_Address'] + " -c 3 > /dev/null 2>&1")

#Check for blocked connections and print the blocked IP addresses for a file. 
    if pinger !=0:
      print (row['IP_Address']+', is unreachable!')
      os.system('echo "'+row['IP_Address']+ ', is unreachable!" >> /home/'+hostname+'/pinger/BlockedConnections.txt)
    else"
      print (row['IP_Address']+', is up!')

print('A list of failed connections can be found at /home/'+hostname+'/pinger/BlockedConnections.txt')
