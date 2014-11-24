def calcUm(num1, num2):
    a = (num1*2) + (num2/2)
    msg = ("O produto do dobro do primeiro com metade do segundo é:"+ str(a))
    return msg

def calcDois(num1, num3):
    b = ((num1*3) + num3)
    msg = ("A soma do triplo do primeiro com o terceiro é:"+ str(b))
    return msg

def calcTres(num3):
    c = num3**3
    msg = ("O terceiro elevado ao cubo é:"+ str(c))
    return msg
    
num1 = int(input("Informe o primeiro número, sendo ele um inteiro: "))
num2 = int(input("Informe o segundo número, sendo ele um inteiro: "))
num3 = float(input("Informe o terceiro número, sendo ele um número real: "))

print (calcUm(num1, num2))
print (calcDois(num1, num3))
print (calcTres(num3))
