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
In order to find the text in the HTML, Either locate a searchable string from the website in this case, or use its identifier like '$'. In this case the '$' was included in the price without any space, which made it hard to locate with the $ alone.
```
# price = doc.find_all(string="$168.63")
```
Then Point to the Parent header and print the entire element. By adding more '.parent' statements we can continue to see the grandparents
```
# parent1 = price[0].parent.parent
# print(parent1)
```

### Store data associated to a tag
In the below example the model HTML tag was stored in 2nd the h2 header value. (h2.1). Remove the HTML tag with 'ModelTag.string'
```
ModelTag = doc.find_all("h2")[1]
Model = ModelTag.string
print(Model)
```
In this case the price was enclosed in the 2nd occurance of <noscript><div>$$$</div></noscript>. using find_all to identify the path
```
price_headtag = doc.find_all("noscript")[1]
price_tag = price_headtag.find_all("div")[0]
price = price_tag.string
print(price)
```
