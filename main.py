import broadlink_control as bc
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from conf import config
from mqtt_conf import variables, run_client

temperaturaAC = 20
estadoAC = 0


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


@app.route('/api/v1/ac/variables', methods=['GET'])
def get_variables():
    return jsonify(variables)


@app.route('/api/v1/ac/estado/<estado>', methods=['PATCH'])
def set_estado(estado):
    global estadoAC
    global temperaturaAC
    if int(estado) == 1:
        estadoAC = int(estado)
        temperaturaAC = int(20)
        bc.change_ac_temp(device, 20)
        response = {'Message': 'Se encendio el aire'}
    elif int(estado) == 0:
        estadoAC = int(estado)
        bc.turn_ac(device, "off")
        response = {'Message': 'Se apago el aire'}
    else:
        response = {'Message': 'error (0: apagado, 1: encendido)'}
    return jsonify(response)


@app.route('/api/v1/ac/temp/<temp>', methods=['PATCH'])
def set_temperatura(temp):
    global estadoAC
    if estadoAC == 1:
        global temperaturaAC
        if 16 <= int(temp) <= 24:
            temperaturaAC = int(temp)
            bc.change_ac_temp(device, int(temp))
            response = {'Message': f'Se ha cambiado la temperatura a {temp}'}
        else:
            response = {'Message': 'temperatura fuera del rango (16-24)'}
    else:
        response = make_response(jsonify({'Message': 'Encienda el A/C'}))
        response.status_code = 400
    return response


if __name__ == '__main__':
    device = bc.busqueda_dispositivos()
    if device:
        run_client()
        app.run(host='0.0.0.0', debug=False)
    else:
        print("No se encontraron broadlinks en la red")
