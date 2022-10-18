#!/usr/bin/env python3
'''
    A script that takes in a list of chemical names from STDIN and looks them up on cas.org one by
    one and prints the corresponding CAS number.
'''

import sys
import fileinput
import requests

headers = {'accept': 'application/json'}

def cas_lookup(query_string):
    #curl -X GET "https://commonchemistry.cas.org/api/search?q=dmap" -H  "accept: application/json"
    res = requests.get("https://commonchemistry.cas.org/api/search?q={}".format(query_string), headers=headers)
    if res.status_code == 200 and res.json().get('count') > 0:
        # grab first result and the "rn" attribute inside of it, that's the CAS number for the first result
        cas_number = res.json()['results'][0]['rn']
        return cas_number

    return "Not Found"

def main():
    # loop through every line of STDIN
    for line in fileinput.input():
        # strip newlines
        stripped_line = line.rstrip()
        print(cas_lookup(stripped_line))

    return 0

if __name__ == '__main__':
    sys.exit(main())
