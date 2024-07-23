# AWS STS (Security Token Service)

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721149200/GkyF8Mg8z4_WVdL503GbNw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/ROY577DXHEP3JaNN_PX6O2QELV9-9Iobp.png)

## Summary

The AWS Security Token Service (STS) is a web service that gives you the ability to request temporary, limited-privilege credentials for IAM users who are taking on a different role, or for users who are being federated. A scenario in which someone, or something, needs access to your account to perform a specific task that is not done on a daily basis would be a great candidate for temporary credentials.

For more information, see the [AWS Security Token Service API Reference](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html).

## Use

- Temporary credentials for an IAM user that needs permisions of a differnt role for a short time. Temporary elevated credentials for a specific task.

# STS

Generates temporary credentials whenever a role is used (sts:AssumeRole) to access AWS resources. STS is requested by an Idenity (AWS or External). 

Similar to Access Keys, except they expire and do not belong to the identity. 

The Role **Trust Policy** defines who can assume a specific role. Conceptually this is a wall around the IAM Role. The sts:AssumeRole* call must be made by an exsisting identity (either AWS or external(federation)).

If an *identity* is not allowed to assume a role based on the trust policy, *AssumeRole* fails. 
If the trust policy for a role allows the *idenitity* to use it, the identities **sts:AssumeRole*** call will succeeed. Then STS will read the **Permissions Policy**, which is attached to the role. STS then uses the permissions policy to generate temporary credentials that allow access until *expiration*. The generate STS information will include:
- AccessKeyId: Unique ID of the credentials
- Expiration: Data and time of credential expiration
- SecretAccessKey: Used to sign requests
- SessionToken: Unique token which must be passed with all requests

When the temporary credentials expire, another sts:AssumeRole* call will be required in order to get new temporary credentials. 
