import random

def escolher_palavra():
    palavras = ['python', 'programação', 'desenvolvimento', 'jogo', 'computador']
    return random.choice(palavras)

def mostrar_palavra(palavra, letras_acertadas):
    mostrar = ""
    for letra in palavra:
        if letra in letras_acertadas:
            mostrar += letra + " "
        else:
            mostrar += "_ "
    return mostrar.strip()



jogar = True

print("==========JOGO DA FORCA==========")
print("Bem-vindo ao jogo da forca!!" \
"\nVocê tem 6 tentativas para acertar a palavra secreta!!" \
"\nBoa sorte!!")

while jogar:
    palavra = escolher_palavra()
    letras_acertadas = []
    letras_erradas = []
    max_erros = 6

    while max_erros > 0:
        print(mostrar_palavra(palavra, letras_acertadas))
        letra = input("Digite uma letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, digite apenas uma letra, números e caracteres especiais não são permitidos.")
            continue
        elif letra in letras_acertadas or letra in letras_erradas:
            print("Você já tentou essa letra. Tente outra. \nLetras já digitadas: " + ", ".join(letras_acertadas + letras_erradas))
            print("Tentativas restantes: " + str(max_erros))
            continue

        if letra in palavra:
            letras_acertadas.append(letra)
            if "_" not in mostrar_palavra(palavra, letras_acertadas):
                print("Parabéns!! Você acertou a palavra: " + palavra)
                break
             
        else:
            letras_erradas.append(letra)
            max_erros -= 1
            print("Letra incorreta! Você tem " + str(max_erros) + " tentativas restantes.")
            if max_erros == 0:
                print("Infelizmente você perdeu!! \nA palavra certa era: " + palavra)
                break
    jogar = input("Deseja jogar novamente? (s/n): ").lower()
    if jogar != 's':
        jogar = False
        print("Obrigado por jogar!!")