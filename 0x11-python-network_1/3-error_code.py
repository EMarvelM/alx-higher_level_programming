#!/usr/bin/python3
"""URL, sends a request to the URL and displays the body
"""

from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as data:
            _str = data.read().decode("utf-8")
            print(_str)

    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
