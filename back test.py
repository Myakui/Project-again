from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder='C:/Users/yakov/Vscode Projects/PhonoText/dist/assets')

@app.route('/')
def serve_static():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(port=8080)
