#!/usr/bin/env python3
import os
from flask import Flask, jsonify
from fundamentus import get_data
from datetime import datetime

app = Flask(__name__)

dia = datetime.strftime(datetime.today(), '%d')
lista = get_data()

@app.route("/")
def json_api():
    global lista, dia
    
    if dia == datetime.strftime(datetime.today(), '%d'):
        return jsonify(lista)
    else:
        dia = datetime.strftime(datetime.today(), '%d')
        lista = lista = get_data()
        return jsonify(lista)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host='0.0.0.0', port=port)