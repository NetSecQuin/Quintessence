# AWS Simple Notification Service (SNS)
SNS is used across AWS Services for notifcation
- Public AWS Se3rvice - network connectivity with public endpoint
- Coordinates the sending and delivery of messages
- Message are less than or equal to 256KB payloads (small messages)
- SNS Topics are the base entity of SNS - and where you configure permissions
- A publisher sends messages to a topic, topics have **subscribers** which recieve messages
  -Messages can be sent via HTTPS, Email(JSON), SWS, Mobile Push, SMS Messages, & Lambda
  - Offeres Delivers Status for HTTP, Lambda, and SQS.
  - Offers Delivery Retires
- Highly availabe and Scalable (region)
- Capable of Server Side Encryption (SSE)
- Can be used cross account via a **Topic Policy** (Like a resource policy for SNS topics)
- 
