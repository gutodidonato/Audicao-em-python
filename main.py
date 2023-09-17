




while True:
    audicao = {}
    pessoas = int(input("Quantas pessoas vão participar? "))
    maior_valor = 0
    pessoa_vencedora = ""

    print("Então vamos Começar")
    for k in range(pessoas):
        pessoa = input("Diga seu nome: ")
        valor = int((input("Quanto quer apostar? ")))
        audicao[pessoa] = {}
        audicao[pessoa]['valor'] = valor
        if valor > maior_valor:
            maior_valor = valor
            pessoa_vencedora = pessoa
            

    print(audicao)
    print(maior_valor)
    print(pessoa_vencedora)