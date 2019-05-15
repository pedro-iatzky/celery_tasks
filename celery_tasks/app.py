"""
    Flask API, each endpoint can expose one or more tasks
"""

import logging

from flask import Flask, request, jsonify

from celery_tasks.tasks import naive_test, write_to_file
from celery_tasks.util import PORT

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello_world():
    print(app.name)
    naive_test.apply_async(countdown=5)
    return "Hello there!!"


@app.route("/write", methods=["POST"])
def write_to_disk():
    write_to_file.apply_async(countdown=5)
    return "Hello there!!"


@app.route("/logger", methods=["POST"])
def log_messages():
    """Since the celery tasks will run in isolated workers, we want to centralize
        the logging. Then, each task could send the logs to this endpoint, if
        needed, in order to print the desired information to the API stdout"""
    json_data = request.get_json()
    if json_data.get("type", "") == 'ERROR':
        message = json_data.get("message", "")
        logging.error(message)
    return jsonify({"msg": "OK"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
