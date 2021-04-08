from flask import Flask, Response

app = Flask("anton-code-test")

@app.route("/")
def hello_world():
    response = Response("hello world", status=200)
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0")