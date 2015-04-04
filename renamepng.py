#!/usr/bin/python
import os
import sys
import urllib2
import re
import timeit
import signal
 
cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)
