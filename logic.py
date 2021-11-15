from domain import *



def upperclass(nume, lista):
    ok = 0
    for i in range(len(lista)):
        if get_nume(lista[i]) == nume:
            ok = 1
            if lista[i][2] == 'economy':
                lista[i][2] = 'economy plus'
            elif lista[i][2] == 'economy plus':
                lista[i][2] = 'business'
            elif lista[i][2] == 'business':
                pass
    if ok == 0:
        raise ValueError("Nu exista nici o rezervare pe acest nume!")
    return lista


def reducere(lista, p):
    lista_aux = []
    for i in range(len(lista)):
        lista_aux.append(lista[i])
    if p < 0:
        raise ValueError("Procentul reducerii trebuie sa fie unul pozitiv!")
    for i in range(len(lista_aux)):
        if get_checkin(lista_aux[i]) == 'da':
            set_pret(lista_aux[i], get_pret(lista_aux[i]) - p / 100 * get_pret(lista_aux[i]))
    return lista_aux


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
    lista_aux = []
    undoLista = []
    for i in range(len(lista)):
        lista_aux.append(lista[i])
        undoLista.append(lista[i])
    for i in range(len(lista_aux)):
        for j in range(i + 1, len(lista_aux)):
            pret_rez_i = get_pret(lista_aux[i])
            pret_rez_j = get_pret(lista_aux[j])
            if pret_rez_j > pret_rez_i:
                rez_aux = lista_aux[j]
                lista_aux[j] = lista_aux[i]
                lista_aux[i] = rez_aux
    return lista_aux


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

