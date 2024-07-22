# AWS Resource Access Manager

Allows you to share AWS resources between AWS Accounts. Substantially changes to traditional AWS Architectures (before you would use VPC peering and transit gateways) There is no cost to using AWS Resource Access Manager, other than the costs for the resources managed. 

Resources and products can be shared through *principals** (Accounts, OUs, or ORGs), and can be accessed natively (Console or CLi)

*Note: AWS rottate which phsical facilities are uased for availability Zones ** My us-east-1a, might not be the same as your us-east1a** (it could be us-east-1b). This is why AZ IDs exsist. Format is **use1-az1**)*

## How it works

The **Owner Account** (AWS account that owns the resource), creates a share and provides a name. They also define the **principal** with whom to share.
- A VPC can be created which provide shared infrastructures services to other AWS Accounts.
- The Owner account has full control of the resources it creates. Where participants will have provissioned access. For example. The owner of the VPC is the only one that can modify subnets and the resources it owns inside. If the AWS account that had the VPC shared with it creates a resource in the VPC, it is the owner of the resource. Only the owner of a resource can modify or delete it.


Sharing access to a resource is handled differently depending on if the accounts are within the same AWS Organization.
- If the participant being shared with is within the ORG, then sharing is enabled automatically. 
- If the target of the sharing is outside of the ORG, then an 'acceptable invite' is sent. 

Some resources can be shared with **any** AWS account, others can only be shared within **AWS ORG accounts**. Not all products support Resource Access Manager. 
