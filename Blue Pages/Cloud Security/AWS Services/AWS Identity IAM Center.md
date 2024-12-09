# AWS Identity IAM Center

## Summary

AWS IAM Identity Center is a cloud single sign-on (SSO) service that provides the central management of SSO access to multiple AWS accounts and business applications. Users can sign in to a user portal with their existing corporate credentials and access all of their assigned accounts and applications from one place. IAM Identity Center includes built-in SAML integrations to many business applications. It might be integrated with Microsoft Active Directory, which means your employees can sign in to your user portal using their corporate Active Directory credentials.

For more information about SSO, see the AWS IAM Identity Center User Guide(opens in a new tab).

## Use

Configuring SSO or SAML from your organizations LDAP (Active Directory) with AWS IAM. 

## AWS Signle Sign-on (SSO) 

Manage SSO Access for AWS Accounts and External Applications. Perfered method by AWS vs tradtional 'workplace' identity federation.

AWS SSO integrates with a range of workplace identity sources from built-in AWS identites to self-managed on-prem active directory confirgurations. It can handle SSO and permissions for **AWS accounts & external applications**. 

Flexible Identity Source: You create an identity store, which will work for a variety of IdP as apposed to SAML Federation, which had to be configured individually.

Works for:
- AWS SSO - Built-in Identity Store
- AWS Managed Microsoft AD (Through AWS Directory Service) 
- On-Premisis Microsoft AD (Two way trust or AD connector)
- External Identity Provider - SAML2.0

How it works:
- Connect a identity source (Active Directory) or create user(s) in AWS SSO.
- You are given a SSO URL, that you can customize to be named after your organization. URL format is "company.awsapps.com"
- Create a group, which is a collection of users
- Select the AWS accounts you want to be in scope for the group and to be selected permission set.
- Attach a prebuilt permission set, or create your own to the group.
- Users login via the URL, and are presented with the AWS accounts available and the assoicated Group name
