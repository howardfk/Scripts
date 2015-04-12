#!/usr/bin/python
import os
import sys
import urllib2
import re
import timeit
import signal

cwd  = os.path.dirname(os.path.abspath(__file__))

def listPlots():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    up_dir = os.path.dirname(script_dir)
    path = os.path.join(up_dir, "Plots")
    plotlist = [files for files in os.listdir(path)]
    return plotlist

def checkfiles(alist):
    plotdir = [files for files in alist]
    filelist = [files for files in alist]
    if plotdir == []:
        return plotdir
    else:
        return plotdir
    #filelist = [files for files in os.listdir(datapath) if os.path.isfile(os.path.join(datapath,files))]

def main():
    savelist = listPlots()
    print savelist
    print checkfiles(savelist)

if __name__ == "__main__":
    main()

