# AWS Control Tower

Allows for the quick and easy setup multi-account enviroments. Think of control tower as the next evelution of AWS Organizations. Control Tower orchestrates other AWS services to provide this function (Organizations, IAM Identity Center, CloudFormation, Config, and more.)

AWS Control Tower is broken up into 4 sections of tools, **Landing Zone**, **Guard Rails**, **Account Factory**, and the **Dashboard**. 

## Landing Zone 
Setup a multi-account enviornment using AWS Organizations and AWS SSO. 

- AWS Organizations: Proides management capabilities for mutliple AWS accounts from a managememnet account with SCPs.
  - **Will by default create two OUs.** 1st is Foundational OU which is for *Security*, the 2nd is Custom OU, which is for *Sandbox*
  - Foundational OU: Contains *Audit Account* & *Log Archive Account*. Seperating access to audit & logging with an isolated read-only account.
    - Log Archive Account: Logs from **AWS Config** & **CloudTrail**
    - Audit Account: Logs from SNS & CloudWatch 

- AWS SSO: Single-Sign-On access for federated IDs from other identity providers or internal AWS IDs.

## Guard Rails: 
Detect/Mandate rules/standards across all accounts with AWS Config, which prevent drifiting away from standards, or blocking drifts in general. 
Guard Rails come in three types (Mandatory, Strongly Recommended, or Elective), and are either preventitive or detective. 
  - Preventitive rails are meant to stop you from doing thing (AWS ORG SCP)
    - They can either be *enforced** for *not enabled*.
    - Ex. Allow or Deny regions allowed to be used. Or Disallow bucket policy changes.
  - Detective rails are meant to be compliance checks (AWS Config Rules)
    - They can be *clear*, *in violation*, or *not enabled*.
    - Ex. A detective check to see if cloudtrail logging is enabled in a S3 bucket, or whether there are any public IPv4 IPs associated to EC2 instances. 

## Account Factory
Provides capaibility to automatically create, modify, and delete template based accounts as needed with **CloudFormation** within Custom OU. 

- Provisioning of the automated accounts can be prefromed either by *Cloud Admins* or *End Users*(with appropriate permissions and account provisioning in the Service Catelog). When these accounts are created, *Guard Rails are automatically added* through Organizational SCPs and CloudFormation templated AWS Config rules.

These automatically provisioned accounts will come with standard Account and Network configuration that align with organization standards. 
  - Account Baseline (Template): Templated AWS accounts with configured defualt policies that align with organizational standards.
  - Network Baseline (Template): Templated VPCs and Network configs from configured defualt policies that align with organizational standards.

Account Factory can be fully integrated with a buisness Software Development Lifecycle (SDLC) using APIs. 

## Dashboard
A single pane of glass for the entire organization
