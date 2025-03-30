# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 17:07:46 2025

@author: USER
"""

import os
import subprocess
from flask import Flask, send_from_directory, render_template

# 確保 Flask 已安裝
try:
    import flask
except ImportError:
    subprocess.run(["pip", "install", "Flask"])
    import flask

app = Flask(__name__)

# GitHub raw PDF URL
GITHUB_PDF_URL = "https://github.com/Jim-Yang98/my-sideproject/raw/main/RFM.pdf"

@app.route('/')
def home():
    return f'''
    <h1>PDF 內容</h1>
    <iframe src="{GITHUB_PDF_URL}" width="800" height="600"></iframe>
    '''

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
