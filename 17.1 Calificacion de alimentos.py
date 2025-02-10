# 17.1 Calificación de alimentos #Codedex

print('Introduzca su valoración de los siguientes alimentos del 1 al 10: ')
alimento1 = int(input('Que calificación le daría a la leche:  '))
alimento2 = int(input('Que califiación le daría al pan:  '))
alimento3 =int(input('Que calificación le daría a la carne:  '))
alimento4 = int(input('Que calificaciçón le daría las veduras:  '))
alimento5 = int(input('Que calificación le daría a las frutas:  '))
alimento6 = int(input('Que calificación le daría a las legumbres:  '))
alimento7 = int(input('Que calificación le daría a los cereales:  '))
alimento8 = int(input('Que calificación le daría a los huevos:  '))
alimento9 = int(input('Que calificación le daría a los frutos secos:  '))
alimento10 = int(input('Que calificación le daría a los batidos de proteínas:  '))

promedio = (alimento1 + alimento2 + alimento3 + alimento4 + alimento5 + alimento6 + alimento7 + alimento8 + alimento9 + alimento10) / 10

if promedio > 4.5:
    print('su calificación es: Extraordinario')
elif promedio > 4:
    print('su calificación es: Excelente')
elif promedio > 3:
    print('su calificación es: Bueno')
elif promedio > 2:
    print('su calificación es: Regular')
elif promedio > 1:
    print('su calificación es: Malo')
else:
    print('Error de clasificaicón, debe introducir valores numéricos del 1 al 10  ')
