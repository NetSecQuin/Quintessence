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

IAM users are an identity used for anything requiring long-term AWS access (Humans, Applications, and Service Accounts) and can be tied to a signle principal (Ex. Single User)

An IAM User is an AWS account which can have policies or permission sets assigned to it. IAM Users can authenticate through the mentioned credential types, but do require each form of authentication. IAM Users can either be given console access or just be given CLI access, therefore it is not required that an IAM User has a password set (authentication through access keys)

Note: There can only be 5,000 IAM Users per account, and IAM user can only be a member of up to 10 groups.
- IAM Roles & Identity Federation fix this


#### IAM User Access Keys
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


#### AWS CLI

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

#### Managed Polcies vs Inline Policies

- Inline: Attached and managed at a per identity basis. Used for special or exceptions to the access rights (allows or denys)
- Managed: Created as their own object and attached to multiple identities. Should be used by default. Reusable & have low management overhead

## IAM Groups

IAM Groups are simply containers for IAM users. 

Groups allow grouping users together and can have policys attached to them (Either Inline or Managed). Users can still have additional policies attached to them 

- Groups can not be nested.
- You can have up to 300 Groups. 

Trick question: There is no 'all users group' created natively. 

Note:
- You can not login to an IAM group, they do not have any credentials. 
- Resources can have policies attached to it, which reference Users and Roles, but Groups are not a true identity, therefore they can *not* be referenced as a principal in a policy.

## IAM Roles

Role is an identity best used by a number of principals that must make use of access. It is best used on a temporary basis. It is not something that represents 'you' (a human), it is a set of permissions/access that can be used by multiple identities and represent a level of access within an AWS account. 

IAM roles are assumed.. You become that role (borrow the permissions for a short period of time)

IAM roles have two types of policies that can be attached
- Trust Policy: Controls which identities (IAM users, Roles, Services, or even allow anonymous usage or other identities (facebook, twitter, ect.) can *assume* that role.
- Permission Policy: Controls what access permissions the role has
  - When an identity *assumes a role*, AWS issues temporary security credentials (similar to time-limited **Access keys**) through AWS STS:AssumeRole.

#### When to use IAM Roles
If you do not know the number of principals that will be using the access. 

1.) AWS Lambda: By default Lambda does not have any permissions, therefore it needs permissions to run. A *Lambda Execution Role* can be used to provide a lambda function with temporary credentials in order to access AWS resources. 
  - Without Assuming a role, you would need to hard code credentials into the Lambda function.. which is a no-no.

2.) Break Glass Emergency Roles. User has default access of Read-Only, but in emergencies may need write permissions. A role with write permission may be created and assumable, with extra logging and alerting around its usage to isolate default permissions, but provide additional access in emergencies. 

3.) Adding AWS into ane exsisting enviornment, with exsisting identies (Active Directory). External identies can not be used to directly interact with AWS resources, so by assuming a role, external identities can assume the permissions to access AWS resources. Additionally there is a limit of 5000 identities in AWS, so by using assumed roles we can circumvent this limit. 

4.) You have a web application or mobile app that has millions of users. This application utalizes an AWS service DynamoDB. The app allows users to login with web identities (facebook, google, twitter, etc.), which can then assume a role in order to access DynamoDB resources. This prevents each end-user from needing an AWS account (which would hit the 5000 limit). This also prevents AWS credentials on the app. 

5.) Within AWS Organizations when you need to access a resource or service in a partner/member account. Instead of having every user have a user-account in each AWS account in the organization, we can use roles to allow cross account access. 

#### Service-linked Roles & PassRole

Service-Linked roles are IAM roles linked to a specific service, and its permissions are predefined by the service. It may be created by the service itself, or it may be created during setup of a service usecase. 

Passrole permissions allows a user who does not have a full set of permissions, to pass a role into a service that has the necessary permissions. For example, When a end-user is using a CloudFormation template to create an EC2 instance, but does not have the permissions to create an EC2 instance themselves, they can pass CloudFormation a role that has the permissions to fufil the Stack operation and create the physical resources. 


#### EC2 Instance Roles

A role that allows the EC2 service to assume the role. 

In order for the roles credentals to be delieved to the inside of an EC2 instance (so things running in the EC2 can use the role), an instance profile is created under the same name as the IAM role. (IF created in the console UI, this occurs automatically, but if through CLi or CloudFormation, you must create the instance profile manually/seperately.)
Credentials are then delievered to the EC2 instance through the instance meta-data. Additionally EC2 and STS work with eachother when using EC2 instance roles, consitantly checking the metadata, and renewing/rotating temporary credentials before they expire.

#### Exteral ID

Used when connecting to an external service at another company/organization through assume role, to provide additional validation that the requested is who they say they are, since Role ARNs are not private values. 

Works by providing an additional randomly generated ExternalId in order to solve the 'confused deputity' vulneribility/problem. 
- Confused Deputity: When an AWS account uses a role ARN to request resources from an external organization where the ARN has access, it will be provided. However this leaves a vulnerability where a different AWS account could figure out the role ARN and make requests on their behalf. (Role ARNs are not private values). This can be fixed through requiring an externalID in the request, in addition to the role ARN. 

## IAM Policies

IAM Policies are attached to *identities* and **allow** or **deny** access to take an action. All AWS permissions begin with an implicit Deny, therefore everything is blocked by default unless explicitly allowed. If there is an overlap in the permissions from two statement blocks, an explicit **deny** will always over rule an explicit **allow**. 
- Ex. 1st policy or statement block allows all S3 access. 2nd blocks write access. > All write access will be blocked. (Does not matter order of the statement blocks, it is not hierarchical.)

#### Statements
Statements contain a set of permissions (allow or deny) for a single use case. There can be numerous statement blocks within a statement. 

- 1.) Identity how many *Statement* blocks there are. These are identitfied by being contained within `[` `]`, and traditionally will begin with 'Statement". 
- 2.) Identify what each *Statement* does. Statement blocks are contained within `{` `}`.

#### Statement Blocks
Statements can contain 1 or more statement blocks. 
A statement block can contain:

- an `Sid:` : A name or ID for the statement block
- An `Effect:` : Can be either Allow or Deny.
- An `Action:` : A list of actions that will be part of the policy. Will be an API action (Ex. S3:PutObject).
- A `NotAction:` : A list of actions that will **not** be part of the policy. Inverse of Action. (Ex. `NotAction: iam:*` would included all actions *other that* iam.) 
- A `Resource:` : An ARN associated with a named resource. Whenever evaluating a policy, ensure to identify any wildcards.

**Condition block types**
- A `Condition:` : An explicitly mapped condition that must be *True* for the condition block to be active.
  - `StringEquals` & `StringNotEquals`
  - `StringLike` : Used commonly with `s3:prefix:` to apply access to specific folders within an S3 bucket.

Tips:
- Best to start with a large allow, then following statement blocks get more granular with *Deny* statements.
- When looking for overlap in permissions (allow or deny), first look at the resource ARN to see if it matches or overlaps prior statement blocks.
- If you have a Policy with a single statement that only contains a *deny* (no allow), it will likely be used in conjuncture with another policy
- Be hyper aware of inverse fields (Ex. `NotAction`, `StringNotEquals`) **BIG EXAM AREA QUESTION**
- Three actions require the resource to be a wildcard `Resource: "*"`. They are `s3:CreateBucket`, `s3:ListAllMyBuckets`, and `s3:GetBucketLocation`

#### Policy Evaluation Logic
When AWS is determaining whether access should be **allowed** or **denied**, it goes through the following sets of policies in order to determain what permissions are present:

- 1.) Organization SCPs
- 2.) Resource Policies
- 3.) IAM Identity Boundaries
- 4.) Session Policies
- 5.) Identity Policies

AWS will look at all policies and check for an *explicit allow* in each policy in the following order. If there is an *explicit allow*, AWS will look continue to look at the following policy. For efficiancy, AWS will look for *explicit denies* in order to go through a limit number of policies. The order of operation is as follows:
- 1.) Are there any explicit denies?
- 2.) Are there any SCPs associated with the identity account that would explicitly deny this activity?
- 3.) Are there any Resource Policies attached to the resource that would explicitly allows this activity?
- 4.) Are there any Permission Boundaries
- 5.) Is there a session policy that limits/denies permissions when assuming the IAM role?
- 6.) Last are there any identity policies that specifically define an explicit allow? If so, access is allowed. 


Note: With multiple accounts, there needs to be an **allow** in **both** the account making the request and in the acccount recieving the request. 

#### Permission Boundaries

Permission boundaries apply at the identity level, and allow for limiting permissions beyond an attacked IAM policy. You can create a permission boundary, which acts as a wrapper to the idenitity account, to exclude the possible permissions that an identity can recieve. The most common usecase for permission boundaries is to limit priveledge escalation as you can never create a resource that has greater permissions that the one creating it. 

This works by creating a boundary policy, where all future resources/accounts that the user with original boundary policy, is automatically also applied to everything they create. 

Ex. Administrator creates 'bob' a user account in order to be an IAM administrator. 'bob' the account has a permission boundary attached to it. The permission boundary only allows 'bob' to create new users that also have the same permissions boundary policy attached to it. 

#### Policy Actions











## Policy Variables

Policy varaibles allow you to add varaibles to IAM policies which match enviornment, account or resource attributes. 

In this following example, we are assigning access to the user *bob* to access the *user/bob*'s IAM access keys. This can not scale because if we add this policy block to another user (user *jane*), the account *jane* would have access to bob's access keys, not Jane's.

```
{
  "Version": "2024-07-23",
  "Statement": [{
    "Action": [iam:*AccessKeys*],
    "Effect": "Allow",
    "Resource": ["arn:aws:iam::account-id:user/bob"]
  }]
}
```

In the next example, we use Policy variables to pull the username of the user that the policy pertains too. This allows the tempate to be scalable and attached to a group or OU. 

```
{
  "Version": "2024-07-23",
  "Statement": [{
    "Action": [iam:*AccessKeys*],
    "Effect": "Allow",
    "Resource": ["arn:aws:iam::account-id:user/${aws:username}"]
  }]
}
```

Learn more about [Policy Variables](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html)


