from flask import Flask, request

app = Flask(__name__)
@app.route("/",methods=('GET','POST'))
def hello_world():
    if request.method == "GET":
        data = request.args
    return app.response_class(str(data), mimetype="text/json")

if __name__ == "__main__":
    app.run(port=(8088))