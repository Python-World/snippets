#The below code snippet is used as a web scrapper and can be used in any website to scrap all the hyperlinks from the website.


#import the required libraries.
import urllib2
import re

#connection making to the target website  URL

website = urllib2.urlopen(website_url)

#read html code from the target website
html_code = website.read()

#use re.findall to get all the links from the website

hyperlinks = re.findall('"((http|ftp)s?://.*?)"', html_code)

print hyperlinks
