def calc(altura):
    ideal = ((72.7*altura)-58)
    return ideal

altura = float(input("Informe sua altura, utlizando x.yy, sendo x o metro e y os centimetros: "))
print (calc(altura))
