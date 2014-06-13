#!/usr/bin/env python

import calendar
import datetime

from flask import Flask, jsonify
from flask.ext.cache import Cache
from scraper import scrape


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})
# app.debug = True


def now_timestamp():
    now_tt = datetime.datetime.utctimetuple(datetime.datetime.utcnow())
    return calendar.timegm(now_tt)


# TODO: Cache this function or the /api route? Going with the route for now
# @cache.cached(timeout=10, key_prefix='data')
def get_data():
    data = scrape()
    data['last_updated'] = now_timestamp()
    return data


@app.route('/')
def hello():
    return 'Hello World (Cup)!'


@app.route("/api")
@cache.cached(timeout=10)
def api():
    return jsonify(get_data())


if __name__ == "__main__":
    app.run()
