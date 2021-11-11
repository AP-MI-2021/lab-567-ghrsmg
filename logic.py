from domain import *


def upperclass(nume, lista):
    for i in range(len(lista)):
        if get_nume(lista[i]) == nume:
            inclass = get_clasa(lista[i])
            print(inclass)
            if inclass == 'economy':
                inclass = 'economy plus'
            elif inclass == 'economy plus':
                inclass = 'business'
            elif inclass == 'business':
                pass
            print(inclass)
            lista[i][2] = inclass
