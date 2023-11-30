from paho.mqtt import client as mqtt_client

BROKER = '200.126.14.229'
PORT = 1883
BASE_TOPIC = 'dschica/estacion/'
USERNAME = 'YOUR_USERNAME'
PASSWORD = 'YOUR_PASSWORD'
BASE_TOPIC_2 = 'aclearn/'

variables = {"temperatura": "", "humedad": "",
             "velocidad": "", "votos": "", "ocupancia": ""}


def connect_mqtt() -> mqtt_client:
    def on_connect(client, usedata, flags, rc):
        if rc == 0:
            print('Conectado a Broker MQTT')
        else:
            print('La conexion al Broker ha fallado')

    client = mqtt_client.Client("estacion_id")
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect
    client.connect(BROKER, PORT)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        topic = msg.topic.split("/")[-1]
        global variables
        variables[topic] = msg.payload.decode()
    client.subscribe([(BASE_TOPIC + "temperatura", 0),
                     (BASE_TOPIC + "humedad", 0),
                     (BASE_TOPIC + "velocidad", 0),
                     (BASE_TOPIC_2 + "votos", 0),
                     (BASE_TOPIC_2 + "ocupancia", 0)])
    client.on_message = on_message


def run_client():
    client = connect_mqtt()
    subscribe(client)
    client.loop_start()
