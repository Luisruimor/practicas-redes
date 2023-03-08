# (1) Importamos la libreria ModbusCliente
from pyModbusTCP.client import ModbusClient

# (2)Creamos el cliente ModbusTCP
client = ModbusClient(host="x.x.x.x", port=23456)

# (3)Conectamos el cliente ModbusTCP creado con el servidor ModbusTCP
client.open()

'''
6.1.- Realice un programa cliente que escriba 3 registros sobre el servidor desde la
dirección 10 y el resultado lo muestre el cliente con un mensaje indicativo de la acción
realizada. Para ello el cliente debe leer los 3 registros desde la dirección 10 en el
servidor. Los valores en los registros a insertar son: 10, 11 y 12 respectivamente.
'''
#client.write_multiple_registers(10, [10, 11, 12])
#print("El alumno Luis Ruiz Moreno ha escrito los valores:", client.read_holding_registers(10, 3))

'''
6.2.- Realice un programa cliente que escriba 3 registros sobre el servidor desde la dirección
14 y el resultado lo muestre el servidor con un mensaje indicativo de la acción realizada. El
cliente también debe mostrar el resultado de la acción realizada, y para ello el cliente debe
leer los 3 registros desde la dirección 14 en el servidor. Los valores en los registros a insertar
son: 14, 15 y 16 respectivamente.
'''
# client.write_multiple_registers(14, [14, 15, 16])
# print("El alumno Luis Ruiz Moreno ha escrito los valores:",client.read_holding_registers(14, 3))

'''
6.3.- Realice un programa cliente que escriba 2 registros sobre el servidor desde la dirección 19
y el resultado lo muestre el cliente y el servidor con un mensaje indicativo de la acción realizada
tanto del lado del cliente como del servidor. El programa cliente debe realizar las siguientes 
verificaciones al leer los 2 registros desde el servidor.
'''
client.write_multiple_registers(19, [19, 20])
print("El alumno Luis Ruiz Moreno ha escrito los valores:",client.read_holding_registers(19, 2))

for i in range(19, 21):
    if client.read_holding_registers(i, 1)[0] % 2 == 0:
        print("El registro", i, "es par")
    else:
        print("El registro", i, "es impar")
