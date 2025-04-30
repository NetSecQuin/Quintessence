# AWS Inspector
Scans EC2 instances and the Instance Operating Systems (or containers) for vulnerabilities and deviations against best practices
- Runs an asssesment of varying legnths for deviations. Legnth can be 15min, 1hr, 8/12 hours, or 1 day.
- Provides a report of findings ordered by priority
- Network Assements (agentless)
- Network **and host** assessment (Agent-based)
- Rules Packages determine what is checked
- Network Reachability can idnetify reachablility end to end (EC2, ALB, DX, ELB, ENI, IGW, ACLs, RTs, SGs, Subnets, VPCs, VGWs, VPC Perring) **Without an agent**
  - Details like (reconginzedPortWithListener, recognisedPortNoAgent, UnrecocongizedPortWithListener)
- Agent based asssements can preform package anaylsis for CVEs, can compare against CIS benchmarks, and check for security best practices provided by Amazon Inspector. 

## Summary

Amazon Inspector is an automated security assessment service that helps improve the security and compliance of applications deployed on AWS. It continuously scans and assesses applications for vulnerabilities or deviations from best practices. All findings are aggregated in the Amazon Inspector console, routed to AWS Security Hub, and pushed through Amazon EventBridge to automate workflows, such as ticketing.  

To learn more, see [Amazon Inspector](https://aws.amazon.com/inspector/).

## Use

- Continuous automated vulnerability scanning of EC2 Instances,AWS ECR Container Images , and Lambda functions
- Seemelessly integrates in the the CI/CD pipeline flow to detect vulnerabilities in near-real time. 

![](https://d1.awsstatic.com/products/inspector/Amazon-Inspector_HIW%402x.c26d455cb7e4e947c5cb2f9a5e0ab0238a445227.png)

