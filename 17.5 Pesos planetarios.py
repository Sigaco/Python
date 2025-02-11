# Pesos planetarios #codedex

peso = float(input("Ingrese su peso en la Tierra:   "))

mercurio = peso * 0.38
venus = peso * 0.91
marte = peso * 0.38
jupiter = peso * 2.34
saturno = peso * 1.06
urano = peso * 0.92
neptuno = peso * 1.19
pluton = peso * 0.06

planeta = str(input("Esribe el planeta del sistema solar al que desea viajar:   "))

if planeta == "mercurio":
    print("Tu peso en Mercurio es de: ", mercurio)
elif planeta == "venus":
    print("Tu peso en Venus es de: ", venus)
elif planeta == "marte":
    print("Tu peso en Marte es de: ", marte)
elif planeta == "jupiter":
    print("Tu peso en Jupiter es de: ", jupiter)
elif planeta == "saturno":
    print("Tu peso en Saturno es de: ", saturno)
elif planeta == "urano":
    print("Tu peso en Urano es de: ", urano)
elif planeta == "neptuno":
    print("Tu peso en Neptuno es de: ", neptuno)
elif planeta == "pluton":
    print("Tu peso en Pluton es de: ", pluton)
else:
    print("Elija un planeta válido")

