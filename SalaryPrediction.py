import pickle
import streamlit as st

pickle_in=open("salaryprediction.pkl",'rb')
model=pickle.load(pickle_in)

e=st.number_input("Enter the experince")
if st.button("PREDICT"):
  s=model.predict([[e]]).squeeze()
  st.succces(f'Salary is {s}')