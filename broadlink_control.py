import broadlink
from constantes import actions, temp


def busqueda_dispositivos():
    devices = broadlink.discover()
    while (len(devices) == 0):
        print("No existen dispositivos disponibles")
        devices = broadlink.discover()
    device = devices[0]
    device.auth()
    print("Se ha establecido conexion con dispositivo broadlink")
    return device


def turn_ac(device, action):
    device.send_data(actions[action])
    status = "encendido" if action == "on" else "apagado"
    print(f"Se ha {status} el aire acondicionado!")


def change_ac_temp(device, new_temp):
    device.send_data(temp[new_temp])
    print(f"Se ha cambiado la temperatura a {new_temp}")
