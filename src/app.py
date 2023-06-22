from flask import Flask, render_template, request, redirect, url_for, session
from forms import RequirementsForm
from middlewares.distribution import distribuir
from bdd.a import mapeo
from middlewares.filters import basic_filter
import pandas as pd
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

@app.route('/')
def hello_world():
    texto = '<p>Bienvenido a PlantING!</p>\n<a href="/comenzar">Comenzar</a>'
    return texto

@app.route('/comenzar', methods=["GET", "POST"])
def requirements_form():
    form = RequirementsForm()
    if form.validate_on_submit():
        comuna = form.comuna.data
        accion = form.accion.data
        ancho = form.ancho.data
        largo = form.largo.data
        luz_baja = form.luz_baja.data
        luz_moderada = form.luz_moderada.data
        luz_abundante = form.luz_abundante.data
        riego_bajo = form.riego_bajo.data
        riego_moderado = form.riego_moderado.data
        riego_abundante = form.riego_abundante.data
        arbol = form.arbol.data
        arbusto = form.arbusto.data
        cubresuelo = form.cubresuelo.data
        enredadera = form.enredadera.data
        floral = form.floral.data
        frutal = form.frutal.data
        abejas = form.abejas.data
        mariposas = form.mariposas.data
        colibries = form.colibries.data
        hardiness = 'Zona 10A'
        if riego_abundante:
            agua = 2
        elif riego_moderado:
            agua = 1
        elif riego_bajo:
            agua = 0
        else:
            agua = 2
        if luz_abundante:
            luz = "Media,Mucha"
        elif luz_moderada:
            luz = "Mucha,Media,Poca"
        elif luz_baja:
            luz = "Media,Poca"
        else:
            luz = "Mucha,Media,Poca"
        material = []
        if arbol:
            material.append("Arbol")
        if arbusto:
            material.append("Arbusto")
        if cubresuelo:
            material.append("Cubresuelo")
        if enredadera:
            material.append("Enredadera")
        if floral:
            material.append("Floral")
        if frutal:
            material.append("Frutal")
        texto = ""
        for el in material:
            texto += el
            texto += ","
        texto = texto.strip(",")
        numero = mapeo[hardiness]
        return redirect(url_for('choose_garden', agua=agua, luz=luz, material=texto, hardiness=numero, ancho=ancho, largo=largo,
                                accion=accion))
    return render_template("requirements.html", form=form)

@app.route('/choose_garden')
def choose_garden():
    ancho = request.args.get('ancho', None)
    largo = request.args.get('largo', None)
    agua = request.args.get('agua', None)
    luz = request.args.get('luz', None)
    material = request.args.get('material', None)
    hardiness = request.args.get('hardiness', None)
    accion = request.args.get('accion', None)
    # Preprocesar db
    # Filtrar 7 veces la db preprocesada, segun la funcion de cada jardin
    return render_template("choose_garden.html", agua=agua, luz=luz, material=material, hardiness=hardiness, ancho=ancho, largo=largo,
                           accion=accion)

@app.route('/distribute')
def distribute():
    nombre = request.args.get('nombre', None)
    ancho = request.args.get('ancho', None)
    largo = request.args.get('largo', None)
    agua = request.args.get('agua', None)
    luz = request.args.get('luz', None)
    material = request.args.get('material', None)
    hardiness = request.args.get('hardiness', None)
    accion = request.args.get('accion', None)
    material_vegetal = material.split(",")
    luces = luz.split(",")
    db = pd.read_csv("src/bdd/100plantas.csv")
    if "Arbol" in material_vegetal:
        db_arbol = db[db['Tipo de material vegetal'].str.contains('Árbol')]
    else:
        db_arbol = db[db['Tipo de material vegetal'].str.contains('Nada')]
    if "Arbusto" in material_vegetal:
        db_arbusto = db[db['Tipo de material vegetal'].str.contains('Arbusto')]
    else:
        db_arbusto = db[db['Tipo de material vegetal'].str.contains('Nada')]
    if "Cubresuelo" in material_vegetal:
        db_cubresuelo = db[db['Tipo de material vegetal'].str.contains('Cubresuelo')]
    else:
        db_cubresuelo = db[db['Tipo de material vegetal'].str.contains('Nada')]
    if "Enredadera" in material_vegetal:
        db_enredadera = db[db['Tipo de material vegetal'].str.contains('Enredadera')]
    else:
        db_enredadera = db[db['Tipo de material vegetal'].str.contains('Nada')]
    if "Floral" in material_vegetal:
        db_floral = db[db['Tipo de material vegetal'].str.contains('Floral')]
    else:
        db_floral = db[db['Tipo de material vegetal'].str.contains('Nada')]
    if "Frutal" in material_vegetal:
        db_frutal = db[db['Tipo de material vegetal'].str.contains('Frutal')]
    else:
        db_frutal = db[db['Tipo de material vegetal'].str.contains('Nada')]
    db_tipos = pd.concat([db_arbol, db_arbusto, db_cubresuelo, db_enredadera, db_floral, db_frutal], ignore_index=True).drop_duplicates()
    db_luces = db[db['Cantidad de luz'].str.contains("Nada")]
    for elem in luces:
        db_luz = db[db['Cantidad de luz'].str.contains(elem)]
        db_luces = pd.concat([db_luces, db_luz], ignore_index=True).drop_duplicates()
    db_primaria = pd.merge(db_tipos, db_luces, how='inner')
    return distribuir(db_primaria, nombre, int(ancho), int(largo), accion, db)

@app.route('/plant_info')
def plant_info():
    nombre = request.args.get('nombre', None)
    db = pd.read_csv("src/bdd/100plantas.csv")
    db_planta = db[(db["Nombre en español"] == nombre)]
    indices = list(db_planta.index.values)
    ind = int(indices[0])
    latin = db_planta["Nombre científico"][ind]
    nativo = db_planta["Nativo de"][ind]
    material = db_planta["Tipo de material vegetal"][ind]
    follaje = db_planta["Caduco / Perenne"][ind]
    luz = db_planta["Cantidad de luz"][ind]
    agua = db_planta["Agua requerida"][ind]
    radio = db_planta["Radio máximo (en metros)"][ind]
    altura = db_planta["Altura máxima (en metros)"][ind]
    hardiness = db_planta["Hardiness Zone"][ind]
    siembra = db_planta["Para cada evento eliga la época correspondiente [Siembra]"][ind]
    floracion = db_planta["Para cada evento eliga la época correspondiente [Floración]"][ind]
    poda = db_planta["Para cada evento eliga la época correspondiente [Poda]"][ind]
    descripcion = db_planta["Descripción"][ind]
    return render_template("plant_info.html", nombre=nombre, latin=latin, nativo=nativo, material=material,
                           follaje=follaje, luz=luz, agua=agua, radio=radio, altura=altura, poda=poda,
                           hardiness=hardiness, siembra=siembra, floracion=floracion, descripcion=descripcion)