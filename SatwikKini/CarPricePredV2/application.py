from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle
data = pd.read_csv('newData.csv')
mod = pickle.load(open("model2.pkl",'rb'))

app=Flask(__name__)


@app.route('/')
def index():
    models=sorted(data['Name'].unique())
    year=sorted(data['Year'].unique())
    fueltypes=sorted(data['Fuel_Type'].unique())
    ownertypes=(data['Owner_Type'].unique())
    return render_template('index.html',models=models,year=year,fueltypes=fueltypes,ownertypes=ownertypes)

@app.route('/predict',methods=['POST'])
def predict():
    model = request.form.get('model')
    year = (request.form.get('year'))
    fuel = request.form.get('fuel')
    own = request.form.get('own')
    kms = (request.form.get('kilo'))

    prediction = mod.predict(pd.DataFrame([[model,own,fuel,year,kms]], columns=['Name','Owner_Type','Fuel_Type','Year','Kilometers_Driven']))

    return str(np.round(prediction[0],2))


if __name__=="__main__":
    app.run(debug=True)