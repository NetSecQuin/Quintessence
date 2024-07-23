# AWS IAM (Identitiy and Access Management)

## Glossary

- Pricipal: An identity the needs a type of access in order to make a request.
- Amazon Resource Name (ARN): Uniquely identify individual resources within an AWS Account

## Types of AWS Credentials

- Username and Password
- Multifactor Authentication (MFA)
- IAM User Access Keys
  - Used to digitally sign API calls made to AWS services via HTTPS, CLI, or SDK
- AWS EC2 Key Pairs
  - Used for SSH/RDP access to EC2 instances. Doesn't show who uses the key, so best practice is to Add the EC2 instances to a directory domain for federated access, when access is required frequently. 

## IAM Users

IAM users are an identity used for anything requiring long-term AWS access (Humans, Applications, and Service Accounts)

An IAM User is an AWS account which can have policies or permission sets assigned to it. IAM Users can authenticate through the mentioned credential types, but do require each form of authentication. IAM Users can either be given console access or just be given CLI access, therefore it is not required that an IAM User has a password set (authentication through access keys)

Note: There can only be 5,000 IAM Users per account, and IAM user can only be a member of up to 10 groups.
- IAM Roles & Identity Federation fix this


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

## Amazon Resource Names (ARN)

Amazon Resource Name (ARN) are uniquely identify individual resources within an AWS Account. ARNs are collections of fields, split by a `:`. 

```
arn:parition:service:region:account-id:resource-id
```
The ending of `:` or `/` will depend on the service and resource type.
```
arn:parition:service:region:account-id:resource-type/resource-id
arn:parition:service:region:account-id:resource-type:resource-id
```

- A `*` would give access to all fields of that collection
  - Ex. `arn:partition:service:*:account-id:resource-id` would give access to all regions

- A *double* `:` is used when there is nothing between it, and it doesnt need to be specifified.
  - Ex. S3 buckets are globaly unique so listing a region or account number isnt necessary

Some actions are taken on a resource (Ex. S3 bucket), and some actions are taken on the objects within a resource (Ex. Objects in an S3 bucket)

Bucket: ``` arn:aws:s3:::plantpics ```
Objects in the Bucket ``` arn:aws:s3:::plantpics/* ```

## IAM Policies

IAM policies are attached to AWS identities and will either **allow** or **deny** access to an AWS resource or service. 
- If there are two rules that overlap they both will be interpreted by the system
  - Explicit **deny** will over rule anything
  - Explicit **allow** will over rule anything, **unless** there is an explicit **deny**
  - If there is not an explicit **allow** (or explicit deny), access will default to **deny**
 
This gets more complicated when there are more than one policy that applies, but the same logic applies. Example:

1.) Sally has 2 IAM Policies attached

2.) Sally is in the *Developers* OU group, which has an IAM policy attached

3.) The AWS resource (S3 bucket for example), has an attached IAM policy

### Managed Polcies vs Inline Policies

- Inline: Attached and managed at a per identity basis. Used for special or exceptions to the access rights (allows or denys)
- Managed: Created as their own object and attached to multiple identities. Should be used by default. Reusable & have low management overhead


