def positivo(num):
    if (num > 0):
        msg = "O número é positivo"
        return msg
    else:
        msg = "o número é negativo"
        return msg
        
num = int(input("Informe o número que deseja obter informações: "))


print(positivo(num))
