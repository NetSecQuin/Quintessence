# AWS Incident Response

## Investigation Requirements



## Implement Automation Where Possible

In the following example we see AWS Step Functions being used to automate an incident response investigation through **AWS Lambda** and **CloudFormation**:

1.) Recieving and Instance ID through an SNS queue that needs to be investigated. Then using a Lambda function, finding/verifiying the instance exsists and removing if from any applicable auto-scaling groups. This prevents unintended changes or destruction of the evidence. 

2.) The next step function is a Lambda function that isolates the instance by removing all security groups and adds a forensics-sg with no ingress or egress permissions. 

3.) The next lambda function uses CloudFormation to create analysis infrastructure, including a brand new VPC and clean forensics workstation with all the tools needed for the forensic investigation. The function attaches the snapshotted EBS volume to the new forenscis investigation workstation.

4.) A lambda function with pre-written forensic analysis scripts is run to collect artifacts and additional information from the evidence. 

5.) The results that have been collected through the automated analysis scripts are organized and passed to a security analyst for further review. If additional invetigation is required, a clean and secure forensic enviorment with attached evidence is already prepared. 


![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721239200/ZEcL0bTnPYhQOsOBxow55Q/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/b2g1V-jZnvmX4qOA_sYgTi6A_iBfSMOkW.png)


## Services
