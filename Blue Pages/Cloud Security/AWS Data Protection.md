# AWS Data Protection

## Protection at rest
Depending on the type of data and compliance requirements, how data at rest is encrypted may be required through either: 

- **Client-Side Encryption**: *You* encrypt the data *before* it is uploaded to AWS.

- **Server-Side Encryption**: *AWS* encrypts the data on your behalf *after* its been uploaded.

## Protection in transit
While data is being uploaded or moved, it also may need to be encrypted in order to protect against interception.

- AWS APIs use TLS for end-to-end encryption
- You can use AWS to generate, deploy, and manage public and private certificates used for TLS encryption in web-based workloads.
- By using IPsec with VPN you can encrypt data in transit to AWS.

## Services

[AWS CloudHSM]() - Dedicated Hardware Security Modules (HSM) for cryptographic key generation and management. (For certain usecases of sensitive data)
[AWS KMS]() - AWS Managed HSM for cryptographic key generation and management (Simple and fits most usecases) 
