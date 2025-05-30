# AWS Athena
- Serverless interactive querying service
- Ad-hoc queries on data - pay on data consumed
- Uses Schema-on-read to use a pre-defined log schema to format the data into a table on read. Therefore original data (Ex. S3) is never changed and remains on S3.
- Output can be sent to other AWS Services
- Supports a number of structured, semistructured, and unstructured data types (XML, JSON, CSV, CloudTrail, Apache, VPC Flow, etc.)
- Schema/Tables are defined in advance in a data catalog and allows data to be read into tables as its read by Athena.
- There is no data loading, data manipulation, or transformating required.
- Supports the Glue Data Catelog & Web Server Logs
- Athena Federated Query Connector can allow use of Athena with other data sources (mysql, etc.)
- 
