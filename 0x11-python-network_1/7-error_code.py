#!/usr/bin/python3
""" URL, sends a request to the URL and displays
    the body of the response.
"""

if __name__ == "__main__":
    import requests
    import sys

    argv = sys.argv
    req = requests.get(argv[1])
    req.status

