def calc(peso):
    if peso < 50.00:
        msg = print("Não houve excessos")
        return msg
    elif peso > 50.00:
        multa = 4.00
        totalPeso = (peso - 50.00)
        totalMulta = round((totalPeso * multa), 2)
        msg = "Foram excedidos " + str(totalPeso) + " Kg, dando um total de: R$ " + str(totalMulta)+ "."
        return msg
    
peso = float(input("Informe a quantidade de quilos de peixe: "))

print (calc(peso))
