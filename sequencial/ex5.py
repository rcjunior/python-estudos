def metro_cent(metro):
    cent = (metro*100)
    msg = str(cent) + " cm"
    return msg

metro = int(input("Informe os metros: "))

print (metro_cent(metro))
