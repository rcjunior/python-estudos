def calcIr(salario):
    ir = (salario*0.11)
    return ir

def calcInss(salario):
    inss = (salario*0.08)
    return inss

def calcSindicato(salario):
    sindicato = (salario*0.05)
    return sindicato

def calcTotal(salario):    
    sal_liquido = ((calcIr(salario)+calcInss(salario)+calcSindicato(salario)) - salario)
    sal_liquido = (sal_liquido*(-1))
    return sal_liquido

print("Calculo salarial")
salario = float(input("Informe seu salário bruto: "))

print("Seu salário brunto é: " + str(salario))
print("Imposto de Renda: R$", calcIr(salario))
print("INSS: R$ ", calcInss(salario))
print("Sindicato: R$ ", calcSindicato(salario))
print("Salário Liquido: R$ ", calcTotal(salario))
