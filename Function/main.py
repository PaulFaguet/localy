# Application principal charge les fonctions
# docs.streamlit.io sur google
# streamlit run main.py

import pandas as pd
import streamlit as st
import pickle

from Data.datasets import obtain_data
from Function.function import clean
from Function.app_bis import modelbuild
from Function.app_bis import make_prediction


df = obtain_data()
df = clean(df)
print(df.info())

# Export model
model = modelbuild(df)
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)


test = make_prediction([44, 100], 69002, 'appartement', '3', './model.pkl')
print(test)
