# importation des lib
import pickle
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OneHotEncoder

# create fonction

def modelbuild(df):
  # Creation de champs a prédire et les paramètre
  target = "moyenne_loyer_mensuel"
  feature = ["zone", "type_habitat", "nombre_piece", "surface_moyenne"]
  X_train = df[feature]
  y_train = df[target]

  # Creation de model et le build
  model = make_pipeline(
      OneHotEncoder(),
      SimpleImputer(),
      Ridge()
  )

  model.fit(X_train, y_train)
  return model

def make_prediction(area, zone, typehab, nobs, model_filepath):
  dat = []
  for surface in area:
    if surface != '':
      data = {
          "zone" : zone,
          "type_habitat": typehab,
          "nombre_piece": nobs,
          "surface_moyenne": surface,
      }
      dat.append(data)
  df = pd.DataFrame.from_dict(dat)
  print(df)
  with open(model_filepath, 'rb') as f:
    model = pickle.load(f)
  df.dropna()
  prediction = model.predict(df).round(2)
  return prediction