from flask import Flask, request
from mongokit import Connection, Document

import json


from idea_mapper import * #comment out for speed of testing
import db_inf 


app = Flask(__name__)

@app.route("/")
def find_related():
	q=request.args.get("query")
	
	if q==None:
		q=''

	print "find related to: '" + q +"'"
	
	return json.dumps(getRelatedIdeas(q)) #comment out for speed of testing
	return 'eue'



@app.route("/add")
def add():
    print "adding idea"
    return json.dumps((request.args.to_dict()))
    #return db_inf.add_idea()
    #return add_idea(request.args.get("query")))


if __name__ == '__main__':
	print 'start'

#	print getRelatedIdeas("food")
	app.run(debug=True, host='0.0.0.0')
	#print getRelatedIdeas('eeg scrolling')
	#printRelatedIdeas('eeg scrolling')
