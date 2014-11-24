def genero(gen):
    i = True
    while i==True:
        if gen in ("m", "masculino"):
            msg = "Masculino"
            return msg
        elif gen in ("f", "feminino"):
            msg = "Feminino"
            return msg
        else:
            msg = "Genero invalido, tente novamente!"
            return msg
gen = str(input("Informe seu sexo, sendo ele masculino/feminino: "))
print (genero(gen))

