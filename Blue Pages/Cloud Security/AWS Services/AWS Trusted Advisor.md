# AWS Trusted Advisor

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721149200/GkyF8Mg8z4_WVdL503GbNw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/eW2PVbi_wVEFfuGb_vvg59k6c7JxfAVDl.png)

## Summary

AWS Trusted Advisor is a service that draws upon best practices and inspects your AWS environment, making recommendations for saving money, improving system performance, or closing security gaps. You can configure Trusted Advisor notifications to receive weekly emails about any changes. You can also subscribe to Business-level and Enterprise-level support to access the full suite of Trusted Advisor best-practice checks.

To learn more, see [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/).


- No agents to install
- Provides a number of checks in: **Cost Optomization**, **Preformances**, **Security**, **Fault Tolerance**, and **Service Limits**


### 7 Core **Free** checks
  - S3 Bucket Permissions
  - Security Groups with Unresticted access (Ports with 0.0.0.0/0)
  - IAM Use: Do you have at least 1 IAM user (not using the root AWS account)
  - MFA on Root Account (Does the root account have MFA enabled)
  - EBS Public Snapshots (Checks the permissions on EBS snapshots to identify any that are publically exposed)
  - RDS Public Snapshots (Checks the permissions on RDS snapshots to identify any that are publically exposed)
  - 50 Service Limit Check (Checks the 50 most common service limits and notifies you if you are over 80%)
 
### Buisness and Enterprise Support
  - Comes with the 7 **Free** core checks
  - 115 Further checks (14 cost, 17 security, 24 fault tolerant, 10 preformance, and 50 service limit.)
  - **AWS Support API Access** (Programatic access to trusted advisor checks and automate when checks are done & refereshed. Can also check status of checks. Open support cases and track and manage open cases.
  - **CloudWatch Integration**: Allows you to take automated actions on Trusted Advisor Findings. 
 
  You may need to identify places on the exam where trusted advisor would be used to preform a check, but then highlight where the buisness/enterprise plan would be needed in order to automate notification, support case generation, or remedition of an identified issue. 


## Use

- Identify places to save on costs (unused resources, under-utalized resources?, etc.)
- Assess your AWS environment against security standards and best practices.
- Improve preformance by analyzing usage and configuration of AWS resources to improve speed and responsiveness.
- Improve resiliance by identifying redundancy shortfalls and overused resources.
- Track service limits and identify when activity nears or exceeds service thresholds. 
