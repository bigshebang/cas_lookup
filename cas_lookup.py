#!/usr/bin/env python3
'''
'''
import sys
import fileinput
import requests

headers = {'accept': 'application/json'}

def cas_lookup(query_string):
    #curl -X GET "https://commonchemistry.cas.org/api/search?q=dmap" -H  "accept: application/json"
    res = requests.get("https://commonchemistry.cas.org/api/search?q={}".format(query_string), headers=headers)
    if res.status_code == 200:
        # grab first result and the "rn" attribute inside of it
        cas_number = res.json()['results'][0]['rn']
        return cas_number

    return None

def main():
    for line in fileinput.input():
        # strip newlines and make sure there's a slash in there
        stripped_line = line.rstrip()
        print(cas_lookup(stripped_line))

    return 0

if __name__ == '__main__':
    sys.exit(main())
