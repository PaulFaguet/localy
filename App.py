import pickle
from pydoc import describe
import streamlit as st
import pandas as pd
import numpy as np
import json

from Data.datasets import obtain_data
from Function.function import clean
from Function.app import modelbuild
from Function.app import make_prediction


df = obtain_data()
df = clean(df)
# print(df.info())

# Export model
model = modelbuild(df)
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)


# check if the checkbox is checked
# title of the checkbox is 'Show/Hide'


st.title("Localy, l'IA à votre service")
st.markdown("## Estimez votre loyer en quelques clics")
col1, col2, col3, col4 = st.columns([3, 2, 3, 2])

lyon_1 = ['69001', 45.7699, 4.8294]
lyon_2 = ['69002', 45.7608, 4.8357]
lyon_3 = ['69003', 45.7571, 4.8588]
lyon_4 = ['69004', 45.7797, 4.8205]
lyon_5 = ['69005', 45.7561, 4.8188]
lyon_6 = ['69006', 45.7751, 4.8502]
lyon_7 = ['69007', 45.7315, 4.8337]
lyon_8 = ['69008', 45.7365, 4.8694]
lyon_9 = ['69009', 45.7753, 4.8054]

geo_lyon = pd.DataFrame(data=[lyon_1, lyon_2, lyon_3, lyon_4,
                        lyon_5, lyon_6, lyon_7, lyon_8, lyon_9], columns=['arrondissement', 'lat', 'lon'])

df = pd.DataFrame(
    np.random.randn(1, 1) / [60, 60] + [45.7645, 4.8357],
    columns=['lat', 'lon'])


with st.sidebar:
    # change the background color of the sidebar

    st.sidebar.image('Images/logo_localy-removebg-preview.png', width=200)

    zone = st.selectbox(
        'Arrondissement',
        ('69001', '69002', '69003', '69004', '69005', '69006', '69007', '69008', '69009'))
    type = st.radio(
        "Type de logement",
        ('appartement', 'maison'))

    surface = st.slider(
        'Surface en m²',
        21, 164, (25, 75), 1)

    nb_piece = st.number_input('Nombre de pièce', 1, 4)

    button = st.button('ESTIMER')
    if button:
        try:
            result = make_prediction(
                list(surface), int(zone), type, str(nb_piece), './model.pkl')

            st.write(result)
        except:
            st.error('Votre recherche ne donne aucun résultat.')

st.map(geo_lyon[geo_lyon['arrondissement'] == zone],
       zoom=13.5)

# geojson = json.load(open('lyon_geojson.json', 'r'))
# geojson = geojson[0]["features"]["properties"]["geometry"]["coordinates"]
# fig = px.choropleth(df,
#    geojson=geojson,
#   locations='fips',
#  color='unemp',
# color_continuous_scale="Viridis",
# range_color=(0, 12),
# scope="usa",
# labels={'unemp': 'unemployment rate'}
# )
# fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
# fig.show()
