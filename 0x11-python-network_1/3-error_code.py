#!/usr/bin/python3
"""URL, sends a request to the URL and displays the body
"""

from urllib import request, error
import sys

if __name__ == "__main__":
    try:
        url = request.Request(sys.argv[1])
        with request.urlopen(url) as data:
            _str = data.read().decode("ascii")
            print(_str)

    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
