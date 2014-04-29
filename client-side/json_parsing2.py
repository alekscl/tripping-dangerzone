#!/usr/bin/env python
import json


# decode the json file
output = json.load(open('cars.json'))

# display the output
print output["CARS"][0]["MODEL"]
