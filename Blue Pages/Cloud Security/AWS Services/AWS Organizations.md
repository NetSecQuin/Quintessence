# AWS Organizations

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721149200/GkyF8Mg8z4_WVdL503GbNw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/IT8qs9OpLqKemLQo_Ujpjq99HbaJwB8WF.jpg)
## Summary

With AWS Organizations, you can centrally manage and enforce policies for multiple AWS accounts. This service allows grouping accounts into organizational units (OUs) and using service control policies to centrally control AWS services across multiple AWS accounts. With Organizations, you can automate the creation of new accounts through APIs. You can also streamline billing by setting up a single payment method for all the accounts in your organization through consolidated billing. Organizations is available to all AWS customers at no additional charge.

For more information, see [AWS Organizations](https://aws.amazon.com/organizations/)

## Use 

- Organize multiple AWS accounts at once
- Group accounts into organizational units (OU)
- Automate creation of new accounts through APIs


## Organization

Consists of numerous exsisting *Standard* accounts that become *Management* accounts and *Member* accounts. Each organization can have 1 *Management/Master* account, and all *Standard* accounts that join the organization under the *Management* account become *Member* accounts. 

  - Current *Standard* accounts need to be invited and accept in order to be added to an AWS Organization.
  - AWS Organizations can create new AWS accounts within the Organization will an email address. 

- Organization Root: A container within an AWS Organization, that contains AWS accounts (Member accounts or the Management account. It can also contain other Orgonazational containers or Organizational Units (OU). *Not the AWS root user, which is the root user of each AWS account*

- Considated Billing: Once Standard accounts join an Organization, billing is consolidated and managed by the Management account.
  - This provides benefits to companies through:
    - Lowering overhead managment responsiblities and costs of operating numerous payment sources
    - Certain services get cheaper with the more usage (think bulk buying or usage discounts)
   
## Managing Users, Roles, and Groups within Organizations

Using an AWS Organization changes what is best practice for how you manage users access and permissions. 

- Have a single account that you login too, instead of user accounts in each AWS account.
- Some organizations may use an exsisting seperate Identity provider with Identity Federation
- Some prefer to keep the managemnet account clean (Like your AWS root account would be) and have a secondary account that is dedicated to handle logins.
  - From one central user account, we can use a feature called *Role-Switch*, which allows us assume roles in the other accounts.

#### Adding Members to your Organization
Once you have clicked AWS Organizations > Create Organization, your account will be converted from a *Standard* account to a *Management* account. 

**Creating an Account**

- If you are creating a new AWS account in your organization, the role will automatically be created for you to *Role-Switch* into.
  - Creating a new AWS account an organization is as simple as providing an email address and assume role name. No root password needed. 

**Inviting an Exsisting Account**

- If you are inviting a current AWS account to your organization, the Management account will need a role created to *Role-Switch* into.
   - **This role will be created in the newly joined account**, providing access to the Management account with the **'AdministratorAccess'** policy.  
   - ``` IAM > Roles > Create Role > Trusted Entity type = AWS Account > Another AWS Account = AccountID of Management Account ```
   - You will need to name the role. AWS syntax suggests using **"OrganizationAccountAccessRole"** as the newly created role name.
     
### Assuming a role
Once you have accepted the invitation and created a new role that provides the *Management account* with AdministrativeAccess policy from the newly joined member account, you can switch back to the *Management* account to assume a role.

Click the dropdown where your username is and click ```Switch role```. 

Then enter the AccountID of the newly joined *Member* account, and the name of the newly created Role. Pick a nickname and color for the role, that will make it easier to identify when switching into it. 
 

## Service Control Policies (SCPs)
Service Control Polcies are account permission boundries that limit what an AWS Account (including account root user) can do. 
  - Despite a Account root user have full account control, SCPs limit what an account can do itself.
    - Common SCPs could be to limit regions available in accounts, or limit the size of EC2 instance that can be created in accounts.   


- Management account can not be restricted by service control policies (SCPs)
- Service Control Policies **do not grant any permissions**, they strictly limit permissions/capabilities.
- By default everything is Allowed, through the defualt/primary SCP policy *'FullAWSAccess'*. therefore it is an explicit deny list.
  - If you want SCP to act as an Allow list, you would delete the *'FullAWSAccess'* policy and build Allow policies. (More secure, but more admin overhead and more likely cause issues.)
 
To Enable Service Control Policies (SCP): ```AWS Organizations > Policies > Service Control Policies > Enable```
- This will enable and create the *'FullAWSAccess'* SCP policy.

To Create a new Service Control Policy: ```AWS Organizations > Policies Service Control Policies > Create New > Enter configuration```
- Just like IAM policies, SCP policies opperate in an upside down christmas tree approach. If the first policy statement in a single SCP shows allow all access to everything, and the second statement says to block S3, everything will be accessible except S3.

In order to add an SCP to an OU, click on the OU under AWS Organizations, scroll down to policies, and click attach policy. Remove policies the same way. Keep things tidy by creating policies that encompas the prior permission blocks, and detach repetitive or former SCPs. 
 
### Creating Organizational Units (OUs)
**Note: AWS Organizations are hierachical, which means that nested OUs carry the SCPs of their parent OU.** 

- 1.) In the *Management* Account, go to **AWS Organizations**. 
- 2.) Click the checkbox next to the parent OU you would like to create a new one under. If it is your first OU, this will be 'Root'. 
- 3.) Select: Actions > Organizational Units > Create New. Then give the OU a name. 
- 4.) **Move** and AWS Account into the new OU with:  ``` Actions > AWS Account > Move ``` 


