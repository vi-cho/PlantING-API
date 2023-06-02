import pandas as pd

def basic_filter(data, db_filename):
    db = pd.read_csv(f'../bdd/{db_filename}')
    db = db.drop(columns='Marca temporal')
    db['Tipo de material vegetal'] = db['Tipo de material vegetal'].apply(lambda x: x.split(','))
    db = db[
        (db['Agua requerida'] <= data['Agua disponible']) &
        (db['Cantidad de luz'] <= data['Cantidad de luz']) &
        (db['Tipo de material vegetal'].apply(lambda x: any(item in x for item in data['Material vegetal']))) &
        (db['Hardiness Zone'] >= data['Hardiness Zone'])
    ]
    print(db)

if __name__ == '__main__':
    basic_filter({
        'Agua disponible': 1,
        'Cantidad de luz': 1,
        'Material vegetal': ['Arbusto', 'Floral'],
        'Hardiness Zone': 15,
    }, 'plantas_final.csv')
