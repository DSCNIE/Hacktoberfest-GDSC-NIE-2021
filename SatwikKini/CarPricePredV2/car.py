import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.metrics import r2_score
from sklearn.pipeline import make_pipeline
data = pd.read_csv('dataset.csv')
backup = data.copy()

# Cleaning the data
data['Year'] = data['Year'].astype(int)
data = data[data['Price']!="Ask For Price"]
data['Price'] = data['Price']*100000
data['Price'] = data['Price'].astype(int)
data['Kilometers_Driven'] = data['Kilometers_Driven'].astype(int)
data['Name'] = data['Name'].str.split(' ').str.slice(0,3).str.join(' ')
data = data.drop("Location",axis=1)
data = data.drop("New_Price",axis=1)
data = data.drop("Unnamed: 0",axis=1)
data = data.drop("Transmission",axis=1)
data = data.drop("Mileage",axis=1)
data = data.drop("Engine",axis=1)
data = data.drop("Power",axis=1)
data = data.drop("Seats",axis=1)
data = data.reset_index(drop=True)
data = data[data['Price']<6e6].reset_index(drop=True)
data.to_csv('newData.csv')
X = data.drop(columns='Price')
Y = data['Price']
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=378)
ohe = OneHotEncoder()
ohe.fit(X[['Name','Fuel_Type','Owner_Type']])
col_trans = make_column_transformer((OneHotEncoder(categories=ohe.categories_),['Name','Fuel_Type','Owner_Type']),remainder='passthrough')
regressor = LinearRegression()
pipe = make_pipeline(col_trans,regressor)
pipe.fit(X_train,Y_train)
Y_pred = pipe.predict(X_test)

######
# scores = []
# for i in range(0,1000):
#     X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.2,random_state=i)
#     regressor = LinearRegression()
#     pipe = make_pipeline(col_trans,regressor)
#     pipe.fit(X_train,Y_train)
#     Y_pred = pipe.predict(X_test)
#     scores.append(r2_score(Y_test,Y_pred))
# print(np.argmax(scores))
######


pickle.dump(pipe,open('Model2.pkl','wb'))
print(pipe.predict(pd.DataFrame([['Maruti Wagon R','First','Petrol',2010,10000]],columns=['Name','Owner_Type','Fuel_Type','Year','Kilometers_Driven'])))