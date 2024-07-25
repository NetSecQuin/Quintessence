# AWS Cognito

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721149200/GkyF8Mg8z4_WVdL503GbNw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/YZvKa7vr7fCGZt1s_egCNNphFBzbbCcAE.png)
## Summary

With Amazon Cognito, you can add user sign-up, sign-in, and access controls to your web and mobile apps. You can define roles and map users to different roles so your app can access only the resources that are authorized for each user. User sign-in can be done either by a third-party identity provider, or directly through Amazon Cognito.

To learn more, see [Amazon Cognito](https://aws.amazon.com/cognito/).

An Amazon Cognito user pool is a user directory that manages the overhead of handling the tokens that are returned from social sign-in providers, such as Facebook, Google, and Amazon, and enterprise identity providers through SAML 2.0. After a successful user pool sign-in, your web or mobile app will receive user pool tokens from Amazon Cognito. These tokens can then be used to retrieve AWS credentials through Amazon Cognito identity pools. These credentials allow your app to access other AWS services and you don’t have to embed long-term AWS credentials in your app.

## Use 

- Used for customers of your web/mobile application to create accounts that can access credentials for AWS resources via AWS Cognito Identity pools.
- Users of your website sign in, and request data from an Amazon hosted database. Cognito provides AWS credentials that allow website user to make query.
- Get past 5,000 IAM user limit.

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721149200/GkyF8Mg8z4_WVdL503GbNw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/YJiik1Nj7Sh097Oh_wm8pANm6aAzP_Zqk.jpg)


## Amazon Cognito

Provides authentication, authorization, and use managment for web/mobile apps. 

#### User Pools
Sign in and get a JSON Web Token (JWT). **Most AWS services can not use JWT for authentication.** Used for managing end-user identities.
- Can be used for authentication with applications and certain AWS services like API Gateway.
- **Do not grant access to AWS Resources.**
- Their job is to control sign-up and sign in services
- customisable web UI to sign in users
- Check for compromised credentials and help configure MFA
- Allow sign in for built in users

Flow of User Pools
- 1.) User visits web/mobile application that servers login through IdP (google, facebook, SAML, etc.)
- 2.) IdP approves authentication, Cognito provides a JWT as authentication for the account as a User Pool user.
  - 2a.) JWT can be used to access self-managed server based resources (Things inside the web/mobile application server)
  - 2b.) JWT can be used to grant access to APIs via **API Gateway** and **Legacy Lambda Custom Authorizers** 

#### Identity Pools
Allow you to offer access to **Temporary AWS Credentials**. Work by assuming a role. Used for providing temporary credentials to an identity.
- Unathenticated Identities: Allow access to unauthenticated/guest users. (Ex. App that shows high scores, without user needing to sign up)
- Federation Identites: Swap and external Identity for temporary AWS credentials in order to access an AWS resource. (Google, SAML, User Pools, etc.)

Flow of Identity Pools
- 1.) User visits web/mobile application that servers login through IdP (google, facebook, SAML, etc.)
- 2.) External IdP approves authentication, and provides a token
- 3.) Cognito Identity Pool supports logins from the external IdP. It is configured with Authenticated and Unauthenticated IAM Roles that Cognito can assume in order to recieve *temporary* AWS credentials.
- 4.) Application recieves these temporary credentials for use with AWS Services and Resources.

#### Combining User Pools and Identity Pools

- 1.) The External IdP is used to sign in to a User Pool user through the use of the provided JWT. (End Result: All external IdP users sign in to become a User Pool user (singular ID provider for Identity pools))
- 2.)  Application passes this User Pool token (JWT) to an Identity Pool. (This removes admin overhead since Identity Pool just needs to work with User Pool)
- 3.) Idenity Pool uses IAM roles to connect to AWS resources. 


