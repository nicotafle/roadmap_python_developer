def word_count():
    """
    A seguinte função faz o conteio de palavras numa frase
    ingressada pelo utilizador
    """
    while True:
        try:
            words = str(input("Ingresse uma frase: \n")).lower().split()
            break
        except:
            print("Desculpa, ocorreu um erro!!")

    words_dict = {}
    for i in words:
        words_dict[i] = words_dict.get(i,0) + 1 # retorna valor da chave do dict ou define '0' como padrão  
        ## Da seguinte forma é igual de efetiva ##
        # if i not in words_dict.keys():
        #     words_dict[i] = 1
        # else:
        #     words_dict[i] += 1

    order_dict = {k:v for k, v in sorted(words_dict.items(), key=lambda item: item[1])}
    for key, value in order_dict.items():
        print(f"{key} : {value}")
word_count()