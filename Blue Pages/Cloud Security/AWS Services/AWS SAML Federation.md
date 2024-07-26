# AWS SAML Federation (Outdated Service/Old Way of Doing Things)

The process of using an identity from another identity provider in order to access an AWS resource. However in AWS, this can not be direct as AWS services can only be accessed through the use of AWS credentials. 

- Exchanging external Identities with AWS credentials
- Enterprise Identity provider needs to be SAML 2.0 Compatible (**not** Google, Facebook, etc. Authentication)
-Uses IAM Roles & AWS Temporary Credentials (12 hour validity)


How this works for API Access
- Appliciation initiates/requests access via IdP
- The IAM instance is configured to *trust* the external Identity Provider (Ex. ADFS)
- The IdP authenticates the request and identitifes which *roles* are avaialbe for the applicaition for that identity
  - The identity may be configured to have access to 1 or more roles
  - The application will be provided this list of available roles, and pick which one it would like to use.
- The IdP then provides the application with a SAML Assertion (token saying the idenitity has authenticated and has the role)
- The Application then communicates with AWS, passes the SAML assertion to STS (sts:AssumeRoleWithSAML), which returns temporary credentials.

How this works for Console Access
- The user browses to the IDP portal (Ex. https://companyadfs/adfs/ls/ldpinitiatedSignOn.apsx
- IdP authenticates requet and identitifes which *roles* are availabel for the user.
- User selects a role to use
- IdP provides a SAML assertion
- The login console sends assertion to a sign-in URL
- AWS SAML endpoint sends it to STS to assume the role and generate temporary credentials.
- **AWS SAML Creats a console sign-in URL for the console with the credentials and redirects the user to the page.** - the primary difference
