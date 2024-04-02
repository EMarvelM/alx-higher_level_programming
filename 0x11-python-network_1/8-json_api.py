#!/usr/bin/python3
""" takes in a letter and sends a POST request to 
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import requests
import sys

if __name__ == "__main__":
    if sys.argv[1]:
        data = {"q": sys.argv[1]}
    else:
        data = {"q": ""}
    re = requests.post("http://0.0.0.0:5000/search_user", data=data)
    _data = re.json()
    if _data && type(_data) == type({}):
        print("[{}] {}".format(_data.get(id), _data.get(name)))
    elif _date && type(_data) != type({}):
        print("Not a valid JSON")
    else:
        print("No result")


