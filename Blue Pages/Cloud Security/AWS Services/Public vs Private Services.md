# Public vs Private Services
Whether an AWS service is public or private from a **networking perspective**

- When looking at how AWS and its services interact with the "Public Internet", there are 2 zones seperate from the "Public Internet".
  - AWS Public Zone
    - AWS resources are accessible from the public internet by default. They are not on the public internet.
    - Ex. S3 buckets have a publicly accessible address, but are restricted by resource policies by default. 
  - AWS Private Zone
    - AWS resources are not accessible publically and are isolated within VPCs unless configured otherwise.
