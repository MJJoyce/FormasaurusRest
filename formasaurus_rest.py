import json
import os

from flask import Flask
from formasaurus import FormExtractor
import lxml

app = Flask(__name__)

LEADER = "/tmp"

@app.route("/")
def hello():
    return "Hello!"

@app.route("/extract/<path:file_path>")
def extract_local_file_forms(file_path):
    # Open local file and extract forms
    # Format JSON and return
    pass

if __name__ == "__main__":
    app.run()
