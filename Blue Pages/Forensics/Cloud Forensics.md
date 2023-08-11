# Cloud Forensics

### AWS 

#### Creating an investigation host

Before investigating a cloud instance, you will need to have a cloud asset in that can be used to mount and investigate the evidence. To do this we can spin up an EC2 instance. 

Click on EC2 > Instances > Launch an instance

Give it a name and select your prefered OS. I suggest Ubuntu for forensics as it seems to work best with a few of the tools. Specifically when investigating Windows evidence. 

The Instance type my depend on how large the data is the you are anaylzing. If you are going to be running big searches on large data sets you may need a host with a larger CPU. However in most cases you should be fine with a *t2.micro*

Pick a keypair or create a keypair

Click on edit next to the network settings (these settings are a little hidden), and note what VPC and subnets your EC2 is in. It will NEED to be in the same VPC and Subnet as the evidence. 

Select an exsisting security group, or create a new one that is locked down from external connections. This is to ensure that the evidence is not tampered with, or if contains malware it does not spread. 

#### Mounting a snapshot for analysis

##### Step 1. Finding the Snapshot

Under EC2 > Elastic Block Store > Snapshots, locate the snaphot you want to analyze

If there are alot of snapshots in the AWS account, you can search by the Instance state, the name of the instance, or the date, in order to fiter your search

Once the snapsot has been identified, Click on the snapshot ID. 


###### Step 2. Gathering Details

Copy the snapshot ID, and storage information into a notepad for easy reference. 


###### Step 3. Create a volume

Next we will need to create a volume from the snapshots attached drive. This can be done by clicking on "Actions" > "Create a volume from snapshot"

Note: The Availabilty zone of the created snapshot needs to be in the same availability zone as the investigation EC2

###### Step 4. Find and attach the volume 

FInd the newly created volume and identify/document its volume ID 

Click on "Actions" > "Attach Volume", then attach it to your investigation host by selecting the EC2 instance from the list

###### Step 5. Mount the drive to the EC2

Once the volume is attached to the investigation EC2, we need to mount it in order to access it. 

Login to the EC2 via SSH/SSM/Prefered Choice. Note the following commands need to be run as superuser.

run ``` lsblk ``` in order to see the available disk devices and their mount points

run ``` file -s /dev/xvdf ``` to find the disk type. *(Where "xvdf" is the evidence disk/volume)*

Create a directory for where you would like to mount the evidence. ``` mkdir /evidence ```

Mount the disk to the directory ``` mount /dev/xvdf /evidence ``` *(Where "xvdf" is the evidence disk/volume)*

### Azure


### GCP


### VMware
