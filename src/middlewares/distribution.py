from flask import render_template
import pandas as pd
import numpy as np
import math
from middlewares.salida import salida_entero, salida_parcial

def distribuir(db, nombre, ancho, largo, accion, db_original):
    if accion == "Todo":
        if nombre == "Jardín de menor consumo hídrico":
            return entero_menor_consumo(db, ancho, largo, db_original)
        elif nombre == "Jardín mas colorido":
            return entero_colorido(db, ancho, largo, db_original)
        elif nombre == "Jardín mas atractivo para polinizadores":
            return entero_polinizadores(db, ancho, largo, db_original)
        elif nombre == "Jardín para colibries y otras aves":
            return entero_aves(db, ancho, largo, db_original)
        elif nombre == "Jardín de aromas":
            return entero_aromas(db, ancho, largo, db_original)
        elif nombre == "Jardín mas facil de mantener":
            return entero_cuidados(db, ancho, largo, db_original)
        else:
            return entero_anual(db, ancho, largo, db_original)
    else:
        if nombre == "Jardín de menor consumo hídrico":
            return parcial_menor_consumo(db, ancho, largo, db_original)
        elif nombre == "Jardín mas colorido":
            return parcial_colorido(db, ancho, largo, db_original)
        elif nombre == "Jardín mas atractivo para polinizadores":
            return parcial_polinizadores(db, ancho, largo, db_original)
        elif nombre == "Jardín para colibries y otras aves":
            return parcial_aves(db, ancho, largo, db_original)
        elif nombre == "Jardín de aromas":
            return parcial_aromas(db, ancho, largo, db_original)
        elif nombre == "Jardín mas facil de mantener":
            return parcial_cuidados(db, ancho, largo, db_original)
        else:
            return parcial_anual(db, ancho, largo, db_original)


def entero_menor_consumo(db, ancho, largo, db_original):
    db_ordenada = db.sort_values(by='Ranking_agua')
    
    if len(db.index) > (math.sqrt(ancho*largo)+10):
        cantidad_plantas = int((math.sqrt(ancho*largo)+10))
        db_final = db_ordenada.head(cantidad_plantas)
    else:
        restante = int((math.sqrt(ancho*largo)+10)) - len(db_ordenada.index)
        db_restante = pd.merge(db_original, db_ordenada, how='outer', indicator=True)
        db_restante = db_restante[db_restante['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_restante = db_restante.sample(n=restante)
        db_final = pd.concat([db_ordenada, db_restante], ignore_index=True)
    return salida_entero(db_final, "Jardín de menor consumo hídrico", ancho, largo, db_original)

def entero_colorido(db, ancho, largo, db_original):
    db_ordenada = db.sort_values(by='Ranking_color')
    
    if len(db.index) > (math.sqrt(ancho*largo)+10):
        cantidad_plantas = int((math.sqrt(ancho*largo)+10))
        db_final = db_ordenada.head(cantidad_plantas)
    else:
        restante = int((math.sqrt(ancho*largo)+10)) - len(db_ordenada.index)
        db_restante = pd.merge(db_original, db_ordenada, how='outer', indicator=True)
        db_restante = db_restante[db_restante['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_restante = db_restante.sample(n=restante)
        db_final = pd.concat([db_ordenada, db_restante], ignore_index=True)
    return salida_entero(db_final, "Jardín más colorido", ancho, largo, db_original)

def entero_polinizadores(db, ancho, largo, db_original):
    db_ordenada = db.sort_values(by='Ranking_polinizadores')
    
    if len(db.index) > (math.sqrt(ancho*largo)+10):
        cantidad_plantas = int((math.sqrt(ancho*largo)+10))
        db_final = db_ordenada.head(cantidad_plantas)
    else:
        restante = int((math.sqrt(ancho*largo)+10)) - len(db_ordenada.index)
        db_restante = pd.merge(db_original, db_ordenada, how='outer', indicator=True)
        db_restante = db_restante[db_restante['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_restante = db_restante.sample(n=restante)
        db_final = pd.concat([db_ordenada, db_restante], ignore_index=True)
    return salida_entero(db_final, "Jardín más atractivo para polinizadores", ancho, largo, db_original)

def entero_aves(db, ancho, largo, db_original):
    db_ordenada = db.sort_values(by='Ranking_aves')
    
    if len(db.index) > (math.sqrt(ancho*largo)+10):
        cantidad_plantas = int((math.sqrt(ancho*largo)+10))
        db_final = db_ordenada.head(cantidad_plantas)
    else:
        restante = int((math.sqrt(ancho*largo)+10)) - len(db_ordenada.index)
        db_restante = pd.merge(db_original, db_ordenada, how='outer', indicator=True)
        db_restante = db_restante[db_restante['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_restante = db_restante.sample(n=restante)
        db_final = pd.concat([db_ordenada, db_restante], ignore_index=True)
    return salida_entero(db_final, "Jardín atractivo para colibries y otras aves", ancho, largo, db_original)

def entero_aromas(db, ancho, largo, db_original):
    db_ordenada = db.sort_values(by='Ranking_aromas')
    
    if len(db.index) > (math.sqrt(ancho*largo)+10):
        cantidad_plantas = int((math.sqrt(ancho*largo)+10))
        db_final = db_ordenada.head(cantidad_plantas)
    else:
        restante = int((math.sqrt(ancho*largo)+10)) - len(db_ordenada.index)
        db_restante = pd.merge(db_original, db_ordenada, how='outer', indicator=True)
        db_restante = db_restante[db_restante['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_restante = db_restante.sample(n=restante)
        db_final = pd.concat([db_ordenada, db_restante], ignore_index=True)
    return salida_entero(db_final, "Jardín de aromas", ancho, largo, db_original)

def entero_cuidados(db, ancho, largo, db_original):
    db_ordenada = db[(db["Para cada categoría señale una opción entre poco/medio/mucho [Nivel de cuidado]"] == "Poco")]
    
    if len(db_ordenada.index) > (math.sqrt(ancho*largo)+10):
        cantidad_plantas = int((math.sqrt(ancho*largo)+10))
        db_final = db_ordenada.sample(n=cantidad_plantas)
    else:
        restante = int((math.sqrt(ancho*largo)+10)) - len(db_ordenada.index)
        db_restante = pd.merge(db_original, db_ordenada, how='outer', indicator=True)
        db_restante = db_restante[db_restante['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_restante = db_restante.sample(n=restante)
        db_final = pd.concat([db_ordenada, db_restante], ignore_index=True)
    return salida_entero(db_final, "Jardín más fácil de mantener", ancho, largo, db_original)

def entero_anual(db, ancho, largo, db_original):
    db_otono = db_original[(db_original["Para cada evento eliga la época correspondiente [Floración]"] == "Otoño")]
    db_invierno = db_original[(db_original["Para cada evento eliga la época correspondiente [Floración]"] == "Invierno")]

    db_ot_inv = pd.concat([db_otono, db_invierno], ignore_index=True)

    cantidad_restante = (int((math.sqrt(ancho*largo)+10)) - len(db_ot_inv.index))

    if cantidad_restante > 0:
        db_primavera = db[(db["Para cada evento eliga la época correspondiente [Floración]"] == "Primavera")]
        if len(db_primavera.index) > 0:
            tamano_muestra = min((int(cantidad_restante//2)+1), len(db_primavera.index))
            if tamano_muestra == (int(cantidad_restante//2)+1):
                db_primavera = db_primavera.sample(n=tamano_muestra)
            else:
                db_primavera1 = db_primavera.sample(n=tamano_muestra)
                tamano_segunda_muestra = (int(cantidad_restante//2)+1) - len(db_primavera.index)
                db_original_sin_dup = pd.merge(db_original, db_primavera, how='outer', indicator=True)
                db_original_sin_dup = db_original_sin_dup[db_original_sin_dup['_merge'] == 'left_only'].drop('_merge', axis=1)
                db_primavera2 = db_original_sin_dup.sample(n=tamano_segunda_muestra)
                db_primavera = pd.concat([db_primavera1, db_primavera2], ignore_index=True)
        else:
            db_primavera = db_original[(db_original["Para cada evento eliga la época correspondiente [Floración]"] == "Primavera")]
            db_primavera = db_primavera.sample(n=(int(cantidad_restante//2)+1))
        db_verano = db[(db["Para cada evento eliga la época correspondiente [Floración]"] == "Verano")]
        if len(db_verano.index) > 0:
            tamano_muestra = min(int(cantidad_restante//2), len(db_verano.index))
            if tamano_muestra == int(cantidad_restante//2):
                db_verano = db_verano.sample(n=tamano_muestra)
            else:
                db_verano1 = db_verano.sample(n=tamano_muestra)
                tamano_segunda_muestra = int(cantidad_restante//2) - len(db_verano.index)
                db_original_sin_dup = pd.merge(db_original, db_verano, how='outer', indicator=True)
                db_original_sin_dup = db_original_sin_dup[db_original_sin_dup['_merge'] == 'left_only'].drop('_merge', axis=1)
                db_verano2 = db_original_sin_dup.sample(n=tamano_segunda_muestra)
                db_verano = pd.concat([db_verano1, db_verano2], ignore_index=True)
        else:
            db_verano = db_original[(db_original["Para cada evento eliga la época correspondiente [Floración]"] == "Verano")]
            db_verano = db_verano.sample(n=int(cantidad_restante//2))
        db_final = pd.concat([db_ot_inv, db_primavera, db_verano], ignore_index=True)
        return salida_entero(db_final, "Jardín bello en todas las épocas del año", ancho, largo, db_original)
    else:
        db_primavera = db[(db["Para cada evento eliga la época correspondiente [Floración]"] == "Primavera")]
        if len(db_primavera.index) > 0:
            tamano_muestra = min(3, len(db_primavera.index))
            db_primavera = db_primavera.sample(n=tamano_muestra)
        else:
            db_primavera = db_original[(db_original["Para cada evento eliga la época correspondiente [Floración]"] == "Primavera")]
            db_primavera = db_primavera.sample(n=3)
        db_verano = db[(db["Para cada evento eliga la época correspondiente [Floración]"] == "Verano")]
        if len(db_verano.index) > 0:
            tamano_muestra = min(3, len(db_verano.index))
            db_verano = db_verano.sample(n=tamano_muestra)
        else:
            db_verano = db_original[(db_original["Para cada evento eliga la época correspondiente [Floración]"] == "Verano")]
            db_verano = db_verano.sample(n=3)
        db_final = pd.concat([db_ot_inv, db_primavera, db_verano], ignore_index=True)
        return salida_entero(db_final, "Jardín bello en todas las épocas del año", ancho, largo, db_original)
    

def parcial_menor_consumo(db, ancho, largo, db_original):
    db_ordenada = db.sort_values(by='Ranking_agua')
    
    if len(db.index) > (math.sqrt(ancho*largo)+5):
        cantidad_plantas = int((math.sqrt(ancho*largo)+5))
        db_final = db_ordenada.head(cantidad_plantas)
    else:
        restante = int((math.sqrt(ancho*largo)+5)) - len(db_ordenada.index)
        db_restante = pd.merge(db_original, db_ordenada, how='outer', indicator=True)
        db_restante = db_restante[db_restante['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_restante = db_restante.sample(n=restante)
        db_final = pd.concat([db_ordenada, db_restante], ignore_index=True)
    return salida_parcial(db_final, "Espacio de menor consumo hídrico", ancho, largo, db_original)

def parcial_colorido(db, ancho, largo, db_original):
    db_ordenada = db.sort_values(by='Ranking_color')
    
    if len(db.index) > (math.sqrt(ancho*largo)+5):
        cantidad_plantas = int((math.sqrt(ancho*largo)+5))
        db_final = db_ordenada.head(cantidad_plantas)
    else:
        restante = int((math.sqrt(ancho*largo)+5)) - len(db_ordenada.index)
        db_restante = pd.merge(db_original, db_ordenada, how='outer', indicator=True)
        db_restante = db_restante[db_restante['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_restante = db_restante.sample(n=restante)
        db_final = pd.concat([db_ordenada, db_restante], ignore_index=True)
    return salida_parcial(db_final, "Espacio más colorido", ancho, largo, db_original)

def parcial_polinizadores(db, ancho, largo, db_original):
    db_ordenada = db.sort_values(by='Ranking_polinizadores')
    
    if len(db.index) > (math.sqrt(ancho*largo)+5):
        cantidad_plantas = int((math.sqrt(ancho*largo)+5))
        db_final = db_ordenada.head(cantidad_plantas)
    else:
        restante = int((math.sqrt(ancho*largo)+5)) - len(db_ordenada.index)
        db_restante = pd.merge(db_original, db_ordenada, how='outer', indicator=True)
        db_restante = db_restante[db_restante['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_restante = db_restante.sample(n=restante)
        db_final = pd.concat([db_ordenada, db_restante], ignore_index=True)
    return salida_parcial(db_final, "Espacio más atractivo para polinizadores", ancho, largo, db_original)

def parcial_aves(db, ancho, largo, db_original):
    db_ordenada = db.sort_values(by='Ranking_aves')
    
    if len(db.index) > (math.sqrt(ancho*largo)+5):
        cantidad_plantas = int((math.sqrt(ancho*largo)+5))
        db_final = db_ordenada.head(cantidad_plantas)
    else:
        restante = int((math.sqrt(ancho*largo)+5)) - len(db_ordenada.index)
        db_restante = pd.merge(db_original, db_ordenada, how='outer', indicator=True)
        db_restante = db_restante[db_restante['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_restante = db_restante.sample(n=restante)
        db_final = pd.concat([db_ordenada, db_restante], ignore_index=True)
    return salida_parcial(db_final, "Espacio atractivo para colibries y otras aves", ancho, largo, db_original)

def parcial_aromas(db, ancho, largo, db_original):
    db_ordenada = db.sort_values(by='Ranking_aromas')
    
    if len(db.index) > (math.sqrt(ancho*largo)+5):
        cantidad_plantas = int((math.sqrt(ancho*largo)+5))
        db_final = db_ordenada.head(cantidad_plantas)
    else:
        restante = int((math.sqrt(ancho*largo)+5)) - len(db_ordenada.index)
        db_restante = pd.merge(db_original, db_ordenada, how='outer', indicator=True)
        db_restante = db_restante[db_restante['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_restante = db_restante.sample(n=restante)
        db_final = pd.concat([db_ordenada, db_restante], ignore_index=True)
    return salida_parcial(db_final, "Espacio de aromas", ancho, largo, db_original)

def parcial_cuidados(db, ancho, largo, db_original):
    db_ordenada = db[(db["Para cada categoría señale una opción entre poco/medio/mucho [Nivel de cuidado]"] == "Poco")]
    
    if len(db_ordenada.index) > (math.sqrt(ancho*largo)+5):
        cantidad_plantas = int((math.sqrt(ancho*largo)+5))
        db_final = db_ordenada.sample(n=cantidad_plantas)
    else:
        restante = int((math.sqrt(ancho*largo)+5)) - len(db_ordenada.index)
        db_restante = pd.merge(db_original, db_ordenada, how='outer', indicator=True)
        db_restante = db_restante[db_restante['_merge'] == 'left_only'].drop('_merge', axis=1)
        db_restante = db_restante.sample(n=restante)
        db_final = pd.concat([db_ordenada, db_restante], ignore_index=True)
    return salida_parcial(db_final, "Espacio más facil de mantener", ancho, largo, db_original)

def parcial_anual(db, ancho, largo, db_original):
    db_otono = db_original[(db_original["Para cada evento eliga la época correspondiente [Floración]"] == "Otoño")]
    db_invierno = db_original[(db_original["Para cada evento eliga la época correspondiente [Floración]"] == "Invierno")]
    db_otono = db_otono.sample(n=2)
    db_invierno = db_invierno.sample(n=2)

    db_ot_inv = pd.concat([db_otono, db_invierno], ignore_index=True)

    cantidad_restante = (int((math.sqrt(ancho*largo)+5)) - len(db_ot_inv.index))

    if cantidad_restante > 0:
        db_primavera = db[(db["Para cada evento eliga la época correspondiente [Floración]"] == "Primavera")]
        if len(db_primavera.index) > 0:
            tamano_muestra = min((int(cantidad_restante//2)+1), len(db_primavera.index))
            if tamano_muestra == (int(cantidad_restante//2)+1):
                db_primavera = db_primavera.sample(n=tamano_muestra)
            else:
                db_primavera1 = db_primavera.sample(n=tamano_muestra)
                tamano_segunda_muestra = (int(cantidad_restante//2)+1) - len(db_primavera.index)
                db_original_sin_dup = pd.merge(db_original, db_primavera, how='outer', indicator=True)
                db_original_sin_dup = db_original_sin_dup[db_original_sin_dup['_merge'] == 'left_only'].drop('_merge', axis=1)
                db_primavera2 = db_original_sin_dup.sample(n=tamano_segunda_muestra)
                db_primavera = pd.concat([db_primavera1, db_primavera2], ignore_index=True)
        else:
            db_primavera = db_original[(db_original["Para cada evento eliga la época correspondiente [Floración]"] == "Primavera")]
            db_primavera = db_primavera.sample(n=(int(cantidad_restante//2)+1))
        db_verano = db[(db["Para cada evento eliga la época correspondiente [Floración]"] == "Verano")]
        if len(db_verano.index) > 0:
            tamano_muestra = min(int(cantidad_restante//2), len(db_verano.index))
            if tamano_muestra == int(cantidad_restante//2):
                db_verano = db_verano.sample(n=tamano_muestra)
            else:
                db_verano1 = db_verano.sample(n=tamano_muestra)
                tamano_segunda_muestra = int(cantidad_restante//2) - len(db_verano.index)
                db_original_sin_dup = pd.merge(db_original, db_verano, how='outer', indicator=True)
                db_original_sin_dup = db_original_sin_dup[db_original_sin_dup['_merge'] == 'left_only'].drop('_merge', axis=1)
                db_verano2 = db_original_sin_dup.sample(n=tamano_segunda_muestra)
                db_verano = pd.concat([db_verano1, db_verano2], ignore_index=True)
        else:
            db_verano = db_original[(db_original["Para cada evento eliga la época correspondiente [Floración]"] == "Verano")]
            db_verano = db_verano.sample(n=int(cantidad_restante//2))
        db_final = pd.concat([db_ot_inv, db_primavera, db_verano], ignore_index=True)
        return salida_parcial(db_final, "Espacio bello en todas las épocas del año", ancho, largo, db_original)
    else:
        db_primavera = db[(db["Para cada evento eliga la época correspondiente [Floración]"] == "Primavera")]
        if len(db_primavera.index) > 0:
            tamano_muestra = min(2, len(db_primavera.index))
            db_primavera = db_primavera.sample(n=tamano_muestra)
        else:
            db_primavera = db_original[(db_original["Para cada evento eliga la época correspondiente [Floración]"] == "Primavera")]
            db_primavera = db_primavera.sample(n=2)
        db_verano = db[(db["Para cada evento eliga la época correspondiente [Floración]"] == "Verano")]
        if len(db_verano.index) > 0:
            tamano_muestra = min(2, len(db_verano.index))
            db_verano = db_verano.sample(n=tamano_muestra)
        else:
            db_verano = db_original[(db_original["Para cada evento eliga la época correspondiente [Floración]"] == "Verano")]
            db_verano = db_verano.sample(n=2)
        db_final = pd.concat([db_ot_inv, db_primavera, db_verano], ignore_index=True)
        return salida_parcial(db_final, "Espacio bello en todas las épocas del año", ancho, largo, db_original)
