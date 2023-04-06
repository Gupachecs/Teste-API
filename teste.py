from flask import Flask
from flask import request

app = Flask(__name__)
print(__name__)
@app.route("/teste")
def index():
    x=request.args.get("parametro")
    return "<h1>Hello world</h1> %s" % (x)


app.run(host='0.0.0.0', port=81)
