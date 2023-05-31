from flask import Flask, render_template, request, redirect, Response, session
# from db import *
from cam import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gokuCrack'
app.static_folder = 'static'


@app.route("/")
def index():
    return render_template("home.html")


@app.route("/generate")
def generatePage():
    return render_template("generate.html")


@app.route("/video")
def generate():
    user = session.get("user")
    return Response(generate_frames(user["nombre"], user["apellido"]), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route("/cartoon")
def cartoon():
    path = proceso()
    session["image_path"] = path
    return path


@app.route("/result")
def result():
    image_path = session.get("image_path")
    return render_template("result.html", image_path=image_path)


@app.route("/register", methods=["GET", "POST"])
def registerForm():
    if request.method == "POST":
        nombre = request.form["nombre"].lower().capitalize()
        apellido = request.form["apellido"].lower().capitalize()

        user = {
            'nombre': nombre,
            'apellido': apellido
        }
        session["user"] = user

        print("Usuario creado con Nombre: ", nombre, " y Apellido", apellido)

        return redirect("/generate")
    else:
        return render_template("register.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
