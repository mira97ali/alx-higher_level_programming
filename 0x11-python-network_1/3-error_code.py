#!/usr/bin/python3
"""Send Request"""
import sys
from urllib import request, error


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as res:
            print(res.read().decode("UTF-8"))
    except error.HTTPError as exc:
        print("Error code:", exc.code)
