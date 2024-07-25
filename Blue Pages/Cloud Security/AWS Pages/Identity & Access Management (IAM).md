# Identitiy and Access Management

## Types of AWS Credentials

- Username and Password
- Multifactor Authentication (MFA)
- User Access Keys
  - Used to digitally sign API calls made to AWS services via HTTPS, CLI, or SDK
- AWS EC2 Key Pairs
  - Used for SSH/RDP access to EC2 instances. Doesn't show who uses the key, so best practice is to Add the EC2 instances to a directory domain for federated access, when access is required frequently. 

## IAM Services

[AWS IAM](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20IAM.md) - Manage Crendential policies and IAM Resources (Groups, Users, Roles, Policies(Permissions), and Identity Providers)

[AWS Identity IAM Center](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Identity%20IAM%20Center.md) - Configure SSO or SAML from your organizations LDAP (Active Directory) with AWS IAM. 

[AWS Organizations](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Organizations.md) - Organize multiple AWS accounts at once. Group accounts into OUs. Automate creation of new accounts.

[AWS Secrets Manager](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Secrets%20Manager.md) - Manage credentials and Keys. Call API instead of hardcoding credentials. Automate secret rotation.  

[AWS STS](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20STS.md) - Temporary credentials for an IAM user that needs permisions of a differnt role for a short time.

[AWS Directory Services](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Directory%20Services.md) - Active Directory DCs in AWS. Extended current AD. Build AWS AD. Manage access for AD users to services & resources. 

[AWS Cognito](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Cognito.md) - Add/Manage your website's user accounts. Give those users access to credentials that can utalize AWS services. 

[AWS Control Tower](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Control%20Tower.md) - Allows for easy config and setup of multi-account enviornments with the Landing Zone, Guard Rails, Account Factory, and the Dashboard. 

[AWS Identity Federation](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Identity%20Federation.md) - Allow use of external Identity Providers (IdP) to authenticate to AWS resources
