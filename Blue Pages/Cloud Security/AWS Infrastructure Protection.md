# AWS Infrastructure Protection

### Network Protection
 - AWS VPC is used to isolate resources with subnetting, Network ACLs, and Security groups. These three layers can block inbound and outbound traffic according to specific IP address, Protocol, or ports, mentioned in policy.

### Application & OS Protection
- AWS Systems Manager
- AWS Firewall Manager
- AWS Direct Connect
- AWS Cloudformation

## Services

[AWS VPC](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20VPC.md) - Creating VPCs to isolate resources with defense-in-depth, via Subnets > NACLs > Security Groups

[AWS Systems Manager (SSM)](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Systems%20Manager.md) - Automate changes, patching, installs, and more across numerous hosts at once. Login directly through SSM agent.

[AWS Firewall Manager](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Firewall%20Manager.md) - Central location to manage firewalls, WAFs, and AWS Services to manage and centrally push changes to gateways. 

[AWS Direct Connect](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Direct%20Connect.md) - Connect internal network or data centers to a location with a physical connection to the AWS Network. Bypassing the public internet. 

[AWS CloudFormation](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20CloudFormation.md) - Infrastructure as code through creating and deploying templated configurations into CI/CD pipeline. 
