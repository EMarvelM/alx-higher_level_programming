#!/bin/bash
# take a url, send a request and displays the size of the body
url=$1
#curl -w "%{size_download}" "$url"
curl -s "$url" | wc -c


