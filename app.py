from flask import Flask, render_template, request, redirect, Response, session, url_for
from db import *
from cam import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'gokuCrack'


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

        conextion_DB = connectionDB()
        cursor = conextion_DB.cursor(buffered=True)

        cursor.execute("SELECT id FROM Pennyproject WHERE nombre = %s AND apellido = %s", (nombre, apellido))
        registro = cursor.fetchone()
        user = cursor.fetchall()

        if registro:
            alert_message = "El nombre y apellido ya están registrados. Por favor, elige otros."
            return render_template("register.html", alert_message=alert_message)
        else:

            cursor.execute(
                "INSERT INTO Pennyproject(nombre,apellido, img) VALUES (%s, %s, %s)", (nombre, apellido, ""))
            conextion_DB.commit()

            inserted_id = cursor.lastrowid
            user = {
                'id': inserted_id,
                'nombre': nombre,
                'apellido': apellido
            }
            session["user"] = user

            cursor.close()
            conextion_DB.close()

            print("Usuario creado con: Id", inserted_id,  ", Nombre", nombre, ", Apellido", apellido)

            return redirect("/generate")
    else:
        return render_template("register.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
