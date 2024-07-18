# AWS Account Creation

AWS accounts act as a container for your enviornment. Access to your resources and services inside an AWS account are contained, and can not be managed from outside of your AWS account. The root user account, created with your email, is the only (unless additional are added) account with complete control over everything in the account, and therefore should be only used to create the account and manage the top level account settings (account deletion and some billing).

**Once you create a new root AWS account. There are a few things that should be done, then all other activity should be handled through an admin level account created with IAM.**

- 1.) Enable Multi-Factor Authentication (MFA) ```Security Credentials > MFA```
- 2.) Allow IAM users & role access to Billing information. ```Account > IAM user and role access to Billing information```
- 3.) Add alternate contacts (IF production/buisness use). ```Account > Alternative Contacts```
- 4.) Turn on PDF Invoices and all alert preferences. ```Account > Billing Preferences```
- 5.) Configure a budget depending on your account usecase. ```Account > Budgets```
- 6.) Create an account alias for your AWS account, making it easier for IAM user logins. ```IAM > AWS Account > Add Alias```

**Then create an a user and provide it will full access. This will be the admin account for all other activity in the future.** 

- Create the user account  ``` IAM > Users > Create User ```
- Attach *AdministratorAccess* policy ```Attach policies directly > AdministratorAccess```
- Sign in through the alias page to the new admin account ```https://alias.signin.aws.amazon.com/console```
- Enable Multi-Factor Authentication (MFA) ```Security Credentials > MFA```
