# AWS Firewall Manager

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721163600/qQMAeir7CedYq2w0pM_zlw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/9voKOpBv0RJKsz-B_r8OE4wT87tgyCFBV.png)

## Summary

AWS Firewall Manager is a security management service that helps you to centrally configure and manage AWS WAF rules across your accounts and applications. Firewall Manager is able to bring new applications and resources into compliance with a common set of security rules from the start.

To learn more, see [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/)

## Use

- Central repository for managing firewall or gateway blocks across AWS services, and third party firewalls.
- Write a single set of firewall and WAF rules that can be pushed/replicated to numerous services and applications

![](https://d1.awsstatic.com/products/firewall-manager/product-page-diagram_AWS-Firewall-Manager%402x%20(1)1.ad6bf5281dc2c33c0493e9988e3504dd1590eaa2.png)


### AWS Network Firewall
A regional product that creates a network firewall subnet within your VPC included with network firewall endpoints. 
- Traffic flows into the VPC to the Firewall subnets via route tables. Firewall subnets route traffic with their attached route table to the network firewall endpoint. The network firewall endpoint audits the request, passes it back to the firewall subnet, which then follows the route table rule for traffic coming from the firewall endpoint, and forwards it to the subnet where the target resource is located.
