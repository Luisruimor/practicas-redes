from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform

# create an instance of Modbusserver
server = ModbusServer("x.x.x.x", 23456, no_block=True)

try:
    print("Start server...")
    server.start()
    print("Server is on line")
    state = [0]
    while True:
        DataBank.set_words(1, [int(uniform(0, 100))])
        if state != DataBank.get_words(19, 1):
            state = DataBank.get_words(19, 2)
            print("value register 19 has changed to " + str(state))
            sleep(3)
except:
    print("Shutdown server...")
    server.stop()
    print("Server is offline")
