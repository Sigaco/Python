# 13. Niveles PH # Codedex

# Programa que determina el nivel de PH de una sustancia

ph = int(input('Introduce el nivel de PH de la sustancia (entre 0 y 14): '))

if ph > 7:
    print('Básico')
elif ph < 7:
    print('Ácido')
else:
    print('Neutro')