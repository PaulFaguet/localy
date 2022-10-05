import pandas as pd

def clean(db) :
    db = db.rename(columns={'nombre_pièces' : "nombre_piece"})
    db['loyer_moyen'] = pd.to_numeric(db['loyer_moyen'], errors = 'coerce')
    db.fillna(value= {
        'loyer_moyen' : db['loyer_moyen'].median(),
        'moyenne_loyer_mensuel' : db['moyenne_loyer_mensuel'].median(),
        'surface_moyenne' : db['surface_moyenne'].median(),
        'nombre_observations' : db['nombre_observations'].median()}, inplace = True)
    return db

