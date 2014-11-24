def verifica(letra):
    i = True
    letra = letra.lower()
    while i==True:
        if letra in ("a", "e", "i", "o", "u"):
            msg = "A letra '"+str(letra)+"' é uma vogal."
            return msg
        else:
            msg = "A letra é uma consoante."
letra = str(input("Informe a letra que deseja obter informação: "))
print (verifica(letra))

