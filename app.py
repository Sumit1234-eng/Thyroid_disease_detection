#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('random_forest_classifier_model.pkl', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = int(request.form['age'])
        TSH = float(request.form['TSH'])
        T3 = float(request.form['T3'])
        TT4 = float(request.form['TT4'])
        T4U = float(request.form['T4U'])
        FTI = float(request.form['FTI'])
        sex = request.form['sex']
        if (sex == 'Male'):
            sex = 1
        else:
            sex = 0
        on_thyroxine = request.form['on_thyroxine']
        if (on_thyroxine == 'False'):
            on_thyroxine = 1
        else:
            on_thyroxine = 0

        on_antithyroid_medication = request.form['on_antithyroid_medication']
        if (on_antithyroid_medication == 'False'):
            on_antithyroid_medication = 1
        else:
            on_antithyroid_medication = 0

        thyroid_surgery = request.form['thyroid_surgery']
        if (thyroid_surgery == 'False'):
            thyroid_surgery = 1
        else:
            thyroid_surgery = 0

        query_hypothyroid = request.form['query_hypothyroid']
        if (query_hypothyroid == 'False'):
            query_hypothyroid = 1
        else:
            query_hypothyroid = 0

        query_hyperthyroid = request.form['query_hyperthyroid']
        if (query_hyperthyroid == 'False'):
            query_hyperthyroid = 1
        else:
            query_hyperthyroid = 0

        sick = request.form['sick']
        if (sick == 'False'):
            sick = 1
        else:
            sick = 0
        prediction = model.predict([[age, TSH, T3, TT4, T4U, FTI, sex, on_thyroxine, on_antithyroid_medication,
                                     thyroid_surgery, query_hypothyroid, query_hyperthyroid, sick]])

        output = prediction
        if output == 0:
            return render_template('index.html', prediction_texts="the person is suffering from {}".format('thyroid'))
        else:
            return render_template('index.html', prediction_text="the person is not suffering from {}".format('thyroid'))
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

