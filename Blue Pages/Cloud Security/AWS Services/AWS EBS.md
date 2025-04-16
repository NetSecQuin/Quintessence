# AWS EBS (Elastic Block Storage)

## Summary

Amazon Elastic Block Store (Amazon EBS) is an easy-to-use, scalable, high-performance block-storage service designed for Amazon Elastic Compute Cloud (Amazon EC2).

More inforation at [Amazon EBS](https://aws.amazon.com/ebs/)

## Use

- Virtual storage (HDD/SSD) to attach to EC2 instances. Can be attached, detatched, copied (snapshot), and managed just like physical drives.
- EBS volumes are created within Availability Zones and can not be transfered. 
  - EBS Snapshots can be used to create an EBS volume in a new Availability Zone
  - EBS Snapshots can be copied and pasted into a new region. 
- Snapshots of a running machine are stored as new EBS volumes. The new volume can be attached to a forensic workstation for analysis.
- Deploy and scale your choice of databases, including SAP HANA, Oracle, Microsoft SQL Server, PostgreSQL, MySQL, Cassandra, and MongoDB.


![](https://d1.awsstatic.com/product-marketing/Storage/EBS/Product-Page-Diagram_Amazon-Elastic-Block-Store.5821c6ee4297f3c01cba37e304922451c828fb04.png)

## EBS Encryption
EBS Encryption is encryption of your data at rest. Data is transfered to an EC2 instance, which has a EC2 instance role with KMS:Decrypt permissions, data exsists unencrypted in memory, and is then encrypted by the KMS service as it is stored locally to the volume. 
- Accounts can be set to encrpyt EBS by default, but it is not enabled by default.
  - IF EBS Encryption is enabled by default, it can be configured to use a *default KMS key*, otherwise the end-user/engineer would pick a KMS key to use.
- The KMS key is used to generate a Data Encryption Key (DEK)
  - Each volume uses 1 unique DEK
  - Snapshots & future volumes use the same DEK
  - You can not change a volume to **not** be encrpyted
- OS isnt aware of the encryption, therefore there is no performance loss for using it.
