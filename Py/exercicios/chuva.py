def raindrops(numero):
    raindrop_song = ""
    verificacao = False

    if(numero%3==0):
        raindrop_song+="Pling"
        verificacao = True

    if(numero%5==0):
        raindrop_song+="Plang"
        verificacao = True

    if(numero%7==0):
        raindrop_song+="Plong"
        verificacao = True

    if(verificacao == False):
        raindrop_song = str(numero)

    return raindrop_song


print(raindrops(34))