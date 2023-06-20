import os
from flask import Flask
from flask_restful import  Resource, Api
import pickle
import pandas as pd
import numpy as np

model = pickle.loads(open("rf_model.pkl", "rb"))

app = Flask(__name__)
api = Api(app)

class Predict(Resource):

    def get(self, data):
        return "Random Forest Model API"
    
    def post(self, data):
        lst = data.split(",")
        names = [x.split(":")[0] for x in lst]
        vals = [int(x.split(":")[-1]) if x.isdigit() else x.split(":")[-1] for x in lst]
        encoders = {}
        ##encoding
        for f in os.listdir():
            if "pkl" in f and "model" not in f:
                enc = pickle.load(open(f, "rb"))
                encoders[f.split(".")[0]] = enc
            else:
                continue

        arr = []
        for n,x in list(zip(names, vals)):
            if n in encoders.keys():
                v = encoders[n].transform([x])
                arr.append(v[0])
            else:
                arr.append(x)

        #predicting
        arr = np.array(arr).reshape(-1,1)
        pred = model.predict(arr)
        if pred[0] >= 10.0:
            text = "This student will perform well in the next session"
        else:
            text = "This student will perform bad in the next session, \
                academic advice is to monitor progress and establish improvement schemes"
        return {"response": text}, 200
    


api.add_resource(Predict, "/predict/<data>")


if __name__ == "__main__":
    app.run(debug=True)