
from flask import Flask
from mongokit import Connection, Document

# configuration
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017

# create the little application object
app = Flask(__name__)
app.config.from_object(__name__)

# connect to the database
connection = Connection(app.config['MONGODB_HOST'],
                        app.config['MONGODB_PORT'])


collection = connection['test'].Ideas

def add_idea(doc):
  try:
    doc.title
    doc.description
    doc.status
    doc.votes
    doc.creator
    doc.relatedIdeas
    doc.timestamp
  except NameError:
     return False


  collection.insert(doc)

  return True;


def list_ideas():
  return list(collection.find())

  '''
  if not doc.title && not doc.description:
    titleDesc=extractIdeaNameDesc(doc.text)
    doc.title=titleDesc[0]
    doc.description=titleDesc[1]


  if not doc.status:
    doc.status=0

  if not doc.votes:
    doc.votes=0
    
  if not doc.creator:
    doc.creator='anon'

  if not doc.relatedIdeas:
    doc.relatedIdeas=[]
  if not doc.timestamp:
      doc.timestamp = new Date

  return Ideas.insert(doc);
  '''
        
'''
from app import connection
from app import User
collection = connection['test'].users
user = collection.User()
user['name'] = u'admin'
user['email'] = u'admin@localhost'
user.save()
'''




def max_length(length):
    def validate(value):
        if len(value) <= length:
            return True
        raise Exception('%s must be at most %s characters long' % length)
    return validate

class User(Document):
    structure = {
        'name': unicode,
        'email': unicode,
    }
    validators = {
        'name': max_length(50),
        'email': max_length(120)
    }
    use_dot_notation = True
    def __repr__(self):
        return '<User %r>' % (self.name)

# register the User document with our current connection
#connection.register([User])
