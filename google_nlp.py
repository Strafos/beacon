import googleapiclient.discovery

from geolocate import geolocate
import argparse
import json
import sys
import nlp
from entry import Entry
import states

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

file = open('testtweet.txt', 'r')

for line in file.readlines():
    result = analyze_entities(line, get_native_encoding_type())
    analyzed_tweet = json.dumps(result, indent=2)
    print(analyzed_tweet)
    print(line)
    address = nlp.find_Loc(analyzed_tweet, line)
    coordinates = geolocate(nlp.find_Loc(analyzed_tweet, line))
    new_entry = None
    if coordinates is not None:
        new_entry = Entry(coordinates[0], coordinates[1], address)