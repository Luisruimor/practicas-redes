from time import sleep

from pyModbusTCP.client import ModbusClient

# Creamos cliente ModbusTCP
client = ModbusClient(host="x.x.x.x", port=23456)

# Conectamos el cliente al servidor ModbusTCP
client.open()

while True:
    data = client.read_holding_registers(0, 20)
    print(data)

    client.write_single_register(8, data[0])  # Indice
    client.write_single_register(10, data[1])  # Temperatura
    client.write_single_register(12, data[3])  # Presión sistólica
    client.write_single_register(14, data[5])  # Presión diastólica

    # Normal(1) o Alterado(2)
    if (37 > data[1] > 36) and (130 > data[3] > 110) and (90 > data[5] > 70):
        client.write_single_register(16, 1)
    else:
        client.write_single_register(16, 2)

    sleep(2)
