def homem(altura):
    ideal = ((72.7*altura)-58)
    ideal = round(ideal, 3)
    msg = "Sua altura ideal é: "+str(ideal)+" kg"
    return msg

def mulher(altura):
    ideal = ((62.1*altura)-44.7)
    ideal = round(ideal, 3)
    msg = "Sua altura ideal é: "+str(ideal)+" kg"
    return msg

i = True
while i == True:
    resp = input("Você é homem ou mulher?")
    
    if resp in ("h", "ho", "hom", "home", "homem"):
        altura = float(input("Informe sua altura: "))
        print (homem(altura))
        i=False
    elif resp in ("m", "mu", "mul", "mulh", "mulhe", "mulher",):
        altura = float(input("Informe sua altura: "))
        print (mulher(altura))
        i=False
    else:
        print("Opção invalida")

cont = input("Deseja continuar? S/N\n")
a = True
while a == True:
    if cont in ("s", "si", "sim"):
        i = True
        import ex13.py
        break
    elif cont in ("n", "nã", "não"):
        print (exit())
        break
    else:
        print ("opção invalida")
