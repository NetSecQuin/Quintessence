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

[AWS CloudHSM](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20CloudHSM.md) - Dedicated Hardware Security Modules (HSM) for cryptographic key generation and management. (For certain usecases of sensitive data)

[AWS KMS](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20KMS.md) - AWS Managed HSM for cryptographic key generation and management (Simple and fits most usecases) 

[AWS S3 Glacier](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20S3%20Glacier.md) Store data that does not need frequent access at low costs. Use Glacier Vault Lock to ensure tamper proof storage. 

[AWS Certificate Manager](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Certificate%20Manager.md) - Create and manage SSL/TLS certificates for your public or private webpages and applications.

[AWS Macie](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Macie.md) - Scan S3 for sensitve data with ML. Identify unencrypted data and insecure bucket policies. 


