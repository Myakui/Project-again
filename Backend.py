from flask import Flask, request
from Solution1 import scenario1  # Импортируем функцию из другого файла

app = Flask(__name__)
@app.route("/",methods=('GET','POST'))
def hello_world():
    if request.method == "GET":
        data = request.args
        # Вызываем функцию для вывода чего-то
        response_data = scenario1()
    return app.response_class(str(response_data), mimetype="text/json")

if __name__ == "__main__":
    app.run(port=(8088))