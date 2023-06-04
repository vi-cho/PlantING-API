from flask import Flask, render_template, request, redirect, url_for
from forms import RequirementsForm
from middlewares.distribution import distribuir
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

@app.route('/')
def hello_world():
    texto = '<p>Bienvenido a PlantING!</p>\n<a href="/comenzar">Comenzar</a>'
    return texto

@app.route('/comenzar', methods=["GET", "POST"])
def requirements_form():
    # form = RequirementsForm()
    # if form.validate_on_submit():
        # comuna = form.comuna.data
        # ancho = form.ancho.data
        # largo = form.largo.data
        # luz_baja = form.luz_baja.data
        # luz_moderada = form.luz_moderada.data
        # luz_abundante = form.luz_abundante.data
        # riego_bajo = form.riego_bajo.data
        # riego_moderado = form.riego_moderado.data
        # riego_abundante = form.riego_abundante.data
        # arbol = form.arbol.data
        # arbusto = form.arbusto.data
        # cubresuelo = form.cubresuelo.data
        # enredadera = form.enredadera.data
        # floral = form.floral.data
        # frutal = form.frutal.data
        # abejas = form.abejas.data
        # mariposas = form.mariposas.data
        # colibries = form.colibries.data
        # hardiness = form.hardiness.data
        # next = request.args.get('next', None)
        # if next:
            # return redirect(next)
        # return redirect(url_for('next'))
    # return render_template("requirements.html", form=form)
    db = pd.read_csv('src/bdd/plantas.csv')
    return distribuir(db, "Jardin de menor consumo hidrico", 18, 14)