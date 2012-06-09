#!/usr/bin/env python

import requests
import sys
from optparse import OptionParser

opts = OptionParser('Usage: %prog [-f filename]')
opts.add_option('-f', '--file', dest='filename', default='', type='string',
        nargs=1, help='File whose contents you want to upload.')

valid, _ = opts.parse_args()

data = {'sprunge': ''}
if valid.filename:
    data['sprunge'] = open(valid.filename).read()
else:
    data['sprunge'] = sys.stdin.read()

response = requests.post('http://sprunge.us', data)
print(response.content)
