from flask import Flask, Response, stream_with_context
import time
import itertools
import os

app = Flask(__name__)
interval = os.environ['INTERVAL']
message = os.environ['MESSAGE']
try:
    interval = int(interval)
except ValueError:
    print('ERROR - INTERVAL has to be an integer')
    exit(1)


@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def all_get(path):
    return Response(stream_with_context(events()), content_type='text/event-stream')


def events():
    for i, c in enumerate(itertools.cycle('\|/-')):
        yield message + ' \n'
        time.sleep(interval)
