import pandas as pd

# Chargement des données


def obtain_data():
    db = pd.read_csv("Data/Base_OP_FIN.csv",
                     encoding='ISO-8859-1', sep=';')
    return db
