from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    texto = '<p>Bienvenido a PlantING!</p>\n<a href="/comenzar">Comenzar</a>'
    return texto

@app.route('/comenzar', methods=["GET", "POST"])
def requirements_form():
    return '<p>Aca se mostrara el formulario</p>'