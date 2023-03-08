from pyModbusTCP.client import ModbusClient

# Creamos cliente ModbusTCP
client = ModbusClient(host="x.x.x.x", port=23456)

# Conectamos el cliente al servidor ModbusTCP
client.open()

client.write_single_register(19,22)