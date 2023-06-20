import streamlit as stream
import requests


stream.title("Student Performance Predictor")
stream.write("Predict if a student will perform well. ")

url = "http://localhost:5000/"

columns = {
    'school': "string", 'sex': "string", 'age': "int", 'address': "string", 'famsize': "string",
    'Pstatus': "string", 'Medu': "int", 'Fedu': "int",
    'Mjob': "string", 'Fjob': "string", 'reason': "string", 'guardian': "string",
    'traveltime': "int", 'studytime': "int", 'failures': "int", 'schoolsup': "string",
    'famsup': "string", 'paid': "string", 'activities': "string", 'nursery': "string",
    'higher': "string", 'internet': "string", 'romantic': "string", 'famrel': "int",
    'freetime': "int", 'goout': "int", 'Dalc': "int",
    'Walc': "int", 'health': "int", 'absences': "int", 'G1': "int", 'G2': "int", 'G3': "int"
}

vals = []

for c in columns.keys():
    if columns[c] == "string":
        v = stream.text_input(f"Enter value for {c}")
        vals.append(v)
    else:
        v = stream.number_input(f"Enter value for {c}")
        vals.append(v)
predict = stream.button("Predict")
if predict:
    try:
        string_input = ",".join([f"{x}:{y}" for x,y in list(zip(columns.keys(), vals))])
        res = requests.post(f"{url}/{string_input}")

        if res.status_code == 200:
            text = res.json().get("response")
            stream.write(text)
        else:
            stream.error("Error connecting to API")
    except Exception:
        print("Error!")