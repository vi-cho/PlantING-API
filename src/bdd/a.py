import pandas as pd

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

df = pd.read_csv('src/bdd/plantas.csv')
df['Hardiness Zone'] = df['Hardiness Zone'].replace(mapeo)

df.to_csv('plantas_final.csv')