from flask import Flask, Response, jsonify
import os

app = Flask("anton-code-test")


@app.route("/")
def hello_world():
    hello_world_response = Response("hello world", status=200)
    return hello_world_response


@app.route("/health")
def health_check():
    health_check_message = {"message": "healthy"}
    return jsonify(health_check_message)


@app.route("/metadata")
def get_application_metadata():
    metadata_message = {
        "version": "1.0.0",
        "description": "very basic flask app",
        "lastcommitsha": os.environ.get("COMMIT_SHA"),
    }
    return jsonify(metadata_message)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
