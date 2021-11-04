#!/usr/bin/env python

# Filename:                     restconf-tutorial.py
# Command to run the program:   python restconf-tutorial.py

import requests
import json

# Suppress HTTPS warnings
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
 
# Print a stream of bytes as pretty JSON
def printBytesAsJSON(bytes):
	print(json.dumps(json.loads(bytes), indent=2))


# Retrieve configuration through RESTCONF
response = requests.get(
    url='https://10.10.20.48/restconf/data/Cisco-IOS-XE-native:native/interface/GigabitEthernet=1',
    auth=('developer', 'C1sco12345'),
    headers={
        'Accept': 'application/yang-data+json'
    },
    verify=False)

# Pretty print our JSON response
printBytesAsJSON(response.content)


