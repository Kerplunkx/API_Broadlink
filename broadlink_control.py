import broadlink
import constantes 

# Conexión al dispositivo Broadlink (verificar direccion ip en archivo de constantes)
def busqueda_dispositivos():
    devices = broadlink.discover(discover_ip_address=constantes.broadcast)
    while(len(devices)==0):
        print("No existen dispositivos disponibles")
        devices = broadlink.discover(discover_ip_address=constantes.broadcast)
    device=devices[0]
    device.auth()
    print("Se ha establecido conexion con dispositivo broadlink")
    return device

# Funciones de control del aire acondicionado (A/C del LST)
def turn_on_AC(device):
    device.send_data(constantes.TURN_ON)
    print("Se ha encendido el aire acondicionado!")

def turn_off_AC(device):
    device.send_data(constantes.TURN_OFF)
    print("Se ha apagado el aire acondicionado!")

def temp_16_AC(device):
    device.send_data(constantes.TEMP_16)
    print("Se ha cambiado la temperatura a 16°C")

def temp_17_AC(device):
    device.send_data(constantes.TEMP_17)
    print("Se ha cambiado la temperatura a 17°C")

def temp_18_AC(device):
    device.send_data(constantes.TEMP_18)
    print("Se ha cambiado la temperatura a 18°C")

def temp_19_AC(device):
    device.send_data(constantes.TEMP_19)
    print("Se ha cambiado la temperatura a 19°C")

def temp_20_AC(device):
    device.send_data(constantes.TEMP_20)
    print("Se ha cambiado la temperatura a 20°C")

def temp_21_AC(device):
    device.send_data(constantes.TEMP_21)
    print("Se ha cambiado la temperatura a 21°C")

def temp_22_AC(device):
    device.send_data(constantes.TEMP_22)
    print("Se ha cambiado la temperatura a 22°C")

def temp_23_AC(device):
    device.send_data(constantes.TEMP_23)
    print("Se ha cambiado la temperatura a 23°C")

def temp_24_AC(device):
    device.send_data(constantes.TEMP_24)
    print("Se ha cambiado la temperatura a 24°C")