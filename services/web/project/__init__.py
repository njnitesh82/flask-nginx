from flask import Flask, jsonify, Response
import json
import time
from flask import request
import os
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(request.host)
    t1 = time.time()
    time.sleep(2)
    t2 = time.time()


    return Response(json.dumps({
        't1': str(t1),
        't2': str(t2),
        'duration':str(t2-t1),
        'pid':os.getpid()
    }), mimetype='application/json')