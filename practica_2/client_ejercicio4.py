from time import sleep

from pyModbusTCP.client import ModbusClient

# Creamos cliente ModbusTCP
client = ModbusClient(host="x.x.x.x", port=23456)

# Conectamos el cliente al servidor ModbusTCP
client.open()

while True:
    data = client.read_holding_registers(0, 20) # Guardamos los registros en una lista
    print(data)

    client.write_single_register(8, data[0])  # Indice -> reg 8

    client.write_single_register(9, data[1])  # Temperatura -> reg 9

    # Alta - Normal - Baja de Temperatura -> reg 10
    if data[1] < 36.5:
        client.write_single_register(10, 1)
    elif data[1] > 37.5:
        client.write_single_register(10, 3)
    else:
        client.write_single_register(10, 2)

    client.write_single_register(11, data[3])  # Presión sistólica -> reg 11

    # Alta - Normal - Baja de presión sistólica -> reg 12
    if data[3] < 80:
        client.write_single_register(12, 1)
    elif data[3] > 120:
        client.write_single_register(12, 3)
    else:
        client.write_single_register(12, 2)

    client.write_single_register(13, data[5])  # Presión diastólica -> reg 13

    # Alta - Normal - Baja de presión diastólica -> reg 14
    if data[5] < 80:
        client.write_single_register(14, 1)
    elif data[5] > 120:
        client.write_single_register(14, 3)
    else:
        client.write_single_register(14, 2)

    sleep(2)