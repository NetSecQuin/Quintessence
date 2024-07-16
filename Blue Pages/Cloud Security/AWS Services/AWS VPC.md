# AWS VPC

## Summary

With Amazon VPC, you can isolate your AWS resources in the cloud. Using a VPC, you can launch resources into a virtual network that you have defined. You can define this network to closely resemble a traditional network that you would operate in your own data center.

#### Subnet Routing
- Configure public IPs or private IPs to restrict access to the internet.  Give your public instances an IPv4 address, IPv6 address or both. 

#### Network ACLs (NACLs)
- Acts as a virtual firewall in front of your resources at the subnet level. By default all traffic is allowed.
- Configurable to allow or deny traffic based on specific IPs, protocols, or ports into or out of the VPC.

#### Security Groups
- Acts as virtual firewalls for your instances specifically. When creating an instances, you must pick security group(s) for it.
- Security Groups are stateful. If a connection is allowed inbound, responses will be allowed outbound, and vise versa.
- By default traffic is blocked inbound, unless specified by a security group.



![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721163600/qQMAeir7CedYq2w0pM_zlw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/tIGAAOvXG7iOcSTU_u1HIeJqGSJ0Dp5cG.png)
