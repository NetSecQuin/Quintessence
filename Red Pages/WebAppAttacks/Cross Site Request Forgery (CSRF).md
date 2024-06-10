# Cross Site Request Forgery (CSRF)
Cross Site Request Forgery is an attack where the victim is lured to a malicious site or form that includes requests to other sites that the user does not expect. The goal of this attack is to use the victims session tokens and cookies to make requests or take actions on another site via the behalf of the victim. The common protection for these attacks are Cross Origin Resource Sharing (CORS) policies, which check the refferer headers of requests.

## Exploitable Fields
As this attack relies on the attacker creating a site or form an embedding requests to other sites inside the page, there are many 'fields' that can be used for the exploit. Some common ones:

- Forms
- Buttons
- Links
- Images

## Types of CSRF

### Synchronous CSRF
Occurs when the victim can visually see the redirect happen after falling victim the attack. For instance upon submitting a form regarding favorite sports teams, the user notices they have suddenly been redirected to their banks website. 

### Asynchronous CSRF (Blind CSRF)
When the request forgery is not directly visible to the user.

### Traditional CSRF
Relies on there being no Cross Origin Resource Sharing policy in place, which allows requests to be made to the site without verification of the referer header. 

### Cross-Origin (XO-CSRF)
Sometimes the CORS policy is implemented with vulnerabilities allowing for it to be exploited and CSRF attacks to still work. Things such as allowing an origin of `*` , allowing any subdomain of the site as a referer like `*.example.com`, or in some cases allowing any port number of the domain (malicious site being hosted on http on an https domain.)

### JSONP CSRF
Utalizes two requests on the attackers malicious site. The first makes a request to the page the CORS policy would expect to be the origin for the target request. The first page does not have a CORS policy, but generates a token. The attackers site then grabs the token, and uses it with the referer header to make the second request. Thus bypassing the CORS policy. 

### Remediation

- Implement strict CORS policies
- Utalize anti-CSRF tokens
- Disable JSONP where it is not 100% required.
- Phishing awareness and training
