from time import sleep

from pyModbusTCP.client import ModbusClient

# Creamos cliente ModbusTCP
client = ModbusClient(host="x.x.x.x", port=23456)

# Conectamos el cliente al servidor ModbusTCP
client.open()

# Bucle infinito para ir modificando los registros del servidor
while True:
    data = client.read_holding_registers(0, 20)  # Guardamos los registros en una lista
    print(data)

    client.write_single_register(8, data[0])  # Indice -> reg 8
    client.write_single_register(10, data[1])   # Temperatura -> reg 10
    client.write_single_register(12, data[3])   # Presión sistólica -> reg 12
    client.write_single_register(14, data[5])   # Presión diastólica -> reg 14

    sleep(2.5)