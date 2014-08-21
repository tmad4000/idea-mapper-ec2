from flask import Flask, request, abort
from mongokit import Connection, Document

import urllib
import json


from idea_mapper import * #comment out for speed of testing
import db_inf 

import sys
reload(sys)
sys.setdefaultencoding("utf-8")


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

@app.route('/ui')
def ui():
    q=request.args.get('query')
    if q==None:
        q=''


    b='<h1>Has your idea been done before?</h1><br><form method="get"><input type="text" name="query" value="'+q+'" style="width:400px"><input type="submit"></form><br>'

    print 'find related to: '' + q +'''    
    lRay=getRelatedIdeas(q)

    l = ['<li><div style="">'+i[0]+' <div style="color:orange">' +str(i[1])+'</div></li>\n' for i in lRay]

    return b + '\n<ul>'+''.join(l)+'</ul>'

# add ability to confirm/deny connections and add new ideas
@app.route('/ui2')
def ui2():
    q=request.args.get('query')
    if q==None:
        q=''

    b='<h1>Has your idea been done before?</h1><br><form method="get"><input type="text" name="query" value="'+q+'" style="width:400px"><input type="submit"></form><br>'

    print 'find related to: '' + q +'''    
    lRay=getRelatedIdeas(q)
    
    l = ['<li><div style=""><a href="?'+urllib.urlencode({'query' : i[0]})+'">'+i[0]+' </a><div style="color:orange">' +str(i[1])+'</div></li>\n' for i in lRay]

    return b + '\n<ul>'+''.join(l)+'</ul>'

if __name__ == '__main__':
    print 'start'

    #print getRelatedIdeas('food')
    app.run(debug=True, threaded=True, host='0.0.0.0') # DEBUG: remove threaded=True from prod
    #print getRelatedIdeas('eeg scrolling')
    #printRelatedIdeas('eeg scrolling')
