# Python Cheatsheet

# Reading files in

Opens index.html as readonly (r), and read it in as input as f 
```
with open("index.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")
```
