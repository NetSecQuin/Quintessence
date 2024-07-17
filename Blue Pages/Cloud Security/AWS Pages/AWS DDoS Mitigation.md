# AWS DDoS Mitigation

DDoS mitigation can be achieved through both blocking strategies and reduncy techniques. 

- Malicious inbound requests can be blocked through AWS Shield and AWS WAF.
- Web App resources can be distributed and cached across numerous geographic locations with CloudFront CDNs. 
- Routing to web applications can be dynamically changed based on load, location, and availability with Route 53 DNS. 

## Services

[AWS Route 53](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Route%2053.md) - Scalable DNS for your web applications. Includes smart routing options, monitoring, and health checks to improve preformance. 

[AWS CloudFront](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20CloudFront.md) - Amazon Content Delivery Network (CDN). Caches and serves website resources to edge locations to improve site speed. 

[AWS Shield](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20Shield.md) - Automatically mitigate certain DDoS attacks through ML signature detection after creating a baseline of normal traffic.

[AWS WAF](https://github.com/NetSecQuin/Quintessence/blob/main/Blue%20Pages/Cloud%20Security/AWS%20Services/AWS%20WAF.md) - Block traffic inbound to your web application based on granular signatures identified in web requests.

