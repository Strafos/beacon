import googleapiclient.discovery

from geolocate import geolocate
import argparse
import json
import sys
import nlp
from entry import Entry
import info

def analyze_entities(text, encoding='UTF32'):
    body = {
        'document': {
            'type': 'PLAIN_TEXT',
            'content': text,
        },
        'encoding_type': encoding,
    }

    service = googleapiclient.discovery.build('language', 'v1')

    request = service.documents().analyzeEntities(body=body)
    response = request.execute()

    return response

def get_native_encoding_type():
    """Returns the encoding type that matches Python's native strings."""
    if sys.maxunicode == 65535:
        return 'UTF16'
    else:
        return 'UTF32'

def enter_coord(line):
    result = analyze_entities(line, get_native_encoding_type())
    analyzed_tweet = json.dumps(result, indent=2)
    # print(analyzed_tweet)
    # print(line)
    address = nlp.find_Loc(analyzed_tweet, line)
    coordinates = geolocate(nlp.find_Loc(analyzed_tweet, line))
    new_entry = None
    if coordinates is not None:
        total_loc = address + '\t' + str(coordinates[0]) + ', ' + str(coordinates[1]) + '\n'
        g.write(total_loc)
        new_entry = Entry(coordinates[0], coordinates[1], address)

g = open('coordinates.txt', 'w')
f = open('first_filter.txt', 'r')
for i in f.readlines():
    enter_coord(i)