import time

for i in range(1):
    audicao = {}
    pessoas = int(input("Quantas pessoas vão participar? "))
    maior_valor = 0
    pessoa_vencedora = ""

    print("Então vamos Começar")
    for k in range(pessoas):
        pessoa = input("Diga seu nome: ")
        valor = int((input("Quanto quer apostar? ")))
        print("\n"*50)
        audicao[pessoa] = {}
        audicao[pessoa]['valor'] = valor
        if valor > maior_valor:
            maior_valor = valor
            pessoa_vencedora = pessoa
            
    print(f"O vencedor é {pessoa_vencedora} com uma aposta de ${maior_valor}")
    time.sleep(3)
