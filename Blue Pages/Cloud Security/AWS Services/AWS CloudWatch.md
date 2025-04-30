# CloudWatch
CloudWatch as a service is an ingestion, Storage, and Managemenet of Metrics.
- Public Service [regional] - it has public space endpoints
- AWS Service Integration or Agent Integration Based
 - Integrates with AWS Services, but only for externally visible metric data only
 - Agent integration will collect on compute information for richer metrics.
 - On-Prem Integration via Agent/API (custom metrics)
 - Application Integration via API/Agent (custom metrics)
- View datat via UI, consolce, API, dashboards or anomaly detections
- CloudWatch Alarms can be configured to react to metrics and notify or preform actions via SNS notification or EventBridge Events.



### CloudWatch - Data

Terms:
- Namespace = container for metrics (ex. AWS/EC2 & AWS/Lambda)
- Datapoint = Timestamp, value, and a unit of measure (optional)
- Metric = Time ordered set of datapoints (Ex. CPUUtilization, NetworkIn, DiskWriteBytes - (EC2))
- Dimension = Name/Value pair/ (Ex. MetricName=CPUUtilization, Name=InstanceID, Value=i-111111111111)
- Resolution = How frequently a datapoint is collected. (Default/Standard is 60s granularity, At a higher cost you can get up to 1s.)
  - Resolutiion Retention = how long the after the data is ingested will it take to be retained
    - below 60s retained for 3hr, 1min retained for 15 days, 5min retained for 63 days, 1hr for retained for 455 days
    - As data ages its aggragated and stored for longer with less resolution (it takes longer to retrieve the data when queried)
- Statistic = aggregation over a period (ex. Min, Max, Sum, Average
- Percentile Ex. p95 & P97.5

Every metric has a MetricName (ex. CPUUtilization) and a NameSpace (AWS/EC2)


#### CloudWatch Alarms
Alarms watch a metric over a specified period of time
- An alarm will either be in a **OK** State or an **ALARM** State
  - It is driven by the value of a mertic vs a threshold over a time period.
- An alarm can be used to trigger one or more actions


### CloudWatch Logs - Ingestion
Public service for storing, monitoring, or accessing logging data .
- It can log AWS, On-Premsis, IOT or any application (with the help of the CloudWatch Agent (CWAgent)
- Can ingest logs from VPC Flow, CloudTrail, Elastic beanstalk, ECS Container Logs, API Gateway logs, Lambda execution logs, and Route53 Logs. 
- Log Streams = A stream of data from a single source
- Log Group = A collection of log streams
  - WThe log group is where you define retention, permissions, and encrypion


### CloudWatch Logs - Subscriptions
Subscriptions can be used to configure real-time delievery of log data from a log group. 
- S3 Export is not real time export, it takes around 12 hours. **(Uses CreateExportTask which does not use Subscription)**
- You can use Kinesis Data Firehose to get **near real-time** delivery.
- IF you need **real-time** deliver, you can use a subscription filter to forward to traffic to a Lambda function which can forward the traffic to S3 or elasticsearch in real-time.

## CloudWatch Events and EventBridge
Configure rules for detecting events within CloudWatch logs
- EventBridge is the service replacing Cloudwatch events, although CloudWatch events are still available.
- A default Event bus for the account, in CloudWatch Events this is the only bus (implicit), EventBridge can have additional Event Busses
- Rules Match Incoming events (or Schedules// like cron) and routes the event to 1 or more targets (Ex. lambda function)
