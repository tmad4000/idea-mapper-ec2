from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    print 'hello ran'
    app.run()


def blah(fun):
	def foo(a):
		print fun(a) + 1
	return foo

@blah
def plus(a):
	return a+1