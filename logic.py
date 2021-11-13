from domain import *


def upperclass(nume, lista):
    ok = 0
    for i in range(len(lista)):
        if get_nume(lista[i]) == nume:
            ok = 1
            inclass = get_clasa(lista[i])
            if inclass == 'economy':
                inclass = 'economy plus'
            elif inclass == 'economy plus':
                inclass = 'business'
            elif inclass == 'business':
                pass
            lista[i][2] = inclass
    if ok == 0:
        raise ValueError("Nu exista nici o rezervare pe acest nume!")


def reducere(lista, p):
    if p < 0:
        raise ValueError("Procentul reducerii trebuie sa fie unul pozitiv!")
    for i in range(len(lista)):
        if get_checkin(lista[i]) == 'da':
            lista[i][3] = lista[i][3] - p / 100 * lista[i][3]
    return lista


def maxim_pe_clase(lista):
    max_economy = 0
    max_economy_plus = 0
    max_business = 0
    for i in range(len(lista)):
        if lista[i][2] == 'economy':
            pret_rez = get_pret(lista[i])
            if pret_rez > max_economy:
                max_economy = pret_rez
        if lista[i][2] == 'economy plus':
            pret_rez = get_pret(lista[i])
            if pret_rez > max_economy_plus:
                max_economy_plus = pret_rez
        if lista[i][2] == 'business':
            pret_rez = get_pret(lista[i])
            if pret_rez > max_business:
                max_business = pret_rez
    return max_economy, max_economy_plus, max_business


def ordonare(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            pret_rez_i = get_pret(lista[i])
            pret_rez_j = get_pret(lista[j])
            if pret_rez_j > pret_rez_i:
                rez_aux = lista[j]
                lista[j] = lista[i]
                lista[i] = rez_aux
    return lista


def sumapreturi(lista):
    nume_rezervari = []
    pret_rezervari = []
    for i in range(len(lista)):
        if lista[i][1] not in nume_rezervari:
            nume_rezervari.append(lista[i][1])
            pret_rezervari.append(0)
    for i in range(len(nume_rezervari)):
        for j in range(len(lista)):
            if lista[j][1] == nume_rezervari[i]:
                pret_rezervari[i] = pret_rezervari[i] + float(lista[j][3])
    return nume_rezervari, pret_rezervari
