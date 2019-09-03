#!/usr/bin/python
import sys
import json
import urllib2
from urllib2 import Request, urlopen, URLError

'''
desc: a simple script that query the MAC address's vendor via API call
      from https://macaddress.io API
args:
    argv[1]: your API key from macaddress.io
    argv[2]: the target mac address you lookup
return:
    the Company Name associated with that MAC address
'''

apikey = sys.argv[1]
macaddress = sys.argv[2]
url = 'https://api.macaddress.io/v1?apiKey=' + apikey + '&output=json&search=' + macaddress
# print(url)

response = urllib2.Request(url)

try:
    handler = urllib2.urlopen(response)
    json_data = json.load(handler)
except URLError, e:
    print e.code
    sys.exit(2)

searchmac = json_data['macAddressDetails']['searchTerm']
companyname = json_data['vendorDetails']['companyName']
print(companyname)
