import pickle
import streamlit as st
import pandas as pd
import numpy as np
import math

from Data.datasets import obtain_data
from Function.function import clean
from Function.app_bis import modelbuild
from Function.app_bis import make_prediction

st.set_page_config(layout="wide", page_title="LOCALY", page_icon=":house:")

df = obtain_data()
df = clean(df)

model = modelbuild(df)
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)


st.title("LOCALY, l'IA à votre service")

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

tab1, tab2 = st.tabs(["Je suis futur locataire", "Je suis futur bailleur"])


col1, col2 = st.columns(2)

with col1:
    st.markdown('## Estimez votre loyer à Lyon',
                unsafe_allow_html=True)

    zone = st.selectbox(
        'Arrondissement',
        ('69001', '69002', '69003', '69004', '69005', '69006', '69007', '69008', '69009'))
    type = st.radio(
        "Type de logement",
        ('Appartement', 'Maison'))

    surface = st.slider(
        'Surface en m²',
        21, 164, (25, 75), 1)

    nb_piece = st.number_input('Nombre de pièce(s)', 1, 4)

    button = st.button('ESTIMER MON LOYER')
    if button:
        try:
            result = make_prediction(
                list(surface), int(zone), type.lower(), str(nb_piece), './model.pkl')

            st.success('Votre recherche donne des résultats.')

        except:
            st.error('Votre recherche ne donne aucun résultat.')

with col2:
    try:
        result_min = f'<span style="color: #7DCEA0;">{math.ceil(result[0])}€</span>'
        result_max = f'<span style="color: #F1948A;">{math.ceil(result[1])}€</span>'

        st.write(
            f'### Le loyer mensuel est estimé entre {result_min} et {result_max}', unsafe_allow_html=True)
    except:
        pass

    st.map(geo_lyon[geo_lyon['arrondissement'] == zone],
           zoom=13.5)

# geojson = json.load(open('lyon.json', 'r'))
# iterate over the coords and print the first 5
# for geo in geojson:
#     polygon = geo['features'][0]['geometry']['coordinates'][0]

#     fig = px.choropleth(df,
#                         geojson=geojson,
#                         locations=polygon,
#                         color_continuous_scale="Viridis",
#                         range_color=(0, 12),
#                         scope="europe"
#                         )
#     fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
#     fig.show()
