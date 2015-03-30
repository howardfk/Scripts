#!/usr/bin/python
import os
import sys
import urllib2
import re
import timeit
import signal

def pullfiles():
   start = timeit.default_timer()
   filenames = []
   savedir = "/Users/howard/Documents/Research/VLF_Hissler/Data/"

#connect to a URL
   website = urllib2.urlopen("http://vlf-alexandria.stanford.edu/public_web_junk/southpole/2014/")

#read html code
   html = website.read()

#use re.findall to get all the links
   filenames = re.findall('SP.*?\.mat', html)

   count = 0
   countpass = 0
   for files in os.listdir(savedir):
      if files.endswith(".mat"):
         try:
            filenames.remove(files)
            count += 1
         except ValueError:
            countpass += 1
   print "counted number of removes", count
   print "counted number of failed removes", countpass
   print "number files less removed:", len(filenames)

#saves the file names into an array of html link
   links=len(filenames)*[0]
   for j in range(len(filenames)): #len(filenames)):
      links[j] = 'http://vlf-alexandria.stanford.edu/public_web_junk/southpole/2014/'+filenames[j]


   stop = timeit.default_timer()
   print stop - start

   for i in range(len(links)):
      os.system("curl -o "+ filenames[i] + " " + str(links[i]))

   print "links downloaded:",len(links)

def MyExit(signal,frame):
   print("exiting")
   sys.exit(0)

if __name__ == '__main__':
   signal.signal(signal.SIGINT, MyExit)
   pullfiles()
