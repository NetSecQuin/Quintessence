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
DNS in a VPC is provided by Route53 by default, and will be the VPC 'base IP +2' address. Ex. Base IP = 10.16.0.0 then first instance will be 10.16.0.2

There are two DNS options
- 'enableDnsHostname' - Give instances DNS hostnames
- 'enableDnsSupport' - Enabled DNS resolution in the VPC. Hosts can use the DNS address to resolve the host in the VPC

#### VPC Router
The virtual router within a VPC, which is automatically provisioned in all AZs within the VPC. They require no performance managmenet 

- Routes traffic
  - From one subnet to another across AZs
  - From external networks into the VPC
  - From the VPC into external networks
  - Assigned "subnet+1" address in every subnet. (Ex. Subnet range = 10.16.16.0/16. VPC Router IP = 10.16.16.1)
 
  - 
#### Subnet Routing
- Configure public IPs or private IPs to restrict access to the internet.  Give your public instances an IPv4 address, IPv6 address or both.
- Subnets are hosted in Availability Zones (AZs). A subnet can not span AZs
- Subnets cannot overlap with other subnet ranges within a VPC
- Subnets can communicate with other subnets in the VPC

Routing is defined through Route tables. 
A route table designates which route the router will use to find the destination address. i.e Who the router will ask "do you know dest.ip?" first.
- Every VPC is created with a main route table by default. **A subnet is assoicated with only one Route Table**
- The main route table can be replaced with a custom route table.
- The router will preference the more specific subnet range specificed that matches its destination

##### Subnet IP Addressing
For this example, lets say that we have an subnet range of 10.16.16.0/20 (10.16.16.0 => 10.16.31.225)
- Reservered IP addresses: The first 4 IPs, and the last IP in the subnet range are reserved in AWS VPCs.
  - 10.16.16.0 : Network Address (Represents the starting address of the network)
  - 10.16.16.1 : VPC Router (logical network device used to move traffic within and optionally outside of the subet)
  - 10.16.16.2 : Reservered for DNS
  - 10.16.16.3 : Reserverd for future use
  - 10.16.31.255 : Last IP in subnet
 
##### DHCP Option Sets (DHCP in a VPC)
In AWS you can either use explicitly customer provided values or AWS provided through VPC DNS (Route53).
DHCP option sets define how IP addresses are assigned in your VPC to resources. For example defining the reserverd IP addresses. 

- DHCP option sets can be assocaited with 0 or more VPCs.
- DHCP option sets cannot be edited once created.
- DHCP option sets can be associaetd to a VPC immediately, but require a DHCP Renew for changes to take effect, which takes time
- AWS Supply public and private DNS names. To use custom domains you need to use custom DNS servers:
  - Private Ex. ip-10-16-16-14.us-west-2.compute.internal
  - Public Ex. 55.55.54.53.us-west-2.compute.amazonaws.com

#### Network ACLs (NACLs)
- Acts as a virtual firewall in front of your resources at the subnet level. Offers explicit allows and explicit denies. Default is to allow all. 
- Configurable to allow or deny traffic based on specific IPs, protocols, or ports into or out of the VPC.
- As they filter traffic crossing the subnet boundry, they do not inspect traffic between resources within a subnet.
- Rules are processed in order, lowest rule number first. If a earlier rule says deny and a later rule says allow, the traffic will be denied.
- Stateless, so they cannot detect whether the packet is a request or a response. Blocking soley based upon traffic direction.
  - Therefore: Because http/https traffic communicates over TCP, we will have a response on an ephemeral port between 1024 - 65535. An Example NACL policy to allow all HTTPS traffic would be
    - Inbound Allow 0.0.0.0/0 port 443 : Deny 0.0.0.0/0 all
    - Outbound Allow 0.0.0.0/0 port 1024-65535 : Deny 0.0.0.0/0 all
 - AWS prefers you to use security groups, which is why the default NACL is allow all. However, custom NACLs are deny all by default.
 - Can only reference IP ranges and IP addresses. Can not use logical resources. 
 - Used instead of security groups to block 'bad/malicious IPs' or networks. NACLs would be better for blocking a malicious IP.
 - Can be associated with multiple subnets

#### Internet Gateways
*Can* be created and attached to AWS VPCs
- 1 to 1 relationship with VPC. 1 VPC : 1 IG
- Used to access AWS public services and public internet
- Works across all AZs in your VPC, and resilient to AZ faliure. Can be used to route to secondary AZ when there is an outage/failure. 
- Works with IPv4 and IPv6 ingress & egress.
  - IPv4 : Static NAT - Private IPv4 back and forth between Public IPv4. Static NAT requires the instance to have an allocated public IP address
  - IPv6 : IPv6 does not distinguish Private/Public so there is no back and forth translation.
 
In order to access AWS public services and public internet, an internet gateway must be used. To do this via the **IPv4 Static NAT** method:
- 1.) Create IGW and attach it to the VPC
- 2.) Create a custom Route Table and associate that the subnet you want to have public internet access
- 3.) Configure the route tables default routes to forward to the IGW.
- 4.) Configure the subnet to allocate public IP addresses to each of the instances in the subnet.
- 5.) The IGW will recieve the packets and translates the private IPv4 address to its public IPv4 during external communication. 

###### Egress-Only Internet Gateways
Since IPv6 does not differentiate Private/Public, we must use Egress-Only Internet Gateways. 
- Exactly the same as a regular internet gateway, how we use it slightly differs.
  - Acts as the NAT for IPv6?



#### Security Groups
- Acts as virtual firewalls for your instances specifically. When creating an instances, you must pick security group(s) for it.
- Security Groups are stateful. Therefore when comunicating or accessesing a site/application over TCP, it can detect and group request and response packets on ephemeral ports. Therefore a block on outbound requests to an IP will also block response packets
- By default traffic is blocked inbound, unless specified by a security group.
- NO EXPLICIT DENY.. only allow or implicit deny - can't block bad actors.
- Supports IP/CIDR and **logicial resources**
- Attached to ENIs not instances (even though it may look the other way in the console)
- REVIEW THIS AGAIN: "a 'SG source' is the same as "anything with the SG attached". Using a 'self-reference', means "anything with this SG attached.

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721163600/qQMAeir7CedYq2w0pM_zlw/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/tIGAAOvXG7iOcSTU_u1HIeJqGSJ0Dp5cG.png)



### VPC Endpoints

#### Gateway VPC Endpoints

Provide private access to supported services (At this time S3 & DynamoDB) [Which are public resources* and exsist in the AWS public zone outside of any VPCs.]
- Use a prefix list added to route-table to describe the gateway endpoint. describes route to gateway endpoint instead of subnets
- It is highly avaiable across all AZ in a region by default. 
- Endpoint policy (Ex. Bucket resource policy) is used to control what it can access
- They are regional, and cant access cross-region services.
- Help with locking down an S3 bucket by only allowing access from a gateway endpoint.
  - Useful for An instance needing to access an S3 bucket, but we do not want to provide access to the internet. 



#### Interface VPC Endpoints

Uses PrivateLink to inject AWS or 3rd party services network interfaces inside your private VPC and given network interfaces for internal communciation.  
- Any service except DynamoDB (S3 was just added)
- not highly available by default. Is an ENI added to specific subnets. It can become highly available if you add one endpoint, to one subnet, per AZ used in the VPC. 
- Uses security groups to control network access
- Endpoint policies restrict what can be down with the endpoint. Endpoint policies are attached to the of the instance or interface endpoint.
- TCP and IPv4 ONLY
- Creates a endpoint DNS name for accessing the service
  - Ex. vpc1-123-abc.sns.us-west-2.vpc1.amazonaws.com
    - Regional DNS names (unique to region)
    - Zone based DNS (unqiue to zone)
 - Private DNS associateds a private Route53 Hosted Zone to the VPC, cahnging the default service DNS to resolve to the interface endpoint ip
   - This means that we do not need to make changes to the endpoints of the services themselves, but instead use a DNS overroute overide to route through the interface endpoint.
  
###### VPC Endpoint Policies
VPC Endpoints (vpce) allow access to an entire service in a region.
- limits access via that endpoint only
- Contains a principal and conditions
- Commonly used to limit what private VPCs can access. Instead of providing a private VPC with full access to anything accessible in a service like S3, the endpoint policy can limit how it is used. (Ex. Company has 1 private s3 bucket and 1 public to anyone s3 bucket. If we want to only allow access to the private s3 bucket, we can limit the services use with an endpoint policy. )
