with open ('./weather_data.csv') as f:
    lines = f.readlines()
    palavras = []
    
    '''Acumulando as palavras'''
    for i in lines:
        i = i.strip()
        acumulador = ""
        for letra in i:
            if letra != "," and letra != "":
                acumulador += letra
                '''o problema está aqui'''
                if i.index(letra) == i.index(i[len(i) - 1]):
                    palavras.append(acumulador)
                ''' pipi popo popo'''
            elif letra == "," or letra == " ":
                palavras.append(acumulador)
                acumulador = ""
    print(palavras)

    semana = palavras[::3]
    temperatura = palavras[1::3]
    condicao = palavras[2::3]
    
    
    print("\n")
    print(temperatura[1:])
    print(semana[1:])
    print(condicao[1:])
         
         
'''continuando'''
            
            