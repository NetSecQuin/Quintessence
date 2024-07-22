# AWS Config

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721149200/GkyF8Mg8z4_WVdL503GbNw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/YmAussmY29QpVb9V_NL5PHtmHLHdSqyG2.png)

## Summary

AWS Config is a continuous monitoring and assessment service that can help you detect non-compliance configurations in near real time. You can view the current and historic configurations of a resource and use this information to troubleshoot outages and conduct security attack analyses. AWS Config is a regional service, but can support cross-region and account aggregation.


AWS Config has two main jobs:

1.) Record Configration changes over time on resources. (Tracks pre-change and post changes for auditing changes against compliance.)
  - It **Does not prevent changes from happening**. BUT can be used to auto-remediate changes. 
  - Changes can generate SNS notification and near-realtime events via **EventBridge** & **Lambda**

2.) Evaluating configuration against predefined config rules in order to identify *compliant* or *Non-Compliant* with **Config Rules**
  - Are either AWS Managed or Custom (using lambda).
  - AWS Config can send events to Eventbridge. Eventbridge can use Lambda for auto-fixing Account level changes, and SSM for host level auto-fixing.


To learn more, see [AWS Config](https://aws.amazon.com/config/).

## Use

- View current & historic configuration changes to troubleshoot outages or analyze security incidents.
- Audit and evaluate compliance of your resource configurations with your organization’s policies on a continual basis.
- Monitor and assses resource configuration changes in order to keep a record of change management and identify unapproved changes.
  - Compliance-as-Code or Codify your compliance requirements

![](https://d1.awsstatic.com/Product-Page-Diagram_AWS-Config_Preventative-Proactive-Rules%402x.903337bdfa605eef1031213a125b9a8f94b39903.png)
