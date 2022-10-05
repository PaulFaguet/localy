import pandas as pd

# Chargement des données


def obtain_data():
    db = pd.read_csv(r"/Users/paulfaguet/Desktop/localy/Data/Base_OP_FIN.csv",
                     encoding='ISO-8859-1', sep=';')
    return db
