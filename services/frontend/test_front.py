#!/usr/bin/python3


from flask import Flask, jsonify,send_from_directory



app = Flask(__name__,static_url_path='/')


patients = {}
patients["patients"] = []
patients["patients"].append({"idpaciente": "AAAAAA", "score": 0.7})
patients["patients"].append({"idpaciente": "BBBBBB", "score": 0.5})
patients["patients"].append({"idpaciente": "CCCCCC", "score": 0.6})
patients["patients"].append({"idpaciente": "EEEEE", "score": 0.87})
patients["patients"].append({"idpaciente": "FFFFF", "score": 0.9})


@app.route("/api/zombiepatients")
def zombie_patients():
    return jsonify(patients)

@app.route("/api/patientpruebas/<idpaciente>")
def patientpruebas(idpaciente):
    pruebas = {}
    pruebas["pruebas"] = []
    pruebas["pruebas"].append({"idpaciente":idpaciente,"fecha":"2019-05-08","name":"prueba1","value":3.6,"unit": "%"})
    pruebas["pruebas"].append({"idpaciente":idpaciente,"fecha":"2019-05-05","name":"prueba2","value":0.69,"unit": "mg/l"})
    pruebas["pruebas"].append({"idpaciente":idpaciente,"fecha":"2019-05-05","name":"prueba3","value":42,"unit": "kbps"})
    pruebas["pruebas"].append({"idpaciente":idpaciente,"fecha":"2019-05-05","name":"prueba4","value":22,"unit": ""})
    pruebas["pruebas"].append({"idpaciente":idpaciente,"fecha":"2019-05-08","name":"prueba5","value":1,"unit": "teslas"})
    return jsonify(pruebas)

@app.route("/")
def sendindex():
    print("SENDING")
    return send_from_directory("www","index.html")


@app.route("/<path:filepath>")
def staticfile(filepath):
    return send_from_directory('www',filepath)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5555)