# AWS Guard Duty

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721149200/GkyF8Mg8z4_WVdL503GbNw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/eBdHX-VilVYrHWQR_GI1jJPl0oMzUTj2h.png)

## Summary

Amazon GuardDuty is an intelligent threat-detection service that provides customers with a way to continuously monitor and protect their AWS accounts and workloads. GuardDuty identifies suspected attackers through integrated threat intelligence feeds and uses machine learning (ML) to detect anomalies in account and workload activity. It monitors for activity such as unusual API calls or unauthorized deployments that indicate that a customer’s accounts might have been compromised. It also monitors direct threats, like compromised instances or reconnaissance by attackers.

To learn more, see [Amazon GuardDuty](https://aws.amazon.com/guardduty/).

## Use

- AWS built in threat detection through intel intel feeds, suspicious anomalie detection, and threat based activity.
- Center for out of the box malicious activity identification alerting 

## High level alert types

- Malicous/Suspicious IP communication and access from EC2 instances
- Disabling security measures such as cloudtrail logging or server access logging and exposing resources publically (S3, Network ACLs)
- Signs of backdoors or hidden processes at both an applicaiton level and account level. Lambda functions, C&C/C2 communication, and user creation
- Unusual and overly permissive changes being made to IAM permissions
- Port scans and host fingerprinting (Recon)
- Brute force attempts (SSH, RDP) and Denial of service attacks (DDoS)
- Execution of Malicious or suspicious files, code, or processes.
- Exfiltration of data over to suspicious/malicious destinations (IP), by Unauthorized users (IP), or unusual mediums (DNS)
- Hacking operating system types being spun up in the enviornment (Kali, ParotOS, etc.)
- Priveledge escalation among contarized environments like Docket and Kubernetes (Container escape, role creation/binding, and anomalous IAM user)
