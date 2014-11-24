def conFarenheit(celsius):
    fahrenheit = ((9*celsius + 160)/5)
    return fahrenheit

def conCelsius(fahrenheit):
    celsius = (5/9*(fahrenheit-32))
    return celsius

print("Se deseja converter Celsius para Fahrenheit, aperte C.\n"+
      "Se deseja converter Fahrenheit para Celsius, aperte F.")

i = True
while (i == True):
    resp = input("C/F? ")
    if resp in ("C", "c", "celsius", "cel"):
        celsius = int(input("Informe a temperatura em Celsius: "))
        print(conFarenheit(celsius),"º Fahrenheit")
        break
    elif resp in ("F", "f", "fahrenheit", "faren"):
        fahrenheit = int(input("Informe a temperatura em Fahrenheit: "))
        print (conCelsius(fahrenheit), "º Celsius")
        break
    else:
        print("Opções invalidas, tente novamente")
