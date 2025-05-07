# AWS Glue
- serverless ETL (Extract, Transform & Load) vs datapipeline, which can do ETL but uses servers.
- Moves and transforms data between source and destination
- Craswls data sources and generates the AWS Glue Data Catalog.
  - Data Source: Stores: S3, RDS, JDBC Compatible & DynamoDB
  - Data Source: Streams: Kinesis Data Stream, Apache Kafka
  - Data Targets: S3, RDS, JDBC Databeses
- A data catelog is peristent metadata about data sources in a region
- One catalog per region, per account, and preventative against data silos
