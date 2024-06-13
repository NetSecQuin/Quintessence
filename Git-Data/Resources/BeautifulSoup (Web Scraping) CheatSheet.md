# BeautifulSoup (4)
BeautifulSoup is a web scraping and parsing utility when paired with the requests library

### Importing BeautifulSoup

``` from bs4 import BeautifulSoup ```

### Pulling data with Requests

```
url = "https://www.example.com/stufftoscrape

# Make get request and print results in text format
result = requests.get(url)
print(result.text)

# run a get requests and store the data as result. Parse result with BeautifulSoup html parser. Prettyify HTML. 
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
print(doc.prettify())
```

### Finding the tag containg the desired data
Option A.) Search via the HTML headers
```
# You can search for multiple headers at once
ModelTag = doc.find_all(["h1","h2","body"])

# Or one header at a time
ModelTag = doc.find_all("h2")

#Limit the child tags to the one you want with the number it appears. Starts with 0. This one was at h2.1
ModelTag = doc.find_all("h2")[1]
```
Option B.) Search for a string in the webpage.
```
price = doc.find_all(string="$168.63")
```
Option C.) You can search both at the same time
```
price = doc.find_all(["h1","h2"], string="$163.63")
```
Option D.) If you know the HTML header, you can use header="value" statements
```
price = doc.find_all(div="$163.63")
```
Option E.) You can use Regular Expressions (Regex)
```
# must import re first
import re

# This expression will find a dollar sign followed by any number of characters
price = doc.find_all(text=re.compile("\$.*"))
```
If the identified header is too common in a large dataset, you can point to the parent header and print the entire element. By adding more '.parent' statements we can continue to see the grandparents
```
parent1 = price[0].parent.parent
print(parent1)
```

### Store data associated to a tag
In the below example the model HTML tag was stored in 2nd the h2 header value. (h2.1). Remove the HTML tag with 'ModelTag.string'
```
ModelTag = doc.find_all("h2")[1]
Model = ModelTag.string
print(Model)
```
In this case the price was enclosed in the 2nd occurance of `<noscript><div>$$$</div></noscript>`. using find_all to identify the path
```
price_headtag = doc.find_all("noscript")[1]
price_tag = price_headtag.find_all("div")[0]
price = price_tag.string
print(price)
```
