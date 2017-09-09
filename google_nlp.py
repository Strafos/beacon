import googleapiclient.discovery

import argparse
import json
import sys
import nlp
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

file = open('tweets2.txt', 'r')

for line in file.readlines():
    result = analyze_entities(line, get_native_encoding_type())
    analyzed_tweet = json.dumps(result, indent=2)
    nlp.find_Loc(analyzed_tweet, line)