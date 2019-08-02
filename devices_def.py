# Definición de funciones para distinguir equipos de red

# HP Networks Aruba/Procurve

def hp_networks():
    path = "/cfg/startup-config"
    return path

# Allied Telesis IE300

def at_ie300():
    path = "/flash:/default.cfg"
    return path
#
#
#
#
# Dispositivo no definido

def default():
       return "Dispositivo no definido en la base de datos"

# Estructura de control Switch Case (Construida manualmente ya que Python no la integra)

def switch(case):
    devices = {
        0 : hp_networks(),
        1 : at_ie300(),
    }
    return devices.get(case, default())

# print(switch(2))

