from flask import Flask, Response, stream_with_context
import time
import itertools

app = Flask(__name__)


@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def all_get(path):
    return Response(stream_with_context(events()), content_type='text/event-stream')


def events():
    for i, c in enumerate(itertools.cycle('\|/-')):
        yield "Not Found \n"
        time.sleep(5)

# app.run(ssl_context='adhoc')
