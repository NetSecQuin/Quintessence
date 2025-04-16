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
