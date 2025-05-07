# AWS CloudTrail

## Summary

AWS CloudTrail records API calls made on your account. This information helps you track changes made to your AWS resources, troubleshoot operational issues, and ensure compliance with internal policies and regulatory standards.

Additional Details on [CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

## Use

- Track activity made inside an AWS Account through API call monitoring.
- Each Activities is called a CloudTrail event
- Enabled by default - no cost for 90 day history, but need to use a custom trail to send to S3 for longer retention
- management events (enabled by default) and Data events (can be enabled).
- CloudTrail is  regional service. A trail can be set to One region or set to all regions. An all region trails is a collection of trails from differnet regions.
- A custom trial can store the logs in S3, which allows you to store for longer than 90 days.
- Organizational trail can be created as a collection of trails from different accounts in an AWS Organization
- Trails are how you configure S3 and CloudWatch Logs.
- IAM, STS, CloudFront => Global Service Events which will require a trail to be enabled. It will log to US-EAST-1
- NOT REALTIME - There is about a 15min delay

#### CloudTrail Log File Integrity
- Used for integrity validation of cloudtrial logs in S3. (How do you know nobody tampered with them?)
- When you enable Log Validation; CloudTrail creats and signs digest files, each for an hour of log delivery. These digest files are stored in the same bucket, but in a differnet folder from the logs. You can then apply different security policies to the folders contianing the digest files.
- Digest files contain a hash of every log file delivered in the last hour. AND contain the hash of the previous digest file.
- CloudTrail signs each digest file with its private key
- You can validate the logs and digest files through CLI  (validate-logs), but not the console UI. 
