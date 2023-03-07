import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import AdaBoostClassifier


st.title('PREDICTIVE MAINTENANCE SYSTEM')
st.header('Domain : Aerospace')
st.subheader(' Solving the real world Businesss usecase of saving the revenue of organisation  by predicting the remaining useful lifespan of the jetengine using machine learning')
# import the model
st.subheader('Enter the values ')
ada = pickle.load(open('ada.pkl','rb'))
data = pickle.load(open('data.pkl','rb'))

# sensor 14
sensor_14 = int(st.number_input('enter the sensor_14 value'))

# sensor 3
sensor_3 = st.number_input('enter the sensor_3 value')
# sensor 9
sensor_9 = st.number_input('enter the sensor_9 value')

# sensor 7
sensor_7 = st.number_input('enter the sensor_7 value')

# sensor 11
sensor_11 = st.number_input('enter the sensor_11 value')

# sensor 21
sensor_21 = st.number_input('enter the sensor_21 value')

# sensor 15
sensor_15 = st.number_input('enter the sensor_15 value')

# sensor 12
sensor_12 = st.number_input('enter the sensor_12 value')
# sensor 4
sensor_4 = st.number_input('enter the sensor_4 value')


#if st.button('Predict RUL'):
    #columns = [sensor_14,sensor_3,sensor_9,sensor_7,sensor_11,sensor_21,sensor_15,sensor_12,sensor_4]
    #features = np.array(columns).reshape((len(columns), 1))
    ##final_features = [np.array(features)]
   # prediction = ada.predict(features)
    #output = round(prediction[0], 2)
    #st.title("The predicted price of this configuration is " + str(int(np.exp(ada.predict(output)[0]))))

if st.button('Predict Price'):
    query = np.array([sensor_14,sensor_3,sensor_9,sensor_7,sensor_11,sensor_21,sensor_15,sensor_12,sensor_4])
    query = query.reshape(1, 9)
    st.title("The Remaining Useful Life Is  " + str(int(ada.predict(query)[0])))

st.write("GitHuB Link [link](https://github.com/ApurvBhusari/Internship-Predictive-Maintenance)")