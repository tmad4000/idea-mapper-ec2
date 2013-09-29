from flask import Flask, request, abort
from mongokit import Connection, Document

import json


from idea_mapper import * #comment out for speed of testing
import db_inf 


app = Flask(__name__)

@app.route('/')
def find_related():
    q=request.args.get('query')
    if q==None:
        q=''

    print 'find related to: '' + q +'''
    return json.dumps(getRelatedIdeas(q)) #comment out for speed of testing
    return 'eue'



@app.route('/api')
def api():
    request_type = request.args.get('type')
    request_data = request.args.get('data')
    if not request_type: abort(400)
    if request_type == u'create': #hack
        if not request_data: print 'the world is exploding'
        print 'create', request_data
        return add_idea(json.loads(request_data))
    if request_type == u'read': #hack
        if not request_data: print 'the world is exploding'
        return json.dumps(list_ideas())
    elif request_type == u'delete': #hack
        if not request_data: print 'the world is exploding'
        #TODO
        #perform delete logic
    elif request_type == u'update': #hack
        if not request_data: print 'the world is exploding'
        #TODO
        #perform update logic


if __name__ == '__main__':
    print 'start'

    #print getRelatedIdeas('food')
    app.run(debug=True, host='0.0.0.0')
    #print getRelatedIdeas('eeg scrolling')
    #printRelatedIdeas('eeg scrolling')
