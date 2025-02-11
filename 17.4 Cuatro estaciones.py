# Cuatro estaciones  #codedex

mes = str(input('Ingrese el mes:  '))

if mes == 'enero' or mes == 'febrero' or mes == 'marzo':
    print('Estamos en invierno ❄')
elif mes == 'abril' or mes == 'mayo' or mes == 'junio':
    print('Estamos en primavera 🌸')
elif mes == 'julio' or mes == 'agosto' or mes == 'septiembre':
    print('Estamos en verano 🏖')
elif mes == 'octubre' or mes == 'noviembre' or mes == 'diciembre':
    print('Estamos en otoño 🍂')
else:
    print('Introduzca un mes válido')