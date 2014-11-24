def salario(ganho, hora):
    salario = ganho*hora
    return salario

ganho = int(input("Informe quantos vc ganha por hora: "))
hora = int(input("Informe quantoas horas vc trabalha por mês: "))

print ("Você recebe R$",salario(ganho, hora), "por hora trabalhada")
