import random

def jogar():
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")
    
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acertou = False
    
    while not acertou:
        print("\nVocê já fez", tentativas, "tentativa(s).")
        palpite = input("Qual é o seu palpite? ")
        
        try:
            palpite_int = int(palpite)
            
            if palpite_int == numero_secreto:
                print("\nParabéns! Você acertou o número secreto!")
                acertou = True
            elif palpite_int < numero_secreto:
                print("O número que você digitou é menor do que o número secreto.")
            else:
                print("O número que você digitou é maior do que o número secreto.")
            
            tentativas += 1
            
        except ValueError:
            print("\nPor favor, digite um número inteiro válido.")
    
    print("\nFim do Jogo!")

def mostrar_instrucoes():
    print("\nInstruções:")
    print("1. O jogo gera aleatoriamente um número secreto entre 1 e 100.")
    print("2. Você terá que adivinhar o número secreto.")
    print("3. Após cada tentativa, será informado se o seu palpite foi:")
    print("\t- Maior do que o número secreto")
    print("\t- Menor do que o número secreto")
    print("4. Você pode desistir a qualquer momento digitando 'sair'.")
    
if __name__ == "__main__":
    while True:
        mostrar_instrucoes()
        jogar()
        
        opcao = input("\nDeseja jogar novamente? (s/n): ").lower()
        if opcao == 'n':
            break