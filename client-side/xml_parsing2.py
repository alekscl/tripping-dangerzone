#!/usr/bin/env python
from xml.etree import ElementTree as et


def main():
    doc = et.parse("cars.xml")

    for element in doc.findall("CAR"):
        print("%s %s %s" %
              (element.find("MAKE").text,
               element.find("MODEL").text,
               element.find("COST").text))


if __name__ == "__main__":
    main()
