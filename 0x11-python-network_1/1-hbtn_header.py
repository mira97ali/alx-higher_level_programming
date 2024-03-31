#!/usr/bin/python3
"""Send Request"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headers = dict(response.headers)
        print(headers.get("X-Request-Id"))
