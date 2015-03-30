#!/usr/bin/python
import os
import urllib2
import re

filenames = []

#connect to a URL
website = urllib2.urlopen("http://vlf-alexandria.stanford.edu/public_web_junk/southpole/2014/")
#http://www.dartmouth.edu/~spacephy/labelle_group/data/churchill/2012.html")

#read html code
html = website.read()

#use re.findall to get all the links
#links = re.findall('"(http|ftp)s?://.*?.mat"', html)
filenames = re.findall('SP.*?\.mat', html)

#saves the file names into an array of html link
links=10*[0]
for j in range(0,9): #len(filenames)):
   links[j] = 'http://vlf-alexandria.stanford.edu/public_web_junk/southpole/2014/'+filenames[j]

#for i in links:
#   filename.append(i[-22:])

#os.system("curl -o "+ filenames[1] + " " + str(links[1]))

for i in range(len(links)):
   os.system("curl -o "+ filenames[i] + " " + str(links[i]))

print 
print len(links)
