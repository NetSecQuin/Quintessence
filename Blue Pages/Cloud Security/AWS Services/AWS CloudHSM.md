# AWS CloudHSM

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721163600/qQMAeir7CedYq2w0pM_zlw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/ZjRv3m5ZqrjA5_1N_g4K8Gx3Ah5mdgujY.png)

## Summary

AWS CloudHSM provides hardware security modules (HSM) in the AWS Cloud. An HSM is a computing device that processes cryptographic operations and provides secure storage for cryptographic keys. With CloudHSM, you can generate, store, import, export, and manage cryptographic keys, including symmetric keys and asymmetric key pairs.

To learn more, see [AWS CloudHSM](https://aws.amazon.com/cloudhsm/).

## Use

-  Used for for handling cryptographic operations and key management (creating encryption keys, or other cryptographic keys)
-  AWS CloudHSM is your own dedicated and fully controlled HSM, suitable for high-security applications with stringent compliance needs.
  - AWS KMS is an Amazon managed HSM. It is suitable for many types of cryptographic operations and key management with less regulations.
  - AWS CloudHSM or a dedicated HSM may be required for Payment Card informations, Healthcare records, Government, or blockchain usecases.

![](https://d1.awsstatic.com/whiteboard-graphics/products/CloudHSM/product-page-diagram_AWS-CloudHSM_HIW.76ce14889e22d8861a6a9fff0b5664516ed1bddd.png)


## CloudHSM
- True "Single Tenant" HardWare Security Module. It is AWS provisioned by fully customer managed
- AWS does not have access to any of the key data physically. It is interacted with by AWS by Industry standard APIs.
- Fully FIPS 140-2 Level 3 Compliant. (KMS is Level 2 overall, but some level 3 traits)
- KMS can use CloudHSM as a custome key store via a CloudHSM integration with KMS
- Deployed into an AWS managed VPC, and injected into your customer managed VPC by an eni connection. Then An EC2 running the AWS CloudHSM Client software can access the CloudHSM over API.
- No native AWS integration (Ex. no S3 SSE)
- Can be used to offload the ssl/tls processing for webservers
- Enable transparent data encryption (TDS) for Oracle Databases. Protect teh private keys for an Issuing Certificate Authority (CA)
- To ensure the HSM is highly available, it is deployed into 2 Availability Zones 
