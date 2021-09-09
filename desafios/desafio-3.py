def combinar_senha(senha):
    lista_1 = []
    lista_2 = []

    def montar_lista(letra):
        if (not lista_1):
            lista_2.append(letra)
        else:
            for linha in lista_1:
                lista_2.append(linha + letra)

    for i in list(senha):
        montar_lista(i.lower())
        montar_lista(i.upper())
        if   (i.upper() == 'A'): montar_lista("4")
        elif (i.upper() == 'E'): montar_lista("3")
        elif (i.upper() == 'I'): montar_lista("1")
        elif (i.upper() == 'O'): montar_lista("0")
        elif (i.upper() == 'S'): montar_lista("5")

        lista_1 = lista_2[:]
        lista_2.clear()

    print(len(lista_1))

casos = int(input())
cont = int(0)
while (cont < casos):
    senha = input()
    combinar_senha(senha)
    cont += 1