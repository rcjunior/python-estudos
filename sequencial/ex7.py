def area(lado1, lado2):
    area = lado1*lado2
    area = area*2
    return area

lado1 = int(input("Informe o valor do primeiro lado: "))
lado2 = int(input("Informe o valor do segundo lado: "))

print ("O resultado sera: ", area(lado1, lado2))
