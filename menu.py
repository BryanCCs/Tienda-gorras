import averia
import cliente
import factura
import mecanico
import repuesto
import vehiculo
import random
objetoCliente = cliente.Cliente()
objetoMecanico = mecanico.Mecanico()
objetoVehiculo = vehiculo.Vehiculo()
objetoFactura = factura.Factura()
while True:
    print("----------------Sistema de taller mecanico-------------------")
    print("*******Selecione la opcion adecuada")
    print("1. Agregar clientes")
    print("2. Agregar mecanicos")
    print("3. Agregar vehiculos")
    print("4. Generar factura")
    print("5. Salir del sistema")
    #objetoMecanico.salarioxHora = random.randint(500000,900000)
    #print("numero aleatorio generado: ", random.randint(1,5))
    opcionSeleccionada = int(input())
    if opcionSeleccionada == 1:
        print("********Modulo de clientes*********")
        objetoCliente.cedula = input("Escriba la cedula de cliente ")
        objetoCliente.nombre = input("Escriba el nombre de cliente ")
        objetoCliente.apellidos = input("Escriba los apellidos de cliente ")
        objetoCliente.telefono = input("Escriba el telefono de cliente ")
        objetoCliente.correo = input("Escriba el correo de cliente ")
        objetoCliente.tipo = input("Escriba el tipo de cliente ")
        print("Cliente agregado")
        input()
    elif opcionSeleccionada == 2:
        print("********Modulo de mecanicos*********")
        objetoMecanico.cedula = input("Escriba la cedula de mecanico ")
        objetoMecanico.nombre = input("Escriba el nombre de mecanico ")
        objetoMecanico.apellidos = input("Escriba los apellidos de mecanico ")
        objetoMecanico.telefono = input("Escriba el telefono de mecanico ")
        objetoMecanico.correo = input("Escriba el correo de mecanico ")
        objetoMecanico.especialidad = input("Escriba la especialidad de mecanico ")
        objetoMecanico.salarioxHora = float(input("Escriba el salario por hora de mecanico "))
        print("Mecanico agregado")
        input()
    elif opcionSeleccionada == 3:
        print("********Modulo de vehiculos*********")
        objetoVehiculo.color = input("Escriba el color del vehiculo ")
        objetoVehiculo.marca = input("Escriba la marca del vehiculo ")
        objetoVehiculo.motor = input("Escriba el tipo de motor del vehiculo ")
        objetoVehiculo.placa = input("Escriba la placa del vehiculo ")
        objetoVehiculo.duenno= objetoCliente
        print("Vehiculo agregado")
        input()
    elif opcionSeleccionada == 4:
        print("********Modulo de facturas*********")
        objetoFactura.rellenarEncabezado(input("Escriba la fecha "),input("Escriba el identificador "))
        objetoFactura.vehiculoAtendido = objetoVehiculo
        while True:
            print("****** Averias ********")
            objetoAveria = averia.Averia()
            objetoAveria.identificador = int(input("Escriba el identificador de la averia "))
            objetoAveria.nombre = input("Escriba el nombre de la averia ")
            objetoFactura.agregarAveria(objetoAveria)
            if input("Desea agregar mas averias?") == "No":
                break
        while True:
            
            objetoRepuesto = repuesto.Repuesto()
            objetoRepuesto.identificador = int(input("Escriba el identificador del repuesto "))
            objetoRepuesto.nombre = input("Escriba el nombre del repuesto ")
            objetoRepuesto.marca = input("Escriba la marca del respuesto ")
            objetoRepuesto.precioxUnidad = float(input("Escriba el precio unitario "))
            objetoFactura.agregarRepuesto(objetoRepuesto)
            if input("Desea agregar mas repuestos?") == "No":
                break
        duracionMecanico = float(input("Escriba cuanto duro la reparacion "))
        objetoFactura.asignarMecanicoDuracion(objetoMecanico,duracionMecanico)
        objetoFactura.calculoFinal()
        print("Factura generada correctamente")
        input()
    else:
        print("bye bye")
        break






