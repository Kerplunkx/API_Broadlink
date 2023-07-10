#pip install flask
#pip install flask_cors

import broadlink_control as bc
from flask import Flask
from flask import jsonify
from flask_cors import CORS 
from conf import config

#variables
temperaturaAC=20
estadoAC=0

def create_app(enviroment):
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(enviroment)
    return app

enviroment = config['development']
app = create_app(enviroment)

@app.route('/api/v1/ac/temp', methods=['GET'])
def obtener_temperatura():
    response = {'Message': temperaturaAC}
    return jsonify(response)

@app.route('/api/v1/ac/estado', methods=['GET'])
def obtener_estado():
    response = {'Message': estadoAC}
    return jsonify(response)

@app.route('/api/v1/ac/estado/<estado>', methods=['PATCH'])
def set_estado(estado):
    if int(estado) == 1:
        estadoAC = estado
        bc.temp_20_AC(device)
        response = {'Message': 'success'}
    elif int(estado) == 0:
        estadoAC = estado
        bc.turn_off_AC(device)
        response = {'Message': 'success'}
    else:
        response = {'Message': 'error (0: apagado, 1: encendido)'}
    return jsonify(response)

@app.route('/api/v1/ac/temp/<temp>', methods=['PATCH'])
def set_temperatura(temp):
    global estadoAC
    if estadoAC == 1:
        global temperaturaAC 
        temperaturaAC = temp
        if int(temp)==16:
            bc.temp_16_AC(device)
            response = {'Message': 'success'}
        elif int(temp)==17:
            bc.temp_17_AC(device)
            response = {'Message': 'success'}
        elif int(temp)==18:
            bc.temp_18_AC(device)
            response = {'Message': 'success'}
        elif int(temp)==19:
            bc.temp_19_AC(device)
            response = {'Message': 'success'}
        elif int(temp)==20:
            bc.temp_20_AC(device)
            response = {'Message': 'success'}
        elif int(temp)==21:
            bc.temp_21_AC(device)
            response = {'Message': 'success'}
        elif int(temp)==22:
            bc.temp_22_AC(device)
            response = {'Message': 'success'}
        elif int(temp)==23:
            bc.temp_23_AC(device)
            response = {'Message': 'success'}
        elif int(temp)==24:
            bc.temp_24_AC(device)
            response = {'Message': 'success'}
        else:
            response = {'Message': 'temperatura fuera del rango (16-24)'}
    else:
        response = {'Message': 'Encienda el A/C'}
    return jsonify(response)

if __name__ == '__main__':
    device = bc.busqueda_dispositivos()
    if device:
        app.run(host='0.0.0.0', debug=False)
    else:
        print("No se encontraron broadlinks en la red")