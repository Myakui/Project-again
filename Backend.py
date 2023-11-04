from flask import Flask, request
from flask_cors import CORS  # Импортируем CORS
from Solution2 import scenario1
import json

app = Flask(__name__)
CORS(app)  # Настройка CORS

@app.route("/", methods=['GET', 'POST'])
def hello_world():
    if request.method == "GET":
        data = request.args
        # Вызываем функцию для вывода чего-то
        response_data = scenario1()
    return app.response_class(json.dumps(response_data), mimetype="text/json")

if __name__ == "__main__":
    app.run(port=8088)
