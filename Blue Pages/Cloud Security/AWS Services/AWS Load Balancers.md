# AWS Load Balancers

There are three types of AWS Load Balancers: Elastic Load Balancer, Application Load Balancer, Network Load Balancer


### Elastic Load Balancer (ELB)
- Configured to run in 2+ Availablility Zones. Nodes are placed in a subnet in each AZ and scale with load.
- Each ELB is configured with an (A) record DNS name. This reoslves to the ELB Nodes.
- Can be internet facing or internal. This choice decides whether the nodes get public or private IP addresses.
- Load Balancers (Nodes) are configured with listensers, which accept traffic on a port & a protocol with a target group configured communicate on a port and protocol
- A private ELB can connect to either public or private EC2 instances.
- /27 is the right CIDR for an ELB becausae4 they require 8+ free IPs per subnet.

### Cross Zone Load Balancer
- Initially, Elastic Load Balancers did not support cross zone communication. This was fixed by the addition of the cross zone load balancer

### Application Load Balancers
- Classic application load balancers didnt scale since each HTTPS name requires an individual Load Balancer (SNI isnt supported). With v2, rules and target groups were added. Which allow host based routing rules via SNI. This results in ALB consolidation
-  Layer 7 load balancer, listens on HTTP and/or HTTPS but can not understand any other layer 7 protocols (SSH, SMTP, etc.) Does not support TCP/UDP/TLS listeners
-  Can inspect and preform descisions based on Layer 7 content (content type, cookies, custom headres, user location, etc.)
-  HTTP HTTPS SSL/TLS alwways terminated on the ALB. If you require encryption in transit to continue through the load balancer to the target, you must use an NLB. In most cases the ALB is enough, but it depends on the application. 
-  ALBs must have SSL certificaties if HTTPS is used
-  ALBs are slower than NLB due to the increased visibility/content
-  Rules direct connections which arrive at a listener, they are processed in a priority order, and the load ballencer has a default action if no rules are net.
-  Rule Conditions: host-header, http-header, http-request-method, path-pattern, query-string & source IP.
-  Actions: forward, redirect, fixed-response, authenticate-oidc & authenticate-cognito.


### Network Load Balancers
- Layer 4 load balancer (TCP, TLS, UDP, TCP)
- No visibility or understanding of HTTP or HTTPS, can not see into application level request data (headers, etc.)
- No headers, no cookies, no sticky sessions
- Really Really Really fast (millions of requests per second, 25% of ALB latencny
- Health check just check ICMP/TCP handashake.
- NLBs can have static IPs which can be useful for whitelisting
- Forward TCP to instnaces without breaking encrpytion in transit. (unlike ALB which breaks encryption)
- Any requirement for PrivateLink needs NLB
- Used for protocols other than HTTP or HTTPS

### SSL Offload
- Bridging Mode:
  - Listener is configured for HTTPs, Connection is terminated on the ELB, therefore the ELB needs a certificate for the domain. Then the ELB initiates a new SSL connection to backend instances. Instances need SSL certificates and the compute required for the cryptographic operations.
- Pass-through
  - Listener is configured for TCp. No encrpytion or decryption happens on the NLB. Connection is passed to backend instance. Each instance still needs to have the appropriate SSL certificates installed and stored locally. This solves the issue with AWS ELB having the certificate stored, but doesnt resolve the issue on the instances.
-  Offload
  - Listener is configured for HTTPS, connections are terminated and a new backend connection is initatied by the ELB using HTTP. Since the connection does not use SSL, the host does not need to have the SSL certificate installed and stored locally. This resolves the risk of it being installed on the host, but entrusts AWS with the certificate.

### Connection Stickiness
With no stickiness connection are distrobuted across all in-service backend instances. This causes issues for the client as the state of their site may change if the load balancer routes traffic to a different node. 
- AWS ALB stickiness generates a cookie which locks the device to a signle backend instance for a duration


### Security Policies
- Security Policy = Set of ciphers & proocols (which are OK to use, on the listener)
- protocol ensures secure client => server communication (can use many ciphers)
- Cipher is an algorithm. Client and server present ciphers/protocols best supported one is picked.
- You control policy between Client => LB. But AWS chosen one is used for LB => Targets
- Newer Policies = more secure, but less compatable. 
