# AWS S3


### S3 Bucket Policies
S3 Buckets are private by default.

Utilize a form of resource policies, which are like identity policies but attached to a bucket. 

Identity policies control what that identity can access, resource policys describe who can access that resource. 

Identity polices only control access within an AWS account, but resource policies can control access for same or different accounts. 

Resource Policy Example
- Statement 1.) Requires MFA for SuperSecret folder
- Statement 2.) Requires Source IP for access to PhotoAlbum
```
{
  "Version":"2024-12-12",
  "Statement":[
    {
      "Sid":"MFAforsecrets",
      "Effect":"Allow",
      "Principal":"*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:S3:::PhotoAlbum/SuperSecret/*"]
      "Condition": { "Null": { "aws:MultiFactorAuthAge": true } }
    },
    {
      "Sid":"OnlymyIPs",
      "Effect":"Allow",
      "Principal":"*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:S3:::PhotoAlbum/*"]
      "Condition": {
        "OnlyIPAddress": {"aws:SourceIp:" 40.41.42.43/32
    }
  ]
}
```

### S3 Access Control Lists (ACLs) - LEGACY

Significantly less flexible than a identity policy or resource policy. Only offer READ, WRITE, READ_ACP, WRITE_ACP, FULL_CONTROL, for options with access control. Only allows you to specify permissions for a specific bucket for object, not a colleciton of buckets or objects. Ex. "arn:aws:S3:::PhotoAlbum/October/*.jpg"


### Object Versioning
Object versioning allows you to store multiple versions of an object in a bucket. Ex. 3 files called main.py, where each are different versions of eachother. 

Controled at the bucket level. Once *enabled*, it can never be *disabled*. However it can be *suspended* and re-enabled. 

#### MFA Delete
Enabled in Versioning configuration, where MFA is required to change bucket versioning state and delete versions. 
- Need to provide the seriel number of your MFA token and pass it in an API call with the version ID

### S3 Object Lock

Can be enabled on new S3 buckets. Requires AWS Support to enable on exsisting S3 buckets. Once enabled you can not disable. 
- Write-Once-Read-Many (WORM) - No Delete, No Overwrite
- Requires object versioning, individual versions are what is 'locked'
- Two types of Object Lock Retention
  - Retention Period
    - Can be "Compliance" or "Governance" mode
    - Compliance Mode: Retention policy can't be adjusted, deleted, or overwritten, even by root. Retention period must expire before files can be deleted/modified.
    - Governmance Mode: Rentention policy and lock settings can be adjusted by special permissions
  - Legal Hold
    - No retention period
    - S3:PutObjectLegalHoldStatus = True , enables object lock and prevents overwriting or deleting versions until removed. 
  - None.


### Presigned URLs

Presigned URLs can be useful for when a user, who does not have AWS access, needs to upload/download a specific file(s) from S3. Presigned URLs allow an IAM user to pass specific authentication parameters and wrap it in a URL. For example. If an user is accessing a website that stores image files in S3, the website may use a service account (IAM User) to create a presigned URL of the image. This URL would be wrapped in permissions to access the specific file in the S3 bucket, for a limited amount of time, and passed to the user. 

Somet things to think about in regards to presigned URL architecture. 
- When using the URL, the permission match the identity which generated it, therefore:
  - Access denied could mean the generating ID never had access or does not now/on click.
- Dont generate with a role, URL stops working when temporary credentials expire. Therefore it is meant to be used with a IAM user.

### Cross Account Access to S3

Access to S3 buckets can be achieved across accounts via *ACLs (Legacy)*, *Bucket/Resource Policies*, and *Assuming Roles*.
- ACLs will use your Canonical user ID or a legacy identifier, to define access of other AWS account users/roles.
- Bucket/Resource Policies can specify external account conditions
- Assuming a role in another AWS account which has access to S3 bucket via identity policy and resource policy.

#### Object Ownership

When dealing with cross account access to S3, there are settings to define whether an objects is owned by the account that added the file to the S3 bucket, or the account that owns the S3 bucket. This can be defined in settings, and can be the cause of some access errors.
- Because of this, it makes more sense to use Assuming a Role, as it prevents issues where ownership of the bucket and its objects vary.

### Private S3 buckets
Resources in a private VPC can interact with S3 buckets in S3 (a public service) via a *Gateway Endpoint*. Bucket policies can be used to restrict access to only that gateway endpoint, ensuring that only private network traffic is allowed to an S3 bucket. Then the Gateway Endpoint policy can restrict access to S3 buckets at a network level. 

Otherwise, if a principal has access to an S3 bucket, they can preform the actions alloted by the IAM policy from any network. Ex. If you had an S3 bucket with sensative data inside, making it only accessible from a private VPC ensures that if a TA was to get access to AWS credentials, they would also need to have access to a resource within the private VPC. That VPC could also have a link into an on-prem network, ensuring only those on VPN can access it. 

### S3 Access Points
Used for simplifying managing access to S3 buckets/objects instead of 1 bucket w/ 1 bucket policy.
- You create many access points, each with different policies, each with different network access controls, each with their own endpoint address
- Created via either console or cli via the command ```aws s3control create-access-point --name secretdogpics --account-id 123456789010 --bucket dogpics```

### S3 Event Notifications
Older feature, AWS EventBridge is an alternative and supports more types of events and services
- Notifications generated when events occur in a bucket, which cna be delievered to SNS, SQS and Lambda Functions. 
- Tracks events like object Created, deleted, restored, or replicated. 
- You can restrict access to S3 access points to only allow traffic from specific VPCs. 


### S3 Encryption at Rest
Encryption at rest is mandatory in S3, whether via SSE or CSE.
- S3 Server Side Encryption (SSE) is where the S3 endpoint/service encrypts the data as it is being stored at rest. 
- Client Side Encryption (CSE) is where the user encrypts the data before it is uploaded to S3.
  
### S3 Server Side Encryption
There are three options for S3 Server Side Encryion (SSE), each define how much trust you provide the S3 service. 
- Server-Side Encryption w/ Customer-Provided Keys (SSE-C) - Uses keys provided and managed by the customer
- Server-Side Encryption w/ Amazon S3-Managed Keys (SSE-S3) - This is the defualt that will be enabled. Remember encryption at rest is mandatory in S3.
  - S3 Creates, Manages, and Rotates the key. You have no control of the key, and trust that the S3 service and AWS will effectively and securely discard of key data.
- Server-Side Encryption w/ AWS KMS-Managed Keys (SSE-KMS)
  - You can use a KMS managed or CMK managed key for ultimate flexability. The KMS key will be used to create the Data Encryption Key (DEK) by S3. Therefore KMS will not store the DEK and S3 will not hold the KMS/CMK key.
  - Using KMS encryption prevents S3 administrators for decrypting the data inside of every bucket. Where with SSE-S3 and S3 admin would have all S3 permissions including decryption.
  - Can become costly for lots of objects in a bucket due to the excessive API calls to the KMS service


### Bucket Keys
- CloudTrail will show the key related events as from the S3 service, not KMS.
- Works with replication if you were to copy an encrypted object
- If replicating plaintext to a bucket using bucket ketys, the object is iencrypted at the desitination side
