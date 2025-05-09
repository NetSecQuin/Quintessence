# AWS Systems Manager (SSM)

## Summary

AWS Systems Manager has capabilities that help you automate management tasks. Such tasks include collecting system inventory, applying operating system patches, maintaining up-to-date antivirus definitions, and configuring operating systems and applications at scale. Systems Manager helps keep your systems compliant with your defined configuration policies.

## Features

- Collect information about your instances and installed applications, to help understand your configurations and applications
- Automate common and repetitive tasks for IT and Management purposes.
- Deploy software patches automatically across lots of EC2 instances and on-prem servers
- Centralized storage of parameters like secrets, credentials, configurations, and text for reuse and isolation from hardcoding artifacts.
- *run command*, automate tasks across numerous hosts without logging into each one. Install software, make registry edits, etc. at scale.
- Use *Session Manager* to remotely connect to instances through the browser via SSM agent without opening ports, bastian hosts, or SSH keys. 

For the complete list of features, see [AWS Systems Manager Features](https://aws.amazon.com/systems-manager/features/).

## AWS Secrets Manager
Shares some functionality with parmeter store but designed for secrets (passwords, api keys, etc.)
- Usable via Console, CLI, API, or SDKs (integration
- Supports automatic rotation using lambda functions, which is one of the primary differences bettween a hidden secret in parameter store 
- Direclty integrates with some other AWS Prodcutions (Ex. RDS)
- Integrates with IAM so you can set permissions of access by role based access control
