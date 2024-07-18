# AWS IAM (Identitiy and Access Management)

## Types of AWS Credentials

- Username and Password
- Multifactor Authentication (MFA)
- IAM User Access Keys
  - Used to digitally sign API calls made to AWS services via HTTPS, CLI, or SDK
- AWS EC2 Key Pairs
  - Used for SSH/RDP access to EC2 instances. Doesn't show who uses the key, so best practice is to Add the EC2 instances to a directory domain for federated access, when access is required frequently. 

## IAM Users
An IAM User is an AWS account which can have policies or permission sets assigned to it. IAM Users can authenticate through the mentioned credential types, but do require each form of authentication. IAM Users can either be given console access or just be given CLI access, therefore it is not required that an IAM User has a password set (authentication through access keys)



### IAM User Access Keys
Access keys allow IAM Users to authenticate through CLI. They do not change or rotate automatically. 

```
EXAMPLE KEY PAIR
---------------------------------------------------------
Access Key ID: AKIAIOSFODNN7EXAMPLE
Secret Access Key: wkadjiofkwefi/siwefakaf/afdEXAMPLEKEY
```

- Access keys can be *created*, *deleted*, *inactive*, or *active*.
- An IAM user can have **two access keys**. This is so you can generate new ones, migrate your apps to new keys, then destory old ones. 
- Secret Access Key can only be seen at creation, and will **not** be visible ever after (must make a new set). 
- *IAM Users* are the only identity which uses access keys. 
