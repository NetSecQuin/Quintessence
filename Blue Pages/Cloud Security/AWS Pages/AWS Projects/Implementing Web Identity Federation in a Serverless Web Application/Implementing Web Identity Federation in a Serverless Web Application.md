# Implementing Web Identity Federation in a Serverless Web Application

In this project, we will be creating a web application that allows an end-user to authenticate through an external OAUTH identity provider (Google), and access AWS resources. [Project Credit](https://github.com/acantril/learn-cantrill-io-labs/tree/master/aws-cognito-web-identity-federation/02_LABINSTRUCTIONS)

To do this, we will be:
- 1.) Creating AWS resources (with CloudFormation) for hosting a serverless web interface (with CloudFront), and storing private images (with S3).
- 2.) Creating a Google API project that will allow sign-in and provide a JWT token for authentication.
- 3.) Creating a AWS Cognito Identity Pool, that will accept a Google JWT, and allow the end-user to *assume* an IAM role.
- 4.) Creating index.html and script.js files for our serverless web application, that will create pre-signed URLs, and accept authentication.


#### CloudFormation: Creating AWS resources

We will be using this [CloudFormation Template](https://learn-cantrill-labs.s3.amazonaws.com/aws-cognito-web-identity-federation/WEBIDF.yaml
) to set up the following resources:
  - CloudFront and Route53 are used to create a public endpoint and DNS name
  - Two S3 buckets are created
    - 1st is public and hosts resources for the web application (index.html & scripts.js)
    - 2nd is private and contains cat pictures.



#### Creating a Google API project and Client ID

Start by logging into a Google account at [https://console.developers.google.com/apis/credentials](https://console.developers.google.com/apis/credentials) and create a new project. 

Once a new project has been created, click `Credentials > CONFIGURE CONSENT SCREEN`. There will be options for either internal (Withing your GCP organization) or External (Any Google account). For this usecae we will be picking 'External'. When creating the application we also will need to pick an application type (we can use web application), provide a name, and some contact details for the owner of the application. 

Once the project has been created, we will need to Create Credential/OAUTH Client ID. This will require that we enter a DNS url under Authorized JavaScript origins, which will be the DNS name of our CloudFront application created in the last step.

When you hit 'Create', you will be give a Client ID and a secret key. For this usecase we will only need the clientID, but save both values. 



#### Creating a Cognito Identity Pool

Next we will be creating a Cognito Idenity Pool. This will be so that once an end-user logs in with their Google account, we can take their authenticated JWT and provide the user with an IAM role to assume, giving them access to AWS resources. 

To Create this Identity Pool simply go into `Cognito > Identity Pools > Create New > Google OAUTH`. Then provide a name for the Role that will be created, we will adjust the permissions after in IAM. (Cognito will create two IAM roles. 1. For authenticated users, and 2. for unauthenticated users. Review the AWS Cognito page to understand the difference)

The Roles that AWS Cognito will create, will be configured to ownly allow access if authentication was successful (Through JWT) in Cognito for that user. 

#### Updating Web Application

Last we will need to update the web application resources (index.html & scripts.js) To point to the S3 bucket we created, and to allow authentication from the identity pool's IAM role. 
