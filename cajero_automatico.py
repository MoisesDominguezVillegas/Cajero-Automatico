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

