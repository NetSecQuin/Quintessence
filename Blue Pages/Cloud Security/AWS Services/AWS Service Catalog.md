# AWS Service Catalog

A service catalog is an organized collection of products offered by a team or application, presented as a document or database for end users to 'purchase'. It will include key product information, such as cost, requirements, support information, dependancies, and ownership. 

AWS Service Catalog is a self-service portal for end users to be able to launch *predefined products* (created by admins). It is a region based service, so it must deployed in each region that end-users need to use it. It works through the following steps:


1.) Admins define products and portfolios using CloudFormation templates and Service Catalog configuration. 

2.) The Portofolio/products are made available in a chosen region for end-users to review and launch a products into the region (if they have permissions). 

3.) The Service catelog will the launch the infrastructure using the defined CloudFormation Templates. This allows for end-users to launch infrastructure, without needing infrastructure level permissions, just launch permissions. 

An example could be a Service Catelog product that launches a low cost EC2 instance in us-east-1 in a Sandbox AWS account. Using CloudFormation, the low cost instance is created in a specific region, is isocated in its own VPC, and is configured with compliant logging and auditing enabled. 
