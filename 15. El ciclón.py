#El ciclón #Codedex 💖

altura = int(input('Cuál es tu altura?: '))
saldo = int(input('Cuánto dinero llevas?: '))

if altura >= 137 and saldo >= 10:
  print('Disfruta del viaje!')
elif altura < 137 and saldo >= 10:
  print('No tienes altura suficiente')
elif saldo < 10 and altura >= 137:
  print('No tienes suficiente dinero')
else:
  print('Tienes que crecer y ahorrar')