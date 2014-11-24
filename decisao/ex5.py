def nota(nota1, nota2):
    result = (nota1+nota2)/2
    i = True
    while i == True:
        if nota in (0,1,2,3,4,5,6,7,8,9,10):
            if (result >= 10):
                msg = "Aprovado com Distinção"
                return msg
            elif (result <= 7):
                msg = "Reprovado"
                return msg
            else:
                msg = "Aprovado"
                return msg
        else:
            msg = "Valor errado, tente novamente!"
            return msg

def inicio():
    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    print(nota(nota1, nota2))

print (inicio())
    
