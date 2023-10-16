from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle
data = pd.read_csv('Cleaned Car.csv')
mod = pickle.load(open("model.pkl",'rb'))

app=Flask(__name__)


@app.route('/')
def index():
    companies=sorted(data['company'].unique())
    models=sorted(data['name'].unique())
    year=sorted(data['year'].unique())
    fueltypes=sorted(data['fuel_type'].unique())
    companies.insert(0,"Select Company")
    return render_template('index.html',companies=companies,models=models,year=year,fueltypes=fueltypes)

@app.route('/predict',methods=['POST'])
def predict():
    company = request.form.get('company')
    model = request.form.get('model')
    year = int(request.form.get('year'))
    fuel = request.form.get('fuel')
    kms = int(request.form.get('kilo'))

    prediction = mod.predict(pd.DataFrame([[model,company,year,kms,fuel]], columns=['name','company','year','kms_driven','fuel_type']))

    return str(np.round(prediction[0],2))


if __name__=="__main__":
    app.run(debug=True)