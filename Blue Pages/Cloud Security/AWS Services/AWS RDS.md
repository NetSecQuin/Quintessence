# AWS RDS

## RDS Security
- SSL/TlS (in transit) is available for RDS and can be configured to be mandatory
- RDS supports EBS volume encryption - via KMS and EBS encryption and handled by the host/EBS
- AWS or Customer managed CMK generaets data keys. Data Keys are used for encryption of storage, logs, snapshots and replicas.
- Encrypytion can not be removed
- RDS MSSQL and RDS Oracle Support Transpartent Data Encryption (TDE) which is encryption handled within the DB engine, as apposed to by the EBS/KMS service.
- RDS Oracle supports integration with CloudHSM

### IAM Authenitcation
- RDS local DB account configured to use AWS Authentication Token. This account controls the authorization within the database (permissions/access level)
- Auhtorization is still handled internally within the DB, IAM authenticaiton can be used for Authentication only.
- Uses a token with a 15min validity which can be used in place of a DB user password
