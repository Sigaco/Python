# Adivina el número  #codedex ❤

guess = 0
tries = 0

while guess != 8 and tries < 5:
  guess = int(input('Adivina el número entre 1 a 10: (Tienes 5 intentos):   '))
  # update tries