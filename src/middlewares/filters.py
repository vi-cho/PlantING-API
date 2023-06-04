import pandas as pd
import sys
sys.path.insert(1, '/home/yosokosu-mint/Documents/proyecto_innova/backend/PlantING-API/src/models')
from preprocessing import preprocess_plants

def basic_filter(data, db_filename):
    db = pd.read_csv(f'{db_filename}_final.csv')
    db['Tipo de material vegetal'] = db['Tipo de material vegetal'].apply(lambda x: x.split(','))
    db = db[
        (db['Agua requerida'] <= data['Agua disponible']) &
        (db['Cantidad de luz'] <= data['Cantidad de luz']) &
        (db['Tipo de material vegetal'].apply(lambda x: any(item in x for item in data['Material vegetal']))) &
        (db['Hardiness Zone'] >= data['Hardiness Zone'])
    ]
    return db

def water_priority(data, db_filename):
    db = basic_filter(data, db_filename)
    db_new = preprocess_plants(db)
    best = db[db_new['water'] == 0]
    mid = db[db_new['water'] == 1]
    worst = db[db_new['water'] == 2]
    res = pd.concat([best,mid,worst])
    return res

def color_priority(data, db_filename):
    db = basic_filter(data, db_filename)
    db_new = preprocess_plants(db)
    best = db[db_new['color'] == 0]
    mid = db[db_new['color'] == 1]
    worst = db[db_new['color'] == 2]
    res = pd.concat([best,mid,worst])
    return res

def bee_priority(data, db_filename):
    db = basic_filter(data, db_filename)
    db_new = preprocess_plants(db)
    best = db[db_new['bees'] == 0]
    mid = db[db_new['bees'] == 1]
    worst = db[db_new['bees'] == 2]
    res = pd.concat([best,mid,worst])
    return res

def bird_priority(data, db_filename):
    db = basic_filter(data, db_filename)
    db_new = preprocess_plants(db)
    best = db[db_new['birds'] == 0]
    mid = db[db_new['birds'] == 1]
    worst = db[db_new['birds'] == 2]
    res = pd.concat([best,mid,worst])
    return res

def aroma_priority(data, db_filename):
    db = basic_filter(data, db_filename)
    db_new = preprocess_plants(db)
    best = db[db_new['aroma'] == 0]
    mid = db[db_new['aroma'] == 1]
    worst = db[db_new['aroma'] == 2]
    res = pd.concat([best,mid,worst])
    return res

def care_priority(data, db_filename):
    db = basic_filter(data, db_filename)
    db_new = preprocess_plants(db)
    best = db[db_new['care_intensity'] == 0]
    mid = db[db_new['care_intensity'] == 1]
    worst = db[db_new['care_intensity'] == 2]
    res = pd.concat([best,mid,worst])
    return res

if __name__ == '__main__':
    a = pd.read_csv(f'src/bdd/plantas.csv')
    print(water_priority({
        'Agua disponible': 1,
        'Cantidad de luz': 1,
        'Material vegetal': ['Arbusto', 'Floral'],
        'Hardiness Zone': 15,
    },'src/bdd/plantas'))
    print(color_priority({
        'Agua disponible': 1,
        'Cantidad de luz': 1,
        'Material vegetal': ['Arbusto', 'Floral'],
        'Hardiness Zone': 15,
    },'src/bdd/plantas'))
    print(bee_priority({
            'Agua disponible': 1,
            'Cantidad de luz': 1,
            'Material vegetal': ['Arbusto', 'Floral'],
            'Hardiness Zone': 15,
        },'src/bdd/plantas'))
    print(bird_priority({
            'Agua disponible': 1,
            'Cantidad de luz': 1,
            'Material vegetal': ['Arbusto', 'Floral'],
            'Hardiness Zone': 15,
        },'src/bdd/plantas'))
    print(aroma_priority({
            'Agua disponible': 1,
            'Cantidad de luz': 1,
            'Material vegetal': ['Arbusto', 'Floral'],
            'Hardiness Zone': 15,
        },'src/bdd/plantas'))
    print(care_priority({
            'Agua disponible': 1,
            'Cantidad de luz': 1,
            'Material vegetal': ['Arbusto', 'Floral'],
            'Hardiness Zone': 15,
        },'src/bdd/plantas'))

