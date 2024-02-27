def timeConversion(s):

    hora = s[-2:]
    valor = int(s[:2])
    if (hora == "PM" and valor != 12):
        valor = valor + 12
        valor = str(valor)

        s = s.replace(s[:2], valor)

        nova_string = s[0:-2]
        #print(nova_string)
        return nova_string


    elif(hora == "AM" and valor == 12):
        valor = str(00)
        valor = valor + "0"

        s = s.replace(s[:2], valor)

        nova_string = s[0:-2]
        #print(nova_string)
        return nova_string

    else:
        nova_string = s[0:-2]
        #print(nova_string )
        return nova_string
    


s = "12:40:22AM"
timeConversion(s)
