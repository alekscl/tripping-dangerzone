#!/usr/bin/env python
import requests


def main():
    url = "http://httpbin.org/post"
    data = {'fname': 'Michael', 'lname': 'Herman'}
    r = requests.post(url, data=data)
    print r.content


if __name__ == "__main__":
    main()
