# Google Dorking Cheatsheet

### List of Operators

``` " " ``` - Restrict results to only show results with the phrase

``` | ``` - OR

``` ( ) ``` - Groups multiple operations together 

``` * ``` - Wildcard 

``` + ``` -  AND

``` #..# ``` - show all pages contian a number from #-#

``` -* ``` - negate the field

### List of fields

``` site: ``` - Search for a particular website, domain, or subdomain

``` ext: ``` or ``` filetype: ``` - Restrict results to a specific filetype

``` inurl: ``` -Restrict for a phrase that must be found in the specific URL string/path

``` intitle: ``` Restrict to results with a phrase in the sites title

``` @twitter/reddit/facebook/etc. ``` - Only show cooresponding social media pages

``` imagesize: ``` only show results that are images of a specific size

``` link: ``` find sites that contain links to a specific domain

### Useful searches and examples

Find sites with boat in the URL but do not show results regarding sushi boats

```
Ex. inurl:"boat" -inurl:"sushi"
```

Look for specific filetypes that contain certain strings
```
Ex. ext:pdf|ext:doc|ext:xlsx "Confidential" + "Sensitive"
```

Search for specific types of sites (Finds either .gov or .edu sites)
```
Ex. site:.gov|site:.edu
```
