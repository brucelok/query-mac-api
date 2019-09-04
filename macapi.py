#!/usr/bin/python
import sys
import json
import urllib2
from urllib2 import Request, urlopen, URLError, HTTPError

'''
desc: a simple script that query the MAC address's vendor via API call
      from https://macaddress.io API
args:
    argv[1]: your API key from macaddress.io
    argv[2]: the target mac address you lookup
return:
    the Company Name associated with that MAC address
'''

def handle_404_error(code):
    print 'Failed to reach server, error: ', code
    reason = 'not found'
    return reason

def main():
    apikey = sys.argv[1]
    macaddress = sys.argv[2]
    url = 'https://api.macaddress.io/v1?apiKey=' + apikey + '&output=json&search=' + macaddress
    #url = 'http://www.python.org/f'
    response = urllib2.Request(url)

    try:
        handler = urllib2.urlopen(response)
        json_data = json.load(handler)
    except HTTPError, e:
        print e
        if e.code == 404:
            handle_404_error(e.code)
            sys.exit(2)
    except URLError as e:
        print e
        sys.exit(2)

    searchmac = json_data['macAddressDetails']['searchTerm']
    companyname = json_data['vendorDetails']['companyName']
    print(companyname)

if __name__ == '__main__':
    main()
