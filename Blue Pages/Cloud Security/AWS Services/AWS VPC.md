# AWS VPC

## Summary

With Amazon VPC, you can isolate your AWS resources in the cloud. Using a VPC, you can launch resources into a virtual network that you have defined. You can define this network to closely resemble a traditional network that you would operate in your own data center.

- VPCs are regionally isolated service
- Isolated Networks within an AWS account
- Nothin IN or OUT without explicit configuration
- Offer flexible configuration (Simple or Multi-Tier)
- Can be configured to connect cloud & on-prem networks (via site-to-site, direct connect, etc.)
- Creation offers *Default* or *Dedicated Tenancy*, where if you do dedicated tenancy, every instance must be installed on that tentant, which can add a significant cost. *Only use Dedicated Tenancy if 100% necessary*

### Custom VPCs

When creating a custom VPC, by default it will be generated with one primary private IPv4 CIDR block
- It will have a min of /28( 16 IPs) and a max of /16 (65,536 IPs)
- Optionally it can have a secondary, or upto five before a support ticket, additional CIDR blocks.
- Optionally it can have a public IPv4 CIDR block
- Optionally it can have a IPv6 /56 CIDR block

#### DNS in a VPC
DNS in a VPC is provided by Route53 by default, and will be the VPC 'base IP +2' address. Ex. Base IP = 10.0.0.0 then first instance will be 10.0.0.2

There are two DNS options
- 'enableDnsHostname' - Give instances DNS hostnames
- 'enableDnsSupport' - Enabled DNS resolution in the VPC. Hosts can use the DNS address to resolve the host in the VPC

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
