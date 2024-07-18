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
Access keys allow IAM Users to authenticate through CLI. They are *Long Term Credentials*, they do not change or rotate automatically. 

```
EXAMPLE KEY PAIR
---------------------------------------------------------
Access Key ID: AKIAIOSFODNN7EXAMPLE
Secret Access Key: wkadjiofkwefi/siwefakaf/afdEXAMPLEKEY
```

- Access keys can be *created*, *deleted*, *inactive*, or *active*. Setting keys to *inactive* is useful when you want to suspend access. 
- An IAM user can have **TWO access keys**. This is so you can generate new ones, migrate your apps to new keys, then destory old ones. 
- Secret Access Key can only be seen at creation, and will **not** be visible ever after (must make a new set). 
- *IAM Users* are the only identity which uses access keys.


### AWS CLI

To install AWS CLI for your operating system follow [this guide.](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- Once installed, open up your terminal or command line utility and run ```aws --version``` to validate the install was successful. 

With AWS CLI installed, we then want to configure a profile to connect to/as. A profile is binded to a user *Access Key*, a *Secret Key*, and an *AWS region* in order to login without having to provide the details every time. We can create a new profile with the following command example:

```
user@devicename ~ % aws configure --profile profilename
AWS Access Key ID [None]: AKIAXYKJTEXAMPLE
AWS Secret Access Key [None]: faoe3jo1289jafiasdjnewExample
Default region name [None]: us-east-1
```

*It is recommended to name the profile something related to the username and AWS account associated to it for ease.* 

To use a profile you must specify it with the command. 

```
aws s3 ls --profile profilename
```



