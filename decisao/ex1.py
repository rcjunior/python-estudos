def maior(priNum, segNum):
    if (priNum > segNum):
        msg = "O primeiro número é maior que o segundo número."
        return msg
    elif(priNum == segNum):
        msg = "O primeiro número tem o mesmo valor que o segundo"
        return msg
    else:
        msg = "O segundo número é maior que o primeiro número"
        return msg


priNum = int(input("Digite o primeiro número: "))
segNum = int(input("Digite o segundo número: "))

print(maior(priNum, segNum))
