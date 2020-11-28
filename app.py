
import pandas as pd
from flask import Flask, render_template, request
import csv
import os

app = Flask(__name__)

df=pd.read_csv('merged_cardio_train_sample.csv')

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/sampledata')
def sampledata():
    return render_template('sampledata.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

@app.route('/info')
def info():
        return render_template('info.html')

@app.route('/model')
def model():
        return render_template('model.html')


if __name__ == "__main__":
    app.run()