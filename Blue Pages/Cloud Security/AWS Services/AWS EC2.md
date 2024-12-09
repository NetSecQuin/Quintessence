# AWS EC2

### Instance Metadata
Instance metadata is data that the EC2 Service provides to its instances regarding the enviornment that it is running in. Things like:
- Hostname, events, security groups, information on the networking, authentication (ec2-instance-roles)
- It is not authenticated or encrypted

It is accessible inside **all** instances via the address http://169.254.169.254/latest/meta-data/
- REMEMBER THIS URL FOR EXAM

Instance Metadata Command Cheatsheet:
```
curl http://169.254.169.254/latest/meta-data/public-ipv4
curl http://169.254.169.254/latest/meta-data/public-hostname

#Download the instance meta-date script and use it to query for desired information
wget http://s3.amazonaws.com/ec2metadata/ec2-metadata
chmod u+x ec2-metadata

ec2-metadata --help
ec2-metadata -a
ec2-metadata -z
ec2-metadata -s
```


