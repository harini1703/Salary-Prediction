import pickle
import streamlit as st

pickle_in=open("salaryprediction.pkl",'rb')
model=pickle.load(pickle_in)
st.header("Salary and Experince Prediction")
e=st.number_input("Enter the experince:")
if st.button("PREDICT"):
  s=model.predict([[e]]).squeeze()
  s=int(s)
  st.success(f'Salary is {s}')
