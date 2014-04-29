#!/usr/bin/env python
from xml.etree import ElementTree as et
import requests


def main():
    url = "http://www.w3schools.com/xml/cd_catalog.xml"
    xml = requests.get(url)

    with open("test.xml", "wb") as code:
        code.write(xml.content)

    doc = et.parse("test.xml")

    for element in doc.findall("CD"):
        print("Albums: %s" % (element.find("TITLE").text))
        print("Artist: %s" % (element.find("ARTIST").text))
        print("Year: %s" % (element.find("YEAR").text))
        print("\n")


if __name__ == "__main__":
    main()
