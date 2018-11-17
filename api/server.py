from flask import Flask, request
from flask_cors import CORS, cross_origin
from gevent.pywsgi import WSGIServer
from sklearn.externals import joblib
import json
import numpy as np

app = Flask(__name__)
CORS(app)

@app.route('/')
def test():
    return "Hello World!"

@app.route('/classify', methods=['POST'])
def classify():
    sentence = [request.form['sentence']]
    res = np.asscalar(pipeline.predict(sentence))
    print("processing {}, labeled as {}".format(sentence, res))
    return json.dumps({"label": res})

if __name__ == '__main__':
    pipeline = joblib.load('model.pkl')
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
