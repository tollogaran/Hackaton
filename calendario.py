from flask import Flask,request,render_template,jsonify
import requests
import logging
app=Flask(__name__)


@app.route("/home")
def bienvenida():
    return render_template("template_homeb.html",**params)


@app.route("/api/<usuario>/<sala>/<hora_inicio>/<duracion>/<tamaño>")
def reservacion(usuario,sala,hora_inicio,duracion,tamaño):
    params=info_reservacion(usuario,sala,hora_inicio,duracion,tamaño)
    return jsonify(params)

def info_reservacion(usuario,sala,hora_inicio,duracion,tamaño):
    params={"datos_api"}
    response=requests.get("url",params)

    if response.status_code==200:
        print(response.text)
    else:
        print("Error")

    params={"usuario":v_usuario,
    "sala":v_sala,
    "hora_inicio":v_horaini,
    "duracion":v_duracion,
    "tamaño":v_tamaño
    }


if __name__=="__main__":
    app.run(debug=True)
