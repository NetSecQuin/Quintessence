# AWS VPNs

VPN Considerations
- Speed Limitations ~ 1.25Gbps per AWS VPN endpoint or VGW (AWS Limit)
- Runs over public internet, which can add inconsistencies and latency.
- Cost - AWS hourly cost, GB out cost, data caps on premisis.
- Can be used as a backup for Direct Connect (DX) or while you migrate to Direct Connect. 




## Static vs Dynaic VPNs
- The difference is how routes are communicated
    - Static: static routes added to route tables. Network for remote side are statically configured. There is no multiconnection failover or loadbalencing.
    - Dynamic: Uses Border Gateway Protocol (BGP). netowrks are configured using ASN and exchanged over BGP. Multiple VPN connections provides high availability and traffic distrobution. CGW would need to support BGP to use Dynamic. 
- Note:your CGW must support dynamic.

## Virtual Private Gateway (VGW)
- Gateway for connecting AWS VPCs with a non-aws networks.
    - Can attach to only one VPC at a time.
    - can be detached/reattached
    - target on one or more route tables
    - creates endpoints in different AZ, so it is highly available and can withstand failure
 
### VPN CloudHub

## Site-to-Site VPN 
A connection, using IPSec for encrypion, over the public internet to connect a VPC and an onprem network. 
- Quick to provision (>1hr)
- Consists of two components
    - Virtual Private Gateway (VGW) - See above
    - Customer Gateway (CGW) - Customer on-prem router that handles the routing to the VGW. Single point of failure with only one, best practice is to have a 1+ at different locations. 
        - VPN Connection is between the VGW and CGW
     
## Client VPN
Like a Site2Site, but instead of connecting networks it connects and endpoint to a newtwork directly
- Managed implementation of "OpenVPN"
- Any client with OpenVPN software is supported
- Associated with one VPC
- Billed based on network associations

The clients OpenVPN software changes the clients route-table to forward all traffic through the Client VPN endpoint. If the client wants internet access post VPN endpoint, the Client VPN ENI would forward traffic to a NATGW and onto the internet. 

A split tunnel client VPN is where the route table is not overwritten but added to the bottom. This way, typical internet traffic routes over the internet, but the client will be routed to the private network if the address is not found. THIS IS NOT THE DEFAULT, MUST BE ENABLED.
