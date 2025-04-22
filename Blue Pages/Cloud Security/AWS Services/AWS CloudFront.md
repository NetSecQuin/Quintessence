# AWS CloudFront

![](https://explore.skillbuilder.aws/files/a/w/aws_prod1_docebosaas_com/1721239200/ZEcL0bTnPYhQOsOBxow55Q/tincan/1795780_1704469401_o_1hjd4l7tc11hedc913i09dklbhj_zip/assets/AQp2wf27Tee8twPh_afmqDZRDcGDnImN5.png)

## Summary

Amazon CloudFront is a content delivery network (CDN) service that can be used to deliver data, including your entire website, to end users. CloudFront only accepts HTTPS and HTTP well-formed connections to prevent many common DDoS attacks. These capabilities can greatly improve your ability to continue serving traffic to end users during larger DDoS attacks.

To learn more, see [Amazon CloudFront](https://aws.amazon.com/cloudfront/).

## Use

- Caches and serves end-users static and dynamic web content
- Improves speed of loading webpage resources or entire pages themselves by caching/storing data at closest edge data centers.
- Only accepts HTTPS and HTTP well-formed connections to prevent many common DDoS attacks.
- CloudFront does not support uploading files and will not support caching of files uploaded by end-users. It only provides cached files from origins. 

![](https://d1.awsstatic.com/products/cloudfront/product-page-diagram_CloudFront_HIW.475cd71e52ebbb9acbe55fd1b242c75ebb619a2e.png)


### CloudFront Origins
Where your content lives or where it is pulled from. The source location of your content.
- Can be an S3 Origin or a Custom Origin

### CloudFront Behaviors
The CloudFront behavior sits between the CloudFront Origin and CloudFront Distrobution. It defines the behavior that should be taken when a specific path is requested.

### CloudFront Distrobution
The *configuration* unit of CloudFront. Everything is configured within a distrobution
- CloudFront Distrobution has a URL/Distrobution name, but can configured to use your DNS name. 

### CloudFront Edge Locations
Local cache of your data distrobuted globably to near your customers. Smaller than AZs and predomidently used for storage. Cant deploy an EC2 to an edge location
- Provides the fastest and best preformance of service content to an end-user

### Regional Edge Cache
Provides an additional cache and is larger than the edge location, not as many. 
- If the data was not in the Edge location cache, the regional edge cache is requested to provide the object/content.
- If the data was not at the Regional Edge Cache, the regional edge cache requests the file from the origin. 

#### CloudFront and SSl 
- CloudFront Default Domain Name (CNAME DNS Record)
- SSL Supported by default with a *.cloudfront.net certificate.
- Allows HTTP or HTTPS, HTTP +> HTTPS, or HTTPS Only configuration
- There are two SSL Connections: Client => CloudFront and CloudFront => Origin
- Alneranate Domain Names can be added (CNAMES) via Route53?
  - If you want to use HTTPS for an anlternate domain name, you will need to use a matching certificate
  - You must generate or import the certificate into ACM **in the us-east-1 region**
- Self Signed certificates will not work. They must be public verified certificates.
- Old browsers (pre-2003) do not suppoert SNI, therefore CloudFormation charges extra for a dedicated IP for them. More details below. 

###### SSL History
SSL encryption is handled at the TCP layer of the connection, and host headers happens after that in Layer 7 (application layer). Therefore if an instance had one IP address but was trying to serve multiple domains, it wouldnt work. 
- In 2003, SNI, a TLS extension was added to the updated version of SSL which added the option for a host/domain to be included in the TCP handshake. This allowed for multiple domains to be hosted on one IP address.

##### CloudFront OAI/OAC & Custom Origins
Origin Access Identities (OAI) is a type of identity that can be assoiced with a CloudFront Distrobution to connect to S3 via the S3 connector origin (not custom URL origin)
- CloudFront 'becomes' that Origin Access Identity
- The Origin Access Idenitity can be used in S3 Bucket Policies and setup to deny all but one or more specific OAIs

For custom origins we cant use OAIs to control access. Therefore we have to use other methods like HTTPS headers to secure connections to/from Origins
- Configure the custom origin to check for an HTTP/HTTPS header including a custom value provided by CloudFront to ensure only traffic from the CloudFront distrobution is allowed
- Can Also use the IP ranges for CloudFront which are publically available and restrict traffic via a firewall.

##### CloudFront GeoRestriction
CloudFront is a globally available CDN, which hosts its data globaly across its edge locations by default. 
Geo Restictions blocks caching of the content to edge location based on the IP address of the client requester. 
- CloudFront GeoRestrictions
  - Whitelist/Blacklist of **Country Only**
  - Works by a GeoIP Database and applies to the entire distrobution
- 3rd party Geo Restriction
  - Completely customisable and involves using a compute instance to be the analyzer and control whether the client is allowed access
  - Can filter country but more accurately. City, street, etc. 
  - Can be used to filter by anything. Ex. usernames, purchases, user attributes, licenses, and more.
 
#### Private Distrutions (* behaviours)
By default cloudfront is public. Private would be where any request require a signed cookie or URL to access the distrobution
- You can configure multiple behaviours - each is *public* or *private*
- Old Way/Legacy Method - A cloudFront Key is created by an account root user, The account is added as a **TRUSTED SIGNER**
- New Way - **Trusted Key Groups** added

Singed URLs vs Signed Cookies
- Signed URLs provide access to **one object**
- Historically RTMP distrobutions couldnt use cookies, but that is no longer true
- Use URLs if your client does not support cookies
- Cookies provide access to groups of object (ex. All cat gifs)
- Or if maintaining application URLs format is important

###### Field-Level Encryption
Useful for ensuring encryption is followed while it is passed through numerous applications, where only some of the applications require the ability to decrypt of the data. 
- HTTPS encrypts the data in transit by default, but when it is recieved by the first host it is recieved in HTTP before re-encrypting and passing via HTTPs to to the next resource. Adding Field-Level encryption can be used to encrypt the data so that it can not decrypted by every application in the chain.
- Mainly used for highly-secure architectures.

### Lambda@Edge
Run lighteight lambda at edge locations. 
- They can adjust data between the viewer and the origin
- Currently only supports node.js and python
- Run in the AWS Public Zone, so it can not interact with private VPCs.
- Different limits vs normal lambda functions.

There are 4 stages where a ldmbda@edge can be deployed. 

Viewer Request => Origin Request => Origin Response => Viewer Response
- Viewer Request: 
  - After CloudFront recieves a request from a viewer (client)
- Origin Request:
  - Before CloudFront Forwards the request to an origin
- Origin Response:
  - After CloudFront recieves a response from an origin
- Viewer Response
  - Before a responses is forwarded to a viewer (client)
 
Limit Differences:
- Viewer Side of the chain:
  - 128MB for memory allocation & 5 seconds of function timeout
Origin side of the chain:
  - Normal Lambda MB for memory allocation & 30 seconds of function timeout
 
What can Lambda@Edge be used for?
- A/B testing - viewer request
  - Change the URL requested based upon other request details. Ex. Change an image to be loaded based on a header
  - Migration between S3 origins - Origin Request
  - Different objects based on device - origin request. Ex. Check device screen size and choose objects servered to fit their device better
  - Content by Country - Origin Request. Ex/ Netflix
  - More: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html#lambda-examples-redirecting-examples
