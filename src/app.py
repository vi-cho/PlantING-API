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
        hardiness = form.hardiness.data
        if riego_abundante:
            agua = 2
        elif riego_moderado:
            agua = 1
        elif riego_bajo:
            agua = 0
        else:
            agua = 2
        if luz_abundante:
            luz = 2
        elif luz_moderada:
            luz = 1
        elif luz_baja:
            luz = 0
        else:
            luz = 2
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
        data = {
            'Agua disponible': agua,
            'Cantidad de luz': luz,
            'Material vegetal': texto,
            'Hardiness Zone': numero
        }
        db_filtrada = basic_filter(data, "plantas_final.csv")
        return redirect(url_for('choose_garden', agua=agua, luz=luz, material=material, hardiness=numero, ancho=ancho, largo=largo))
    return render_template("requirements.html", form=form)

@app.route('/choose_garden')
def choose_garden():
    ancho = request.args.get('ancho', None)
    largo = request.args.get('largo', None)
    agua = request.args.get('agua', None)
    luz = request.args.get('luz', None)
    material = request.args.get('material', None)
    hardiness = request.args.get('hardiness', None)
    # Preprocesar db
    # Filtrar 7 veces la db preprocesada, segun la funcion de cada jardin
    return render_template("choose_garden.html", agua=agua, luz=luz, material=material, hardiness=hardiness, ancho=ancho, largo=largo)

@app.route('/distribute')
def distribute():
    nombre = request.args.get('nombre', None)
    ancho = request.args.get('ancho', None)
    largo = request.args.get('largo', None)
    agua = request.args.get('agua', None)
    luz = request.args.get('luz', None)
    material = request.args.get('material', None)
    hardiness = request.args.get('hardiness', None)
    material_vegetal = material.split(",")
    data = {
            'Agua disponible': int(agua),
            'Cantidad de luz': int(luz),
            'Material vegetal': material_vegetal,
            'Hardiness Zone': int(hardiness)
        }
    # db_filtrada = basic_filter(data, "plantas_final.csv")
    db = pd.read_csv("plantas_final.csv")
    return distribuir(db, nombre, int(ancho), int(largo))