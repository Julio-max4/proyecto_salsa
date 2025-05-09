from flask import Flask, render_template, jsonify
import pandas as pd
import random
import webbrowser
from threading import Timer
import os  # <-- NEW

app = Flask(__name__)

tabla_incial=pd.read_csv("Pasos_salsa.csv", encoding="utf-8")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_random_value')
def get_random_value():
    random_row = tabla_incial.sample(n=1).iloc[0]
    return jsonify({
        'valores': str(random_row['steps']),
        'difficulty': str(random_row['Conteo']),  # assuming you have this column
        'count': str(random_row['Simetria']),            # assuming you have this column
        'type': str(random_row['Tiempo']),              # assuming you have this column
        'message': "Paso a realizar"
    })
def open_browser():
    if not os.environ.get("WERKZEUG_RUN_MAIN"):  # <-- FIX HERE
        webbrowser.open_new('http://127.0.0.1:5000')

if __name__ == '__main__':
    Timer(1, open_browser).start()
    app.run(debug=True) 