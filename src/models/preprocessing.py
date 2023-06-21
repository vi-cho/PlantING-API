from sklearn.preprocessing import LabelEncoder
import pandas as pd

def preprocess_plants(plants):
    new_names = {
        'Tipo de material vegetal': 'type',
        'Cantidad de luz': 'light',
        'Agua requerida': 'water',
        'Radio máximo (en metros)': 'radius',
        'Altura máxima (en metros)': 'height',
        'Clima óptimo': 'climate',
        'Para cada categoría señale una opción entre poco/medio/mucho [Aporte de color]': 'color',
        'Para cada categoría señale una opción entre poco/medio/mucho [Atracción de abejas]': 'bees',
        'Para cada categoría señale una opción entre poco/medio/mucho [Atracción de mariposas]': 'butterfly',
        'Para cada categoría señale una opción entre poco/medio/mucho [Atracción de colibríes]': 'birds',
        'Para cada categoría señale una opción entre poco/medio/mucho [Aporte aromático]': 'aroma',
        'Para cada categoría señale una opción entre poco/medio/mucho [Nivel de cuidado]': 'care_intensity',
        'Hardiness Zone': 'zone',
    }
    drop_cols = [
        'Marca temporal',
        'Nombre en español',
        'Nombre científico',
        'Nativo de',
        'Caduco / Perenne',
        'Para cada evento eliga la época correspondiente [Siembra]',
        'Para cada evento eliga la época correspondiente [Floración]',
        'Para cada evento eliga la época correspondiente [Poda]',
        'Descripción',
        'Nombre(s) de especie(s) con la cual se viene bien',
        'Agua requerida mensual (en litros)'
    ]
    plants = plants.drop(drop_cols, axis=1)
    plants.rename(columns= new_names, inplace = True)

    mapeo = {
        'Zona 1A': 1,
        'Zona 1B': 2,
        'Zona 2A': 3,
        'Zona 2B': 4,
        'Zona 3A': 5,
        'Zona 3B': 6,
        'Zona 4A': 7,
        'Zona 4B': 8,
        'Zona 5A': 9,
        'Zona 5B': 10,
        'Zona 6A': 11,
        'Zona 6B': 12,
        'Zona 7A': 13,
        'Zona 7B': 14,
        'Zona 8A': 15,
        'Zona 8B': 16,
        'Zona 9A': 17,
        'Zona 9B': 18,
        'Zona 10A': 19,
        'Zona 10B': 20,
        'Zona 11A': 21,
    }
    plants['zone'] = plants['zone'].replace(mapeo)
    # plants['type'] = plants['type'].apply(lambda x: x.split(','))

    label_features = ['color', 'bees', 'butterfly', 'birds', 'aroma', 'care_intensity']
    label_encoder = LabelEncoder()
    plants['type'] = [[label_encoder.fit_transform([sublist]) for sublist in arr] for arr in plants['type']]
    plants['climate'] = label_encoder.fit_transform(plants['climate'])
    
    for feature in label_features:
        plants[feature] = plants[feature].apply(lambda x: ['Poco', 'Medio', 'Mucho'].index(x))
    return plants

