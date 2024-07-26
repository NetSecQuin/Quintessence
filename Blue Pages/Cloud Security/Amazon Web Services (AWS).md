# Amazon Web Services (AWS)

## AWS Certifications

#### [AWS Certified Security - Specialty SCS-C02](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Pages/AWS%20Certified%20Security%20-%20Specialty%20SCS-C02.md)

## Regions and Availability Zones

AWS offers the capability to host your devices, data, and networks from a variety of different data centers. This is covered through Regions, or locations like Washington or Signapore, and availability zones which are entirely isolated/seperated data centers in that locations or region. 

Choosing a **Region** and **Availibility Zone** is a big choice as there are certain factors that need to be considered when storing your data.
- The data center closes to your clients will provide the best user-experience.
- The Region may have certain costs associated to it (Higher electricity costs, infrastructure needs, and regulations impact region costs).
- The data stored may have certain compliance regualtions around the region or country.
- Disastor recovery backups may need to be stored at a different data center.
- Some regions do not offer all AWS services

AWS also has *Edge Data Centers*, which are in 310* different locations than Availability Zones. As access to certain data increases with time, this data is copied to an *edge* location near your customer base for better performance and latency. These centers are used for end-user routing and caching on public web application use-cases primarily (CDNs, DNS, Shield). 

## Categories

#### [Account Creation](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Pages/AWS%20Account%20Creation.md)

#### [AWS Logging, Monitoring, and Alerting](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Pages/AWS%20Logging%2C%20Monitoring%2C%20and%20Alerting.md)

#### [Identify Access Managment (IAM)](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Pages/Identity%20&%20Access%20Management%20(IAM).md)

#### [Infrastructure Protection](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Pages/AWS%20Infrastructure%20Protection.md)

#### [Data Protection](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Pages/AWS%20Data%20Protection.md)

#### [Incident Response](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Pages/AWS%20Incident%20Response.md)

#### [DDoS Mitigation](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Pages/AWS%20DDoS%20Mitigation.md)

#### [AWS Projects](https://github.com/NetSecQuin/Quintessence/tree/main/Blue%20Pages/Cloud%20Security/AWS%20Pages/AWS%20Projects)

## All Services

[AWS Artificat](https://github.com/NetSecQuin/Quintessence/tree/main/Blue%20Pages/Cloud%20Security/AWS%20Services) - Provides audit & compliance documents for AWS's side of the shared responsibility model.

[AWS IAM](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20IAM.md) - Manage Crendential policies and IAM Resources (Groups, Users, Roles, Policies(Permissions), and Identity Providers)

[AWS Identity IAM Center](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Identity%20IAM%20Center.md) - Configure SSO or SAML from your organizations LDAP (Active Directory) with AWS IAM. 

[AWS Organizations](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Organizations.md) - Organize multiple AWS accounts at once. Group accounts into OUs. Automate creation of new accounts.

[AWS Secrets Manager](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Secrets%20Manager.md) - Manage credentials and Keys. Call API instead of hardcoding credentials. Automate secret rotation.  

[AWS STS](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20STS.md) - Temporary credentials for an IAM user that needs permisions of a differnt role for a short time.

[AWS Directory Services](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Directory%20Services.md) - Active Directory DCs in AWS. Extend current AD/Build AWS AD. Manage AD user access to resources. 

[AWS Cognito](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Cognito.md) - Add/Manage your website's user accounts. Give those users access to credentials that can utalize AWS services. 

[AWS VPC](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20VPC.md) - Creating VPCs to isolate resources with defense-in-depth, via Subnets > NACLs > Security Groups

[AWS Systems Manager (SSM)](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Systems%20Manager.md) - Automate changes, patching, installs, etc. across numerous hosts at once. Login through SSM agent.

[AWS Firewall Manager](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Firewall%20Manager.md) - Central location to manage firewalls, WAFs, and AWS Services to manage and centrally push changes to gateways. 

[AWS Direct Connect](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Direct%20Connect.md) - Connect internal network or data centers to a location with a physical connection to AWS. Bypass the public internet. 

[AWS CloudFormation](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20CloudFormation.md) - Infrastructure as code through creating and deploying templated configurations into CI/CD pipeline. 

[AWS Inspector](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Inspector.md) - Vulnerability scanning of instances, containers, and Lambda functions directly integrated into the CI/CD pipeline. 


[CloudTrail](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20CloudTrail.md) - Every action in an AWS account is an API call. All AWS API calls are documented in CloudTrail. 

[CloudWatch] - Instances can have CloudWatch agents installed. Agents report to CloudWatch. CloudWatch logs > Events & Alarms. 

- [EventBridge]

[AWS Guard Duty](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Guard%20Duty.md) - AWS built in threat detection through intel intel feeds, suspicious anomalie detection, and threat based activity. 

[AWS Security Hub](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Security%20Hub.md) - Centralized view for aggregating, organizing, and taking action on security alerts from multiple AWS Services 

[AWS Trusted Advisor](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Trusted%20Advisor.md) - Identify places to lower costs. Align with security standards. Improve resiliance and preformance of resources

[AWS VPC Flow Logs](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20VPC%20Flow%20Logs.md) - Track network activity to your instances inside a VPC. Troubleshoot connectivity and identify network threats. 

[AWS Config](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Config.md) - View current & historic configuration changes to troubleshoot outages or analyze security incidents. 

[AWS CloudHSM](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20CloudHSM.md) - Dedicated Hardware Security Modules (HSM) for cryptographic key generation and management.

[AWS KMS](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20KMS.md) - AWS Managed HSM for cryptographic key generation and management (Simple and fits most usecases) 

[AWS S3 Glacier](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20S3%20Glacier.md) Store data that does not need frequent access at low costs. Use Glacier Vault Lock to ensure tamper proof storage. 

[AWS Certificate Manager](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Certificate%20Manager.md) - Create and manage SSL/TLS certificates for your public or private webpages and applications.

[AWS Macie](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Macie.md) - Scan S3 for sensitve data with ML. Identify unencrypted data and insecure bucket policies. 

[AWS Step Functions](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Step%20Functions.md) - Create automated workflows where the output of one Lambda function can be pushed into a new Lambda function. 

[AWS EBS](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20EBS.md) -  Virtual HDD/SSD storage for attaching to your EC2 instances. 

[AWS Route 53](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Route%2053.md) - Scalable DNS for web applications. Includes smart routing options, monitoring, and health checks to improve preformance. 

[AWS CloudFront](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20CloudFront.md) - Amazon Content Delivery Network (CDN). Caches and serves website resources to edge locations to improve site speed. 

[AWS Shield](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Shield.md) - Automatically mitigate certain DDoS attacks through ML signature detection after creating a baseline of normal traffic.

[AWS WAF](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20WAF.md) - Block traffic inbound to your web application based on granular signatures identified in web requests.

[AWS Well-Architected Tool](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Well-Architected%20Tool.md) - Self-Service questionaire that will ask you questions in order to identify places to improve your workload. 

[AWS Control Tower](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Control%20Tower.md) - Allows for easy config and setup of multi-account enviornments with the Landing Zone, Guard Rails, Account Factory, and the Dashboard. 

[AWS Service Catalog](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Service%20Catalog.md) - A self-service catalog for end-users to *purchase** and launch predefined CloudFormation templates. 

[AWS Resource Access Manager](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Resource%20Access%20Manager%20(RAM).md) - Allows for sharing resources accross AWS accounts and ORGs. 

[AWS Identity Federation](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Identity%20Federation.md) - Allow use of external Identity Providers (IdP) to authenticate to AWS resources

[AWS SAML Federation](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20SAML%20Federation.md) - Outdated/Old Way of doing things. Exchange an external SAML based IdP credentials for AWS credentials. 

## To Be Added or Deleted. 

#### [Lambda]()

