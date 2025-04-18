import random

numero_secreto = random.randint(1, 100)

print("🔐 JOGO DO NÚMERO SECRETO – MODO INSANO 😈")
print("Adivinhe o número entre 1 e 100")
print("Você tem 5 tentativas! Boa sorte...\n")

tentativas = 0
max_tentativas = 5

for i in range(max_tentativas):
    chute = int(input(f"🎯 Tentativa {tentativas + 1}: "))

    if chute < 1 or chute > 100:
        print("🚫 Fora do intervalo! Tente um número entre 1 e 100.\n")
        continue  # não conta como tentativa

    tentativas += 1

    if chute == numero_secreto:
        print("🎉 ACERTOU MISERÁVEEL!!! Você é um gênio! 😍")
        break
    elif chute < numero_secreto:
        print("🔼 Errou! O número é MAIOR.\n")
    else:
        print("🔽 Errou! O número é MENOR.\n")

    if tentativas == max_tentativas:
        print(f"💀 Fim de jogo! O número secreto era {numero_secreto}.")
