#!/usr/bin/env python

import calendar
import datetime

from flask import Flask, jsonify
from scraper import scrape


app = Flask(__name__)
app.debug = True


@app.route('/')
def hello():
    return 'Hello World!'

@app.route("/api")
def api():
    data = scrape()
    now = datetime.datetime.utctimetuple(datetime.datetime.utcnow())
    data['last_updated'] = calendar.timegm(now)
    return jsonify(data)


if __name__ == "__main__":
    app.run()
