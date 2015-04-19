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
   savedir = "/Volumes/JIMSDISK/Data/"

   total = 0
   count = 0
   countpass = 0
   #connect to a URL
   website = urllib2.urlopen("http://vlf-alexandria.stanford.edu/public_web_junk/southpole/2014/")

   #read html code
   html = website.read()

   #use re.findall to get all the links end with .mat
   filenames = re.findall('SP.*?\.mat', html)
   total = len(filenames)
   list_saved = os.listdir(savedir)
   print list_saved[0], list_saved[1]

   for files in list_saved:
      if files.endswith(".mat"):
         #removing the files on the disk form the list of downloads
         try:
            filenames.remove(files)
            count += 1
         except ValueError:
            countpass += 1
   if countpass != 0:
      print "num errors:", countpass
   print "Total number of files on website:", total
   print "counted number of removes", count
   print "number files not removed:", len(filenames)

#saves the file names into an array of html link
   links=len(filenames)*[0]
   for j in range(len(filenames)): #len(filenames)):
      links[j] = 'http://vlf-alexandria.stanford.edu/public_web_junk/southpole/2014/'+filenames[j]


   stop = timeit.default_timer()
   print stop - start

   for i in range(len(links)):
      print filenames[i]
      #os.system("curl -o "+ filenames[i] + " " + str(links[i]))

   print "links downloaded:",len(links)

def MyExit(signal,frame):
   print("exiting")
   sys.exit(0)

if __name__ == '__main__':
   signal.signal(signal.SIGINT, MyExit)
   pullfiles()
