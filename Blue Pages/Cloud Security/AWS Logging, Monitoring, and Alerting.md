# AWS Logging, Monitoring, and Alerting

## Logs to Audit

- **S3 Access Logs** - Shows detailed access to resources and data inside of S3 (GET, PUT, DEl) Cloudtrail would show *listbucket*.

- **ELB Access Logs** - Requests to your load balancer with IP address, response, and latency. Pattern recognition and troubleshooting.

- **CloudWatch Logs & Events** - 

- **VPC Flow Logs** - Network activity to and from your network interfaces and subnets inside your VPC. Identify VPC misconfigurations.  

- **CloudTrail Logs** - Shows API activity in your AWS account made through the Console, CLI, SDKs or other Amazon Services.

## Logging and Detection Services

#### [CloudTrail]() - Every action in an AWS account is an API call. All AWS API calls are documented in CloudTrail. 

#### [CloudWatch]() - Instances can have CloudWatch agents installed. Agents report to CloudWatch. CloudWatch logs > Events & Alarms. 

#### [AWS Guard Duty](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Guard%20Duty.md) - AWS built in threat detection through intel intel feeds, suspicious anomalie detection, and threat based activity. 

#### [AWS Security Hub](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Security%20Hub.md) - Centralized view for aggregating, organizing, and taking action on security alerts from multiple AWS Services 

#### [AWS Trusted Advisor](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Trusted%20Advisor.md) - Identify places to lower costs. Align with security standards. Improve resiliance and preformance of resources

#### [AWS VPC Flow Logs](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20VPC%20Flow%20Logs.md) - Track network activity to your instances inside a VPC. Troubleshoot connectivity and identify network threats. 

#### [AWS Config](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Config.md) - View current & historic configuration changes to troubleshoot outages or analyze security incidents. 
