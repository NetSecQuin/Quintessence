# AWS Route 53
![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721239200/ZEcL0bTnPYhQOsOBxow55Q/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/RvdLDug5R4sjTSYM_XmzS7wcYHTJh0eDH.png)


## Summary

Amazon Route 53 is a highly available and scalable DNS service that can be used to direct traffic to your web application. It includes many advanced features like traffic flow, latency-based routing, weighted round-robin, Geo DNS, health checks, and monitoring. You can use these features to improve the performance of your web application and to avoid site outages. Route 53 is hosted at numerous AWS edge locations, creating a global surface area capable of absorbing large amounts of DDoS traffic.

To learn more, see [Amazon Route 53](https://aws.amazon.com/route53/).

## Use

- Scalable DNS service for routing traffic to your web applications.
- Offers routing features like latency-based, Geo DNS, or weighted round-robin to distribute load to the highest availibility servers.
- Preforms health checks and monitoring to identify outages and prevent end-users from experiencing them with routing.


![](https://d1.awsstatic.com/Route53/product-page-diagram_Amazon-Route-53_HIW%402x.4c2af00405a0825f83fca113352b480b19d9210e.png)


### VPC DNS // Route53 Resolver
- The .2 is reserved in every subnet for DNS (Ex. 10.16.0.**2**).
- Provides Route53 Public & Associated Private Zones
- Only accessible from within a VPC
- Had drawbacks with hybrid environments due to on-prem private networks not being able to resolve DNS hostnames of resources within the AWS VPC because Route53 Resolver is only accessible from within the VPC. This led to the creation of *Route53 Endpoints*
  - Before Route53 Endpoints, best practice was to use an EC2 instance running within the VPC acting as an intermidiary DNS forwarder via DHCP. Requests arrive and are forwarded to the Route53 Resolver or to on-prem DNS servers if configured. 

### Route53 Endpoints
Route 53 Endpoints are:
- VPC Interfaces (ENIs) - Accessible over VPN or Direct connect instead of EC2 intermidiary
- Inbound = On-prem can forward to the Route53 Resolver
- Outbound- Conditional Forwards from the Route53 Resolver to On-Prem network
  - Rules control which request are forwarded
  
