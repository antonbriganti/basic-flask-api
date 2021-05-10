from flask import Flask, Response, jsonify
import os

app = Flask("anton-code-test")

@app.route("/")
def hello_world():
    response = Response("hello world", status=200)
    return response

@app.route("/health")
def health_check():
    message = {"message": "healthy"}
    return jsonify(message)

@app.route("/metadata")
def metadata_endpoint():
    metadata = {"version": "1.0.0", "description": "very basic flask app", "lastcommitsha": os.environ.get('COMMIT_SHA') }
    return jsonify(metadata)

if __name__ == "__main__":
    app.run(host="0.0.0.0")