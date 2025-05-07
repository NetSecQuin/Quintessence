# AWS Macie

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721163600/qQMAeir7CedYq2w0pM_zlw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/aYudK0oJ_ugYdDO3_nP76NGEbwMtTwMVL.png)

## Summary

Amazon Macie uses ML to automatically discover, classify, and protect sensitive data in AWS. Macie recognizes sensitive data, such as personally identifiable information (PII) or intellectual property. It provides you with dashboards and alerts that give visibility into how this data is being accessed or moved.


To learn more, see [Amazon Macie](https://aws.amazon.com/macie/).

## Use

- Scan S3 buckets for sensitive data types with the use of machine learning.
- Identify unencrypted sensitve data, vulnerabilities in bucket policies, and visualize it in an interactive data map.
- Discover, Monitor, and protect data sotred in S3 buckets
- Automated discovery of sensitive data types (PII, PCI, etc.)
- Works by using data identifiers
  -  Managed Data Identifiers (Built-in ML/Patterns by AWS)
    - Comprehensive list of data type identifiers
  -  Custom Data Identifiers (Priorietary and regex based)
    - Useful for data patterns that are unique to the company
    - Refiners allow you to go beyond the regex. Keywords, maximum match distance, and ignore words allow you to get more specific.
- Schedule Macie Discovery Jobs to scan S3 buckets on a schedule for data identifirs.
- Integrated with security Hub & finding events to EventBridge to take automated actions
- Centrally Managed by the AWS Organization, or by Invite.
- Policy findings (S3 was switched to unencrypted from encrypted) or sensitive data findings (Credit card number found)
  - Other Policy Findings: Block Public Access Disabled, S3BucketPublic, S3Bucket SharedExternally.

![](https://d1.awsstatic.com/reInvent/reinvent-2022/macie/Product-Page-Diagram_Amazon-Macie.a51550cca0a731ba2e4a26e8463ed5f5a81202e3.png)
