# Práctica 2

**Ejercicio 2:** Crear un servidor MODBUS-TCP/IP: **Valor 1.5 punto**

[**SERVER**](ModbusServer.py)

**Ejercicio 3:** Crear un programa cliente MODBUS-TCP/IP que lea el índice y las lecturas de los sensores  de temperatura, presión sistólica y presión diastólica en el banco del servidor creado y coloque su valor en el registro 8, 10, 12 y 14. El cliente debe mostrar los valores leídos también. **Valor 1.5 punto**

[**SOLUCION**](client_ejercicio3.py)

**Ejercicio 4:** Crear un programa cliente MODBUS-TCP/IP que lea el índice y las lecturas de los sensores de temperatura, presión sistólica y presión diastólica en el banco del servidor creado y determine si cada lectura es Baja, Normal o Alta. Este valor determinado será un índice determinado que puede valer 1, 2 o 3 dependiendo si la lectura en cuestión es Baja, Normal o Alta respectivamente. Cada lectura leída desde el servidor debe ser enviada al servidor junto con la lectura-determinada a los registros 8, 9, 10, 11, 12, 13, 14 y 15. El cliente debe mostrar los valores leídos cada vez que ocurra un cambio. El orden en que se mostrará los datos en el servidor será el siguiente: **Valor 2.5 puntos**
* Primera dirección: el índice de medida que se ha tomado
* Segunda dirección: temperatura
* Tercera dirección: el valor del índice-determinado que muestra si la temperatura es
  Baja, Normal o Alta
* Cuarta dirección: presión sistólica
* Quinta dirección: el valor del índice-determinado que muestra si la Presión sistólica
  es Baja, Normal o Alta
* Sexta dirección: presión diastólica
* Séptima dirección: el valor del índice-determinado que muestra si la Presión diastólica
  es Baja, Normal o Alta

[**SOLUCION**](client_ejercicio4.py)

**Ejercicio 5:** Crear un programa cliente MODBUS-TCP/IP que lea el índice y las lecturas de los sensores de temperatura, presión sistólica y presión diastólica en el banco del servidor creado y determine si el paciente tiene sus valores leídos en estado Normal o Alterado. Se considerará Normal cuando todos los valores de los sensores leídos se encuentren entre (36-37), (110-130) y (70-90) respectivamente. Este valor determinado será un índice de normalidad que puede valer 1, 2 dependiendo si el índice-de-normalidad es Normal o Alterado respectivamente. Cada lectura debe ser enviada al servidor junto con el índice de normalidad a los registros 8, 10, 12, 14 y 16. El cliente debe mostrar los valores leídos cada vez que ocurra un cambio. El orden en que se mostrará los datos en el servidor será el siguiente: **Valor 2.5 puntos**
* Primera dirección: el índice de medida que se ha tomado
* Segunda dirección: temperatura
* Tercera dirección: presión sistólica
* Cuarta dirección: presión diastólica
* Quinta dirección: el valor del índice-de-normalidad

[**SOLUCION**](client_ejercicio5.py)

**Ejercicio 6:** Crear un segundo programa cliente MODBUS-TCP/IP que escriba sobre el registro 19 del servidor el valor 66. Nota: debe mantenerse en línea el cliente desarrollado en el Apartado. Para no entrar en conflicto debe crear un archivo cliente con nombre diferente, por ejemplo, al archivo cliente anterior, colóquele un _1 al final. **Valor 1 punto**

[**SOLUCION**](client_ejercicio6.py)