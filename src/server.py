from flask import Flask, Response, jsonify

app = Flask("anton-code-test")

@app.route("/")
def hello_world():
    response = Response("hello world", status=200)
    return response

@app.route("/health")
def health_check():
    message = {"message": "healthy"}
    return jsonify(message)

if __name__ == "__main__":
    app.run(host="0.0.0.0")