# AWS Certificate Manager

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721163600/qQMAeir7CedYq2w0pM_zlw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/pgnFFbjxAe0z7Ldz_UjclUZZ0T9PkTfO4.png)

## Summary

AWS Certificate Manager (ACM) handles the complexity of creating and managing public SSL/TLS certificates for your AWS based websites and applications. ACM can also be used to issue private SSL/TLS X.509 certificates that identify users, computers, applications, services, servers, and other devices internally.


To learn more, see [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/).

## Use

- ACM allows you to create SSL/TLS certificates for private and public applications or websites. 
- The SSL/TLS certificate is used for encrypteing the data in-transit
- The certificate proves/validates identity and is signed by a *trusted authority* or a certificate authority to provide a chain of trust.
  - SSL/TLS certificates signed by Private Certificate Authorities will need clients to configure their applications to trust your Private CA.
  - SSL/TLS certificates signed by Public Certificate Authorities have partnerships with Browsers to automatically approve a set of known Certificate Authorities.
- ACM can genreate or import certificates
  - If Generated: it can automatically renew it, but if imporated you are responsible for renewal.
- Supported AWS Services ONLY (CloudFront and ALBs) - EC2 IS NOT SUPPORTED, this is due to EC2s having root level access and can manipulate certificates, where ACM wants to be the authority. 
- ACM is a regional services. Certificates cannot leave the region they are generated or imported in.
- To use a certificate with an ALB in us-west-2, you need a certificate in ACM in us-west-2.
  - NOTE: Global Services such as CloudFront operate as through within us-east-1
- S3 does not use ACM for its certicates. 

![](https://d1.awsstatic.com/product-page-diagram_AWS-Certificate%20Manager%402x.7b2b51b8a698ccac2bbe4d1d904a8ef501dcdda4.png)

