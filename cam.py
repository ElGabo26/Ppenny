import cv2
import os
# from db import *
import random
import os

PathPadre = os.path.dirname(os.path.abspath(__file__))
dataPath = PathPadre + '/data'
exportPath = PathPadre + '\static\procesadas'


# Función para capturar video de la webcam
def generate_frames(nombre, apellido):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    personName = nombre + " " + apellido
    personPath = dataPath + '/' + personName

    if not os.path.exists(personPath):
        print('Carpeta Creada: ', personPath)
        os.makedirs(personPath)
    faceClassif = cv2.CascadeClassifier(
        cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            if count >= 300:
                break
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            rostro = auxFrame[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (720, 720),
                                interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count), rostro)
            count += 1

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    cap.release()


def cartoon(numero):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret, frame = cap.read()

    img = frame
    blur_val = 5
    linea = 19
    k = 25
    gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gris_blur = cv2.medianBlur(gris, blur_val)
    edges = cv2.adaptiveThreshold(
        gris_blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, linea, blur_val)
    blurred = cv2.bilateralFilter(img, d=7, sigmaColor=200, sigmaSpace=200)

    qfinal = cv2.bitwise_and(blurred, blurred, mask=edges)
    img = qfinal

    alpha = 1.1  # Factor de contraste
    beta = 30  # Factor de brillo
    gamma = 1.5  # Factor de saturación
    enhanced = cv2.addWeighted(img, alpha, img, 0, beta)
    hsv = cv2.cvtColor(enhanced, cv2.COLOR_BGR2HSV)
    hsv[..., 1] = hsv[..., 1] * gamma
    enhanced = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    # Mostrar imagen original y mejorada
    cv2.imwrite(exportPath + "/foto_{}.jpg".format(numero), enhanced)
    cap.release()

    return "../static/procesadas/"+"/foto_{}.jpg".format(numero)


def aleatorio():
    return random.randint(1, 100)


def proceso():
    numero = aleatorio()
    return cartoon(numero)
