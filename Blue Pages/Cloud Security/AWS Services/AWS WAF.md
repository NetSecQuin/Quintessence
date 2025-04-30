# AWS WAF

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721239200/ZEcL0bTnPYhQOsOBxow55Q/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/xtAPMEZUN_nXYQL__JmVKkz4bLwQdvZO7.png)
## Summary

AWS WAF helps protect your web applications from common web exploits that could affect application availability, compromise security, or consume excessive resources. AWS WAF gives you control over which traffic to allow or block by defining customizable web security rules.

To learn more, see [AWS WAF](https://aws.amazon.com/waf/).

## Use

- Manage and control which traffic is allowed to a web application through conditional signature detection


![](https://d1.awsstatic.com/Product-Page-Diagram_AWS-Web-Application-Firewall%402x.5f24d1b519ed1a88b7278c5d4cf7e4eeaf9b75cf.png)


### AWS Web Application Firewall (WAF)
- WEBACL Default actions (ALLOW or BLOCK)
- resource Type - CloudFront (Global) or regional Service (Ex. ALB, API GW, APPSync)
- Add Rule Groups or Rules - Which are processed in order
- Web ACL Capicity Unitcs (WCU) or how many rules you can have, defaults to 1500 but can be increased via a support ticket
- Associating a WEBACL with a resource can take time, but adjusting a WEBACL takes less time to take effect.
- Rule Groups do not have default actions, the action is defined when it is added to the WebACL.
- Rule Groups can be referenced by multiple WebACLs. 
- Rule Groups can be provided by you, managed by someone else (AWS or Marketplace), or Service managed (Shield/Firewall Manager)

WAF Rules
- Type, Statement, and Action
  - Type = Regular or Rate Based
  - Statement = (What to match) or (Count All) or (What and Count)
  - Origin country, IP, lable, headers, cookies, query parmeter, URI pathm query string, body (first 8192 bytes only) HTTP method
- Single, AND, OR, NOT
  - Actions: Allow*, Block, Count, Captcha... Custom Response Header, Label (labels can be referenced later in the same WEBACL.. for multi-stage flows.)
  - ALLOW & BLOCK stop processing, Count/Captcha actions continue
- Cost
  - WEBACL - Monthly $5/month (these can be resued ;))
  - RULE on a WebACL - $1/month
  - Requests per WEBACL - $0.60/1million
  - Intellegent Threat Mitigation
    - Bot Control ($10/month) & ($1/1mil requests)
    - Captcha - $0.40/1000 challenge attempts
    - Fraud Control/Account Takeover ($10 /month & 41 /1,000 login attempts
    - Marketplace rule groups - cost extra
