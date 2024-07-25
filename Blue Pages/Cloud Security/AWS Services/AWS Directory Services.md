# AWS Directory Services

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721149200/GkyF8Mg8z4_WVdL503GbNw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/JwBMkjlMshj2b_cI_TXjwBGd8McF9QbUo.png)

## Summary

AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, enables your domain workloads and AWS resources to use managed Active Directory in the AWS Cloud. AWS Managed Microsoft AD is built on the actual Microsoft Active Directory and does not require you to synchronize or replicate data from your existing Active Directory to the cloud.

For more information, see [AWS Directory Service](https://aws.amazon.com/directoryservice/).

## Use

- Build Microsoft Active Directory inside AWS.
- Extend an exsisting Active Directory configuration to the AWS Cloud.
- Manage user permissions and access tied to Active Directory users to AWS services and resources. 

## Directory Service 

#### Microsoft AD Mode
A Full instance of Microsoft Active Directory (AD) running inside AWS.
- Best choice if you have more than 5,000 users and need their to be a trust relationship between AWS and your on-prem directories. (long term hybrid on-prem + cloud based network)

Used for AD Authentication/Authorization of products and services within AWS. (When you need a native Microsoft Active Directory)
- Deploys in two AZs by default, and automatically sync in order to provide high availability in case of AZ failure
- **Can access AWS Side resources, and AWS can access AD side resources (on-prem resources).**
- Can operate through a network link faliure (If on-prem is disconnected or goes down, AWS Microsoft AD can run independantly)
- Supports RADIUS-based MFA
- Support AD Native schema extensions (required by some AD applications)


#### AD Connector


**Relays** any requests that require AD, to your exsisting on-premisis AD enviornement. It does not build or store any AD directory data in AWS. Only used in specific scenarios where it is necessary. (Ex. Small amount of AWS infrastrucutre, legal requirements that AD cant be in AWS, and proof of concepts)  

It provides existing on-premisis AD with the capability to interact with directory compatible AWS Services. It works by having a pair of directroy endpoints running in AWS (ENIs in a VPC).
- Two sizes for the AD connector : *Small* & *Large*. These control the amount of compute allocated by AWS to connector (increase throughput)
- Multiple AD connectors can be used to spread load
- Requires 2 subnets within a VPC and different AZs for redundancy.
- Connector requires 1 or more directory(s) to be configured
- **Requires** a working networking connection (no data is stored in AWS, its just a relay)
- Network connectivity via a **Direct Connect** or a **VPN**
- Proof of concepts to demonstrate a usecase temporarily before going with a full AD Mode deployment. 
