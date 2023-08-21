import time
from playsound import playsound

seconds = int(input("Digite o numero de segundos: "))

for i in range(seconds):
    print(str(seconds - i) + " segundos restando...")
    time.sleep(1)


playsound('boom.mp3')
print("Boom Time is Up")