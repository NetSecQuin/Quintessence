# Amazon Web Services (AWS)

## AWS Certifications

#### [AWS Certified Security - Specialty SCS-C02](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Certified%20Security%20-%20Specialty%20SCS-C02.md)

## Regions and Availability Zones

AWS offers the capability to host your devices, data, and networks from a variety of different data centers. This is covered through Regions, or locations like Washington or Signapore, and availability zones which are entirely isolated/seperated data centers in that locations or region. 

Choosing a **Region** and **Availibility Zone** is a big choice as there are certain factors that need to be considered when storing your data.
- The data center closes to your clients will provide the best user-experience.
- The Region may have certain costs associated to it (Higher electricity costs, infrastructure needs, and regulations impact region costs).
- The data stored may have certain compliance regualtions around the region or country.
- Disastor recovery backups may need to be stored at a different data center.
- Some regions do not offer all AWS services

## Categories

#### [AWS Logging, Monitoring, and Alerting](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Logging%2C%20Monitoring%2C%20and%20Alerting.md)

#### [Identify Access Managment (IAM)](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/Identity%20%26%20Access%20Management%20(IAM).md)

#### [Infrastructure Protection](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Infrastructure%20Protection.md)

#### [Data Protection](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Data%20Protection.md)

#### [Incident Response](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Incident%20Response)

## All Services

#### [AWS Artificat](https://github.com/NetSecQuin/Quintessence/tree/main/Blue%20Pages/Cloud%20Security/AWS%20Services)

#### AWS IAM - Manage Crendential policies and IAM Resources (Groups, Users, Roles, Policies(Permissions), and Identity Providers)

#### [AWS Identity IAM Center](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Identity%20IAM%20Center.md) - Configure SSO or SAML from your organizations LDAP (Active Directory) with AWS IAM. 

#### [AWS Organizations](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Organizations.md) - Organize multiple AWS accounts at once. Group accounts into OUs. Automate creation of new accounts.

#### [AWS Secrets Manager](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Secrets%20Manager.md) - Manage credentials and Keys. Call API instead of hardcoding credentials. Automate secret rotation.  

#### [AWS STS](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20STS.md) - Temporary credentials for an IAM user that needs permisions of a differnt role for a short time.

#### [AWS Directory Services](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Directory%20Services.md) - Active Directory DCs in AWS. Extended current AD. Build AWS AD. Manage access for AD users to services & resources. 

#### [AWS Cognito](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Cognito.md) - Add/Manage your website's user accounts. Give those users access to credentials that can utalize AWS services. 

[AWS VPC](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20VPC.md) - Creating VPCs to isolate resources with defense-in-depth, via Subnets > NACLs > Security Groups

[AWS Systems Manager (SSM)](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Systems%20Manager.md) - Automate changes, patching, installs, and more across numerous hosts at once. Login directly through SSM agent.

[AWS Firewall Manager](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Firewall%20Manager.md) - Central location to manage firewalls, WAFs, and AWS Services to manage and centrally push changes to gateways. 

[AWS Direct Connect](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Direct%20Connect.md) - Connect internal network or data centers to a location with a physical connection to the AWS Network. Bypassing the public internet. 

[AWS CloudFormation](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20CloudFormation.md) - Infrastructure as code through creating and deploying templated configurations into CI/CD pipeline. 

[AWS Inspector](https://github.com/NetSecQuin/Quintessence/tree/main/Blue%20Pages/Cloud%20Security/AWS%20Services) - Vulnerability scanning of instances, containers, and Lambda functions directly integrated into the CI/CD pipeline. 


#### [CloudTrail](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20CloudTrail.md) - Every action in an AWS account is an API call. All AWS API calls are documented in CloudTrail. 

#### [CloudWatch] - Instances can have CloudWatch agents installed. Agents report to CloudWatch. CloudWatch logs > Events & Alarms. 

- #### [EventBridge]

#### [AWS Guard Duty](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Guard%20Duty.md) - AWS built in threat detection through intel intel feeds, suspicious anomalie detection, and threat based activity. 

#### [AWS Security Hub](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Security%20Hub.md) - Centralized view for aggregating, organizing, and taking action on security alerts from multiple AWS Services 

#### [AWS Trusted Advisor](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Trusted%20Advisor.md) - Identify places to lower costs. Align with security standards. Improve resiliance and preformance of resources

#### [AWS VPC Flow Logs](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20VPC%20Flow%20Logs.md) - Track network activity to your instances inside a VPC. Troubleshoot connectivity and identify network threats. 

#### [AWS Config](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Config.md) - View current & historic configuration changes to troubleshoot outages or analyze security incidents. 

[AWS CloudHSM](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20CloudHSM.md) - Dedicated Hardware Security Modules (HSM) for cryptographic key generation and management. (For certain usecases of sensitive data)

[AWS KMS](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20KMS.md) - AWS Managed HSM for cryptographic key generation and management (Simple and fits most usecases) 

[AWS S3 Glacier](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20S3%20Glacier.md) Store data that does not need frequent access at low costs. Use Glacier Vault Lock to ensure tamper proof storage. 

[AWS Certificate Manager](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Certificate%20Manager.md) - Create and manage SSL/TLS certificates for your public or private webpages and applications.

[AWS Macie](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Macie.md) - Scan S3 for sensitve data with ML. Identify unencrypted data and insecure bucket policies. 




## To Be Added or Deleted. 

#### [Key Managment Service (KMS)]()

#### [AWS Systems Manager (ASM)]()

#### [Lambda]()

