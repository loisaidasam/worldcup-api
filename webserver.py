#!/usr/bin/env python

from flask import Flask, jsonify
from scraper import scrape


app = Flask(__name__)
app.debug = True


@app.route("/api")
def api():
    return jsonify(scrape())
    #return jsonify({'foo': 'bar'})


if __name__ == "__main__":
    app.run()
