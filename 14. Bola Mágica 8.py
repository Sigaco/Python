# Bola Mágica 8 #Codedex 💖

import random
num = random.randint(1, 8)

input('Escribe tu pregunta a la bola mágica 8: ')

if num == 1:
  print('Sí, definitivamente')
elif num == 2:
  print('Definitivamente será así')
elif num == 3:
  print('Sin ninguna duda')
elif num == 4:
  print('Respuesta confusa, intentalo de nuevo')
elif num == 5:
  print('Aún no lo veo, pregunta más tarde')
elif num == 6:
  print('Es mejor que no te lo diga ahora')
elif num == 7:
  print('Es posible que no')
else:
  print('Las perspectivas no son muy buenas')

