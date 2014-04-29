#!/usr/bin/env python
import json

# decodes the json file
output = json.load(open('cars.json'))

# display output to screen
print output

# If you're having a hard time, try changing the print statement to:
print json.dumps(output, indent=4, sort_keys=True)
