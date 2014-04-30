#!/usr/bin/env python
import json
import requests


def main():
    porigin = "origin=Calle+de+Caleruega+Madrid"
    pdestination = "destination=Calle+Orense+Madrid"
    psensor = "sensor=false"
    url = "http://maps.googleapis.com/maps/api/directions/json?" + \
        porigin + "&" + pdestination + "&" + psensor
    response = requests.get(url)

    with open("response.json", "wb") as f:
        f.write(response.content)

    output = json.load(open("response.json", "rb"))

    for route in output["routes"]:
        for leg in route["legs"]:
            for step in leg["steps"]:
                print step


if __name__ == "__main__":
    main()
