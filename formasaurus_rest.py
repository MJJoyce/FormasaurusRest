import json
import os

from flask import Flask
from formasaurus import FormExtractor
import lxml

app = Flask(__name__)
ex = FormExtractor.load()

LEADER = "/tmp"

@app.route("/")
def hello():
    return "Hello!"

@app.route("/extract/<path:file_path>")
def extract_local_file_forms(file_path):
    full_path = os.path.join(LEADER, file_path)
    tree = lxml.html.parse(full_path)
    forms = ex.extract_forms(tree)
    forms = [
        (lxml.etree.tostring(form[0]), form[1], tree.getpath(form[0]))
        for form in forms
    ]
    return json.dumps(forms)

if __name__ == "__main__":
    app.run()
