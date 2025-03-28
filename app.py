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

# 設定存放 PDF 的資料夾
PDF_FOLDER = os.path.join(os.getcwd(), "static", "pdf")
os.makedirs(PDF_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return '''
    <h1>PDF Viewer</h1>
    <p><a href="/view-pdf/sample.pdf">點擊這裡查看 PDF</a></p>
    <p><a href="/download-pdf/sample.pdf">點擊這裡下載 PDF</a></p>
    '''

# 提供 PDF 預覽
@app.route('/view-pdf/<filename>')
def view_pdf(filename):
    return send_from_directory(PDF_FOLDER, filename)

# 提供 PDF 下載
@app.route('/download-pdf/<filename>')
def download_pdf(filename):
    return send_from_directory(PDF_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
