# AWS CloudHSM

## Summary

AWS CloudHSM provides hardware security modules (HSM) in the AWS Cloud. An HSM is a computing device that processes cryptographic operations and provides secure storage for cryptographic keys. With CloudHSM, you can generate, store, import, export, and manage cryptographic keys, including symmetric keys and asymmetric key pairs.

To learn more, see [AWS CloudHSM](https://aws.amazon.com/cloudhsm/).

## Use

-  Used for for handling cryptographic operations and key management (creating encryption keys, or other cryptographic keys)
-  AWS CloudHSM is your own dedicated and fully controlled HSM, suitable for high-security applications with stringent compliance needs.
  - AWS KMS is an Amazon managed HSM. It is suitable for many types of cryptographic operations and key management with less regulations.
  - AWS CloudHSM or a dedicated HSM may be required for Payment Card informations, Healthcare records, Government, or blockchain usecases.

![](https://d1.awsstatic.com/whiteboard-graphics/products/CloudHSM/product-page-diagram_AWS-CloudHSM_HIW.76ce14889e22d8861a6a9fff0b5664516ed1bddd.png)
