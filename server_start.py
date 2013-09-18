from flask import Flask, request
from mongokit import Connection, Document

import json

from idea_mapper import *


app = Flask(__name__)

@app.route("/")
def hello():
    print "in the route"
    return json.dumps(getRelatedIdeas(request.args.get("query")))

if __name__ == '__main__':
	print 'start'
	print getRelatedIdeas("food")
	app.run(host='0.0.0.0')
	#print getRelatedIdeas('eeg scrolling')
	#printRelatedIdeas('eeg scrolling')