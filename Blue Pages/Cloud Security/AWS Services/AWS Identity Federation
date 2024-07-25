# AWS Identity Federation
Identity Federation is a process where external identies are used instead of services maintaining their own identies. This allows for a better experience for customers and less admin overhead for services. Examples would include end-users using their external Identities from Facebook or Google as an identity for your service. 

Three main parts in AWS ID Federation
- 1.) Customers who use the application
- 2.) Application itself (Service Provider (SP))
- 3.) Identity Provider (IdP)

Identity providers can use enterprise standards such as SAML, or Web Identity Providers such as Google, Facebook, or Twitter. 

This works by an applicaiton (The service provider), having a login form with an Identity Provider option (Ex. Sign in with Google). The this login page will be hosted by the Identity Provider (Google), and handle the authorization and validation of the credentials. The IdP will then provide a authorization token which is provided back to the application/service provider. The SP uses this token to authenticate the user under the IdP's identity, preventing the SP from needing the actual credentials. 

When to use Identity Federation:
- You want to reduce the number of logins for customers to manage.
- Reduce barrier to entry (customers dont need to go through the process to create an account again)
- Logins are managed externally. Security of those credentials is the IdPs responsibility, which they already were responsible for. 
  - This could be considered more secure, as it means that there isnt a new place where the credentials are stored (another risk)
- Less admin overhead (SP side)
- Bypass the 5,000 IAM user AWS limit
- Operate with exsisting signle source of truth enterprise ID stores (Enterprise only needs to manage one primary set of credentials)
