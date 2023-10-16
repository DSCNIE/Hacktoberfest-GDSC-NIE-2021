import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.metrics import r2_score
from sklearn.pipeline import make_pipeline
data = pd.read_csv('car.csv')
backup = data.copy()

# Cleaning the data
data = data[data['year'].str.isnumeric()]
data['year'] = data['year'].astype(int)
data = data[data['Price']!="Ask For Price"]
data['Price'] = data['Price'].str.replace(',','')
data['Price'] = data['Price'].astype(int)
data['kms_driven'] = data['kms_driven'].str.split(' ').str.get(0).str.replace(',','')
data = data[data['kms_driven'].str.isnumeric()]
data['kms_driven'] = data['kms_driven'].astype(int)
data = data[~data['fuel_type'].isna()]
data['name'] = data['name'].str.split(' ').str.slice(0,3).str.join(' ')
data = data.reset_index(drop=True)
data = data[data['Price']<6e6].reset_index(drop=True)
data.to_csv('Cleaned Car.csv')
X = data.drop(columns='Price')
Y = data['Price']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=661)
ohe = OneHotEncoder()
ohe.fit(X[['name','company','fuel_type']])
col_trans = make_column_transformer((OneHotEncoder(categories=ohe.categories_),['name','company','fuel_type']),remainder='passthrough')
regressor = LinearRegression()
pipe = make_pipeline(col_trans,regressor)
pipe.fit(X_train,Y_train)
Y_pred = pipe.predict(X_test)
#pickle.dump(pipe,open('Model.pkl','wb'))
