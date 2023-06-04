from flask import render_template
import pandas as pd

def distribuir(db, nombre, ancho, largo):
    if int(ancho) > int(largo) and (int(ancho)*int(largo)) > 25:
        db_primer_nivel = db[(db["Altura máxima (en metros)"] < 0.5)]
        db_segundo_nivel = db[(db["Altura máxima (en metros)"] >= 0.5) &
                              (db["Altura máxima (en metros)"] <= 1.5)]
        db_tercer_nivel = db[(db["Altura máxima (en metros)"] > 1.5)]
        
        plantas1 = db_primer_nivel["Nombre en español"].values.tolist()
        plantas2 = db_segundo_nivel["Nombre en español"].values.tolist()
        plantas3 = db_tercer_nivel["Nombre en español"].values.tolist()
        
        if len(plantas1) > 0:
            n_bloquecen = int(int(ancho)*int(largo)*0.7/4)
            n_ind_bloquecen = n_bloquecen // len(plantas1)
            n_bloquecen = n_ind_bloquecen * len(plantas1)
        else:
            n_bloquecen = 0
            n_ind_bloquecen = 0
        
        db_plantas11 = db_primer_nivel.sample(frac = 1/3)
        resto1 = db_primer_nivel.drop(db_plantas11.index)
        db_plantas12 = resto1.sample(frac = 0.5)
        db_plantas13 = resto1.drop(db_plantas12.index)
        
        db_plantas21 = db_segundo_nivel.sample(frac = 1/3)
        resto2 = db_segundo_nivel.drop(db_plantas21.index)
        db_plantas22 = resto2.sample(frac = 0.5)
        db_plantas23 = resto2.drop(db_plantas22.index)

        db_plantas31 = db_tercer_nivel.sample(frac = 1/3)
        resto3 = db_tercer_nivel.drop(db_plantas31.index)
        db_plantas32 = resto3.sample(frac = 0.5)
        db_plantas33 = resto3.drop(db_plantas32.index)

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
            n_plantas11 = n_ind_plantas11 * len(plantas11)
        else:
            n_plantas11 = 0
            n_ind_plantas11 = 0

        if len(plantas21) > 0:
            n_plantas21 = int(int(ancho)/1.5)
            n_ind_plantas21 = n_plantas21 // len(plantas21)
            n_plantas21 = n_ind_plantas21 * len(plantas21)
        else:
            n_plantas21 = 0
            n_ind_plantas21 = 0

        if len(plantas31) > 0:
            n_plantas31 = int(int(ancho)/2.5)
            n_ind_plantas31 = n_plantas31 // len(plantas31)
            n_plantas31 = n_ind_plantas31 * len(plantas31)
        else:
            n_plantas31 = 0
            n_ind_plantas31 = 0

        if len(plantas12) > 0:
            n_plantas12 = int(largo)*2*0.8
            n_ind_plantas12 = n_plantas12 // len(plantas12)
            n_plantas12 = n_ind_plantas12 * len(plantas12)
        else:
            n_plantas12 = 0
            n_ind_plantas12 = 0

        if len(plantas22) > 0:
            n_plantas22 = int(int(largo)*0.8/1.5)
            n_ind_plantas22 = n_plantas22 // len(plantas22)
            n_plantas22 = n_ind_plantas22 * len(plantas22)
        else:
            n_plantas22 = 0
            n_ind_plantas22 = 0

        if len(plantas32) > 0:
            n_plantas32 = int(int(largo)*0.8/2.5)
            n_ind_plantas32 = n_plantas32 // len(plantas32)
            n_plantas32 = n_ind_plantas32 * len(plantas32)
        else:
            n_plantas32 = 0
            n_ind_plantas32 = 0

        if len(plantas13) > 0:
            n_plantas13 = int(largo)*2*0.8
            n_ind_plantas13 = n_plantas13 // len(plantas13)
            n_plantas13 = n_ind_plantas13 * len(plantas13)
        else:
            n_plantas13 = 0
            n_ind_plantas13 = 0

        if len(plantas23) > 0:
            n_plantas23 = int(int(largo)*0.8/1.5)
            n_ind_plantas23 = n_plantas23 // len(plantas23)
            n_plantas23 = n_ind_plantas23 * len(plantas23)
        else:
            n_plantas23 = 0
            n_ind_plantas23 = 0

        if len(plantas33) > 0:
            n_plantas33 = int(int(largo)*0.8/2.5)
            n_ind_plantas33 = n_plantas33 // len(plantas33)
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