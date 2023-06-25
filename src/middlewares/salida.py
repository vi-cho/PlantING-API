from flask import render_template
import pandas as pd
import numpy as np
import math

def salida_entero(db, nombre, ancho, largo, db_original):
    
    db_primer_nivel = db[(db["Altura máxima (en metros)"] < 0.5)]
    db_segundo_nivel = db[(db["Altura máxima (en metros)"] >= 0.5) &
                            (db["Altura máxima (en metros)"] <= 2)]
    db_tercer_nivel = db[(db["Altura máxima (en metros)"] > 2)]

    if len(db_primer_nivel.index) < 3:
        extras = 3 - len(db_primer_nivel.index)
        db_original_sin_dup = pd.merge(db_original, db_primer_nivel, how='outer', indicator=True)
        db_original_sin_dup = db_original_sin_dup[db_original_sin_dup['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_extras = db_original_sin_dup[(db_original_sin_dup["Altura máxima (en metros)"] < 0.5)]
        db_extras = db_extras.sample(n=extras)
        db_primer_nivel = pd.concat([db_primer_nivel, db_extras], ignore_index=True)
    
    if len(db_segundo_nivel.index) < 3:
        extras = 3 - len(db_segundo_nivel.index)
        db_original_sin_dup = pd.merge(db_original, db_segundo_nivel, how='outer', indicator=True)
        db_original_sin_dup = db_original_sin_dup[db_original_sin_dup['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_extras = db_original_sin_dup[(db_original_sin_dup["Altura máxima (en metros)"] >= 0.5) &
                                        (db["Altura máxima (en metros)"] <= 2)]
        db_extras = db_extras.sample(n=extras)
        db_segundo_nivel = pd.concat([db_segundo_nivel, db_extras], ignore_index=True)
    
    if len(db_tercer_nivel.index) < 3:
        extras = 3 - len(db_tercer_nivel.index)
        db_original_sin_dup = pd.merge(db_original, db_tercer_nivel, how='outer', indicator=True)
        db_original_sin_dup = db_original_sin_dup[db_original_sin_dup['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_extras = db_original_sin_dup[(db_original_sin_dup["Altura máxima (en metros)"] > 2)]
        db_extras = db_extras.sample(n=extras)
        db_tercer_nivel = pd.concat([db_tercer_nivel, db_extras], ignore_index=True)

    db_primer_nivel = db_primer_nivel.sort_values(by='Ranking_agua')
    db_segundo_nivel = db_segundo_nivel.sort_values(by='Ranking_agua')
    db_tercer_nivel = db_tercer_nivel.sort_values(by='Ranking_agua')
    
    plantas1 = db_primer_nivel["Nombre en español"].values.tolist()
    plantas2 = db_segundo_nivel["Nombre en español"].values.tolist()
    plantas3 = db_tercer_nivel["Nombre en español"].values.tolist()
    
    if len(plantas1) > 0:
        n_bloquecen = int(int(ancho)*int(largo)*0.7/4)
        n_ind_bloquecen = n_bloquecen // len(plantas1)
        if n_ind_bloquecen == 0:
            n_ind_bloquecen = 1
        n_bloquecen = n_ind_bloquecen * len(plantas1)
    else:
        n_bloquecen = 0
        n_ind_bloquecen = 0
    
    db1_dividida = np.array_split(db_primer_nivel, 3)
    db2_dividida = np.array_split(db_segundo_nivel, 3)
    db3_dividida = np.array_split(db_tercer_nivel, 3)
    
    db_plantas11 = db1_dividida[0]
    db_plantas12 = db1_dividida[1]
    db_plantas13 = db1_dividida[2]
    db_plantas21 = db2_dividida[0]
    db_plantas22 = db2_dividida[1]
    db_plantas23 = db2_dividida[2]
    db_plantas31 = db3_dividida[0]
    db_plantas32 = db3_dividida[1]
    db_plantas33 = db3_dividida[2]
    plantas11 = db_plantas11["Nombre en español"].values.tolist()
    plantas12 = db_plantas12["Nombre en español"].values.tolist()
    plantas13 = db_plantas13["Nombre en español"].values.tolist()
    plantas21 = db_plantas21["Nombre en español"].values.tolist()
    plantas22 = db_plantas22["Nombre en español"].values.tolist()
    plantas23 = db_plantas23["Nombre en español"].values.tolist()
    plantas31 = db_plantas31["Nombre en español"].values.tolist()
    plantas32 = db_plantas32["Nombre en español"].values.tolist()
    plantas33 = db_plantas33["Nombre en español"].values.tolist()

    if len(plantas11) > 0:
        n_plantas11 = int(ancho)*2
        n_ind_plantas11 = n_plantas11 // len(plantas11)
        if n_ind_plantas11 == 0:
            n_ind_plantas11 = 1
        n_plantas11 = n_ind_plantas11 * len(plantas11)
    else:
        n_plantas11 = 0
        n_ind_plantas11 = 0

    if len(plantas21) > 0:
        n_plantas21 = int(int(ancho)/1.5)
        n_ind_plantas21 = n_plantas21 // len(plantas21)
        if n_ind_plantas21 == 0:
            n_ind_plantas21 = 1
        n_plantas21 = n_ind_plantas21 * len(plantas21)
    else:
        n_plantas21 = 0
        n_ind_plantas21 = 0

    if len(plantas31) > 0:
        n_plantas31 = int(int(ancho)/2.5)
        n_ind_plantas31 = n_plantas31 // len(plantas31)
        if n_ind_plantas31 == 0:
            n_ind_plantas31 = 1
        n_plantas31 = n_ind_plantas31 * len(plantas31)
    else:
        n_plantas31 = 0
        n_ind_plantas31 = 0

    if len(plantas12) > 0:
        n_plantas12 = int(largo)*2*0.8
        n_ind_plantas12 = n_plantas12 // len(plantas12)
        if n_ind_plantas12 == 0:
            n_ind_plantas12 = 1
        n_plantas12 = n_ind_plantas12 * len(plantas12)
    else:
        n_plantas12 = 0
        n_ind_plantas12 = 0

    if len(plantas22) > 0:
        n_plantas22 = int(int(largo)*0.8/1.5)
        n_ind_plantas22 = n_plantas22 // len(plantas22)
        if n_ind_plantas22 == 0:
            n_ind_plantas22 = 1
        n_plantas22 = n_ind_plantas22 * len(plantas22)
    else:
        n_plantas22 = 0
        n_ind_plantas22 = 0

    if len(plantas32) > 0:
        n_plantas32 = int(int(largo)*0.8/2.5)
        n_ind_plantas32 = n_plantas32 // len(plantas32)
        if n_ind_plantas32 == 0:
            n_ind_plantas32 = 1
        n_plantas32 = n_ind_plantas32 * len(plantas32)
    else:
        n_plantas32 = 0
        n_ind_plantas32 = 0

    if len(plantas13) > 0:
        n_plantas13 = int(largo)*2*0.8
        n_ind_plantas13 = n_plantas13 // len(plantas13)
        if n_ind_plantas13 == 0:
            n_ind_plantas13 = 1
        n_plantas13 = n_ind_plantas13 * len(plantas13)
    else:
        n_plantas13 = 0
        n_ind_plantas13 = 0

    if len(plantas23) > 0:
        n_plantas23 = int(int(largo)*0.8/1.5)
        n_ind_plantas23 = n_plantas23 // len(plantas23)
        if n_ind_plantas23 == 0:
            n_ind_plantas23 = 1
        n_plantas23 = n_ind_plantas23 * len(plantas23)
    else:
        n_plantas23 = 0
        n_ind_plantas23 = 0

    if len(plantas33) > 0:
        n_plantas33 = int(int(largo)*0.8/2.5)
        n_ind_plantas33 = n_plantas33 // len(plantas33)
        if n_ind_plantas33 == 0:
            n_ind_plantas33 = 1
        n_plantas33 = n_ind_plantas33 * len(plantas33)
    else:
        n_plantas33 = 0
        n_ind_plantas33 = 0

    return render_template("distribution.html", largo_db=len(db.index), nombre=nombre, ancho=ancho, largo=largo,
                            plantas1=plantas1, plantas2=plantas2, plantas3=plantas3, n_bloquecen=n_bloquecen,
                            n_ind_bloquecen=n_ind_bloquecen, plantas11=plantas11, plantas12=plantas12, plantas13=plantas13,
                            plantas21=plantas21, plantas22=plantas22, plantas23=plantas23, plantas31=plantas31,
                            plantas32=plantas32, plantas33=plantas33, n_plantas11=n_plantas11, n_ind_plantas11=n_ind_plantas11,
                            n_plantas21=n_plantas21, n_ind_plantas21=n_ind_plantas21, n_plantas31=n_plantas31,
                            n_ind_plantas31=n_ind_plantas31, n_plantas12=n_plantas12, n_ind_plantas12=n_ind_plantas12,
                            n_plantas22=n_plantas22, n_ind_plantas22=n_ind_plantas22, n_plantas32=n_plantas32,
                            n_ind_plantas32=n_ind_plantas32, n_plantas13=n_plantas13, n_ind_plantas13=n_ind_plantas13,
                            n_plantas23=n_plantas23, n_ind_plantas23=n_ind_plantas23, n_plantas33=n_plantas33,
                            n_ind_plantas33=n_ind_plantas33)

def salida_parcial(db, nombre, ancho, largo, db_original):
    db_primer_nivel = db[(db["Altura máxima (en metros)"] < 0.5)]
    db_segundo_nivel = db[(db["Altura máxima (en metros)"] >= 0.5) &
                            (db["Altura máxima (en metros)"] <= 2)]
    db_tercer_nivel = db[(db["Altura máxima (en metros)"] > 2)]

    if len(db_primer_nivel.index) == 0:
        db_original_sin_dup = pd.merge(db_original, db_primer_nivel, how='outer', indicator=True)
        db_original_sin_dup = db_original_sin_dup[db_original_sin_dup['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_extras = db_original_sin_dup[(db_original_sin_dup["Altura máxima (en metros)"] < 0.5)]
        db_extras = db_extras.sample(n=1)
        db_primer_nivel = pd.concat([db_primer_nivel, db_extras], ignore_index=True)
    
    if len(db_segundo_nivel.index) == 0:
        db_original_sin_dup = pd.merge(db_original, db_segundo_nivel, how='outer', indicator=True)
        db_original_sin_dup = db_original_sin_dup[db_original_sin_dup['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_extras = db_original_sin_dup[(db_original_sin_dup["Altura máxima (en metros)"] >= 0.5) &
                                        (db["Altura máxima (en metros)"] <= 2)]
        db_extras = db_extras.sample(n=1)
        db_segundo_nivel = pd.concat([db_segundo_nivel, db_extras], ignore_index=True)
    
    if len(db_tercer_nivel.index) == 0:
        db_original_sin_dup = pd.merge(db_original, db_tercer_nivel, how='outer', indicator=True)
        db_original_sin_dup = db_original_sin_dup[db_original_sin_dup['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_extras = db_original_sin_dup[(db_original_sin_dup["Altura máxima (en metros)"] > 2)]
        db_extras = db_extras.sample(n=1)
        db_tercer_nivel = pd.concat([db_tercer_nivel, db_extras], ignore_index=True)

    plantas1 = db_primer_nivel["Nombre en español"].values.tolist()
    plantas2 = db_segundo_nivel["Nombre en español"].values.tolist()
    plantas3 = db_tercer_nivel["Nombre en español"].values.tolist()

    if len(plantas1) > 0:
        n_plantas1 = int(largo)*2
        n_ind_plantas1 = n_plantas1 // len(plantas1)
        if n_ind_plantas1 == 0:
            n_ind_plantas1 = 1
        n_plantas1 = n_ind_plantas1 * len(plantas1)

        n_plantas1_cen = int(largo)*4 + int(int(ancho)*4*0.6)
        n_ind_plantas1_cen = n_plantas1_cen // len(plantas1)
        if n_ind_plantas1_cen == 0:
            n_ind_plantas1_cen = 1
        n_plantas1_cen = n_ind_plantas1_cen * len(plantas1)
    else:
        n_plantas1 = 0
        n_ind_plantas1 = 0

    if len(plantas2) > 0:
        n_plantas2 = int(int(largo)/1.5)
        n_ind_plantas2 = n_plantas2 // len(plantas2)
        if n_ind_plantas2 == 0:
            n_ind_plantas2 = 1
        n_plantas2 = n_ind_plantas2 * len(plantas2)

        n_plantas2_cen = int(int(ancho)*int(largo)*0.36/1.5)
        n_ind_plantas2_cen = n_plantas2_cen // len(plantas2)
        if n_ind_plantas2_cen == 0:
            n_ind_plantas2_cen = 1
        n_plantas2_cen = n_ind_plantas2_cen * len(plantas2)
    else:
        n_plantas2 = 0
        n_ind_plantas2 = 0

    if len(plantas3) > 0:
        n_plantas3 = int(int(largo)/2.5)
        n_ind_plantas3 = n_plantas3 // len(plantas3)
        if n_ind_plantas3 == 0:
            n_ind_plantas3 = 1
        n_plantas3 = n_ind_plantas3 * len(plantas3)
    else:
        n_plantas3 = 0
        n_ind_plantas3 = 0

    return render_template("little_space.html", largo_db=len(db.index), nombre=nombre, ancho=ancho, largo=largo,
                            plantas1=plantas1, plantas2=plantas2, plantas3=plantas3, n_plantas1=n_plantas1,
                            n_ind_plantas1=n_ind_plantas1, n_plantas2=n_plantas2, n_ind_plantas2=n_ind_plantas2,
                            n_plantas3=n_plantas3, n_ind_plantas3=n_ind_plantas3, n_plantas1_cen=n_plantas1_cen,
                            n_ind_plantas1_cen=n_ind_plantas1_cen, n_plantas2_cen=n_plantas2_cen,
                            n_ind_plantas2_cen=n_ind_plantas2_cen)