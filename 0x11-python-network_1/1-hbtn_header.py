#!/usr/bin/python3
"""URL, sends request to the URL and displays the value of the X-Request-Id"""
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as data:
    head = data.headers
    print(head.get("X-Request-Id"))
