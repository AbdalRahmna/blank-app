import pickle
import streamlit as st
import pandas as pd


#    ====== Upload the Data =======
Data=pickle.load(open("logistic.sav","rb"))

#   ====== Create the App ========

st.title("Diabetes prediction Web App")
st.info("Easy Application For Diabetest prediction Disease")
#      ===  inputs      ===

Pregnancies=st.text_input("Pregnancies")
Glucose=st.text_input("Glucose")
BloodPressure=st.text_input("BloodPressure")
SkinThickness=st.text_input("SkinThickness")
Insulin=st.text_input("Insulin")
BMI=st.text_input("BMI")
DiabetesPedigreeFunction=st.text_input("DiabetesPedigreeFunction")
Age=st.text_input("Age")

#    ====Side bar ====
st.sidebar.header('Feature Selection')

df=pd.DataFrame({
    "Pregnancies":[Pregnancies],
    "Glucose":[Glucose],
    "BloodPressure":[BloodPressure],
    "SkinThickness":[SkinThickness],
    "Insulin":[Insulin],
    "BMI":[BMI],
    "DiabetesPedigreeFunction":[DiabetesPedigreeFunction],
    "Age":[Age]},
     index=[0])
con=st.sidebar.button('confirm')
if con:
    result=Data.predict(df)
    if result==0:
       st.sidebar.write("the paient is clear")
       st.sidebar.image("https://media.istockphoto.com/id/1641151865/photo/keto-food-for-ketogenic-and-cholesteral-diet-healthy-nutritional-eating-lifestyle-for-good.jpg?s=612x612&w=0&k=20&c=bNZ9sjF9U00B2O2pw1zHSop4oVLH0eCAlLDV6QeSrMk=",width=250)
    else:
       st.sidebar.write("the paient has disease")
       st.sidebar.image("https://media.istockphoto.com/id/650343892/photo/type-1-diabetes-concept-suggested-by-insulin-syringe.jpg?s=612x612&w=0&k=20&c=GBpUDwkUgMHcynf98Rt3SYOXd-kdkEq2shASnNWIGUo=",width=250)   

