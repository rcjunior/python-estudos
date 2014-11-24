import math

def area(diametro):
    diametro = diametro/2
    raio = (math.pi*(diametro*diametro))
    raio = round(raio, 2)
    return raio


diametro = int(input("Informe o diametro do circulo: "))

print ("A area do circulo é:", area(diametro))
