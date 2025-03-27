# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 17:07:46 2025

@author: USER
"""

import os
import subprocess

# 確保 Flask 已安裝
try:
    import flask
except ImportError:
    subprocess.run(["pip", "install", "Flask"])
    import flask

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
