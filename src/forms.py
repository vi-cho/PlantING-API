from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, SelectField, IntegerField, \
    BooleanField, RadioField
from wtforms.validators import DataRequired, Email, Length


def lista_comunas():
    comunas = []
    with open("src/bdd/comunas.csv", "r") as archivo_comunas:
        lineas = archivo_comunas.readlines()
    for linea in lineas:
        lista_ind = linea.strip().split(";")
        comunas.append(lista_ind[1])
    return comunas

def hardiness_zones():
    return ["Zona 1A", "Zona 1B", "Zona 2A", "Zona 2B", "Zona 3A", 
            "Zona 3B", "Zona 4A", "Zona 4B", "Zona 5A", "Zona 5B", 
            "Zona 6A", "Zona 6B", "Zona 7A", "Zona 7B", "Zona 8A", 
            "Zona 8B", "Zona 9A", "Zona 9B", "Zona 10A", "Zona 10A", "Zona 11A"]

class RequirementsForm(FlaskForm):
    comuna = SelectField('Comuna', choices=lista_comunas())
    ancho = IntegerField('Ancho del jardin')
    largo = IntegerField('Largo del jardin')
    luz_baja = BooleanField('Baja')
    luz_moderada = BooleanField('Moderada')
    luz_abundante = BooleanField('Abundante')
    riego_bajo = BooleanField('Bajo')
    riego_moderado = BooleanField('Moderado')
    riego_abundante = BooleanField('Abundante')
    arbol = BooleanField('Arbol')
    arbusto = BooleanField('Arbusto')
    cubresuelo = BooleanField('Cubresuelo')
    enredadera = BooleanField('Enredadera')
    floral = BooleanField('Floral')
    frutal = BooleanField('Frutal')
    abejas = BooleanField('Abejas')
    mariposas = BooleanField('Mariposas')
    colibries = BooleanField('Colibríes (y otras aves)')
    hardiness = RadioField('Zona de resistencia al frio (Hardiness Zone)', choices=hardiness_zones())
    submit = SubmitField('Diseñar jardines')