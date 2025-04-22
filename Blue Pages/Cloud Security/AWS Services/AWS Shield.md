# AWS Shield

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721239200/ZEcL0bTnPYhQOsOBxow55Q/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/HvE48M1NNFyB9osA_KOKWasYjvKThhiUG.png)

## Summary

AWS Shield is a managed DDoS protection service that safeguards web applications that run on AWS. AWS Shield provides always-on detection and automatic inline mitigations that minimize application downtime and latency.

To learn more, see [AWS Shield](https://aws.amazon.com/shield/).

## Use

- Automatically blocks layer 3/Network DDos attacks (Ping Floods and ICMP related attacks like fragments and smurf attacks) - Saturation based attacks
- Automatically blocks some layer 4/Transport DDoS attacks (TCP floods/SYN&ACK, UDP floods) - leave em hanging attacks 
- Automated DDoS identification and blocking (opt-in) through machine learning. 30 day baseline, identifies anomalies outside of baseline. Will suggest or implement WAF rules to block attack based on identified signatures. WAF rule will be removed after attack ends. (SHIELD ADVANCED ONLY) - 

![](https://d1.awsstatic.com/AWS%20Shield%402x.1d111b296bfd0dd864664b682217bc7610453808.png)

### AWS Shield
- Comes in Standard (FREE) & Advanced ($$$) versions.
- Shield Standard
  - Protection at the permiter. (region/VPC or the AWS edge)
  - Common network (Layer 3) or transport (Layer4) attacks
  - Best protection if you are using Route53, CloudFront, AWS Global Accelerator
- Shield Advanced
  - $3,000 per month, per AWS Organization. 1 year comitment required. Also a charge for data outbound.
  - Protects CloudFormation, Route53, Global Accellerator, anything assocaited with EIPs (ex. Ec2), ALBs, CLBs, and NLBs
  - Not Automatic. Must be explicatly enabled in Shield Advanced or AWS firewall Manager Shield Advance policy.
  - Cost protection (Ex. EC2 scaling) for unmitigated attacks
  - Proactive engagement & AWS Shield Response Team (SRT) included with subscription
  - WAF intergation - includeds basic AWS WAF fees for Web ACLS, rules, and web requests
  - Application Layer (layer 7) DDOS protection (uses WAF)
  - Real time visibility of DDOS events and attacks
  - Health-based detection : applcioation specifci health checks used by proactive engagement team
  - protection groups, which allow you to group applications together shortening overhead. 
