print('***** Cajero Automatico de Ciudad Gotica *****')
saldo = 1000 # Saldo inicial

salir = False
while not salir:
    print(f'''Operaciones que puedes realizar: 
    1. Consultar Saldo
    2. Retirar
    3. Depositar
    4. Salir''')
    opcion = int(input('Escoje una opcion: '))

    if opcion == 1:
        print(f'Tu saldo actual es: {saldo: .2f}€\n')
    elif opcion == 2:
        retiro = float(input('Ingresa la cantidad a retirar: '))
        # Validacion
        if retiro <= saldo:
               saldo -= retiro # saldo = saldo - retiro
               print(f'Tu nuevo saldo es: {saldo: .2f}€\n')
        else:
               print(f'No cuentas con el saldo suficiente, Tu saldo es: {saldo}')
    elif opcion == 3:
        deposito = float(input('Ingresa la cantidad a depositar: '))
        saldo += deposito # saldo = saldo + deposito
        print(f'Tu nuevo saldo es: {saldo: .2f}€\n')
    elif opcion == 4:
        print('Saliendo del cajero automatico, Hasta pronto!...')
        salir = True
    else:
        print('Opcion invalida. Selecciona otra opcion')