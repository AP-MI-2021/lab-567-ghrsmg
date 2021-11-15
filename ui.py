from copy import deepcopy

from CRUD import *
from logic import *



def printMenu():
    print("1.Adaugare rezervare")
    print("2.Stergere rezervare")
    print("3.Modificare rezervare")
    print("4.Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("5.Reducerea preturilor biletelor cu checkin-ul facut")
    print("6.Afisarea preturilor maxime pe clase ")
    print("7. Ordonarea rezervarilor descrescator")
    print("8. Afisarea sumelor preturilor pentru fiecare nume")
    print("u.Undo")
    print("r.Redo")
    print("a.Afisare rezervari")
    print("x.Iesire")


def uiAdaugaRezervare(lista, undoLista, redoLista):
    try:
        id = input("Dati id-ul: ")
        nume = input("Dati numele: ")
        clasa = input("Dati clasa: ")
        pret = float(input("Dati pret: "))
        checkin = input("Dati check-in: ")
        while clasa not in ['economy', 'economy plus', 'business']:
            print("Clasele disponibile sunt economy, economy plus sau business")
            clasa = input("Dati clasa: ")
        while checkin not in ['da', 'nu']:
            checkin = input("Dati check-in: ")
            print("Datele introduse sunt gresite")
        rezultat = adaugaRezervare(id, nume, clasa, pret, checkin, lista)
        undoLista.append(lista)
        redoLista.clear()
        return rezultat

    except ValueError as ve:
        print("Eroare : {}".format(ve))
        return lista


def uiStergeRezervare(lista, undoLista, redoLista):
    try:
        id = input("Dati id-ul rezervarii de sters: ")
        rezultat = stergeRezervare(id, lista)
        undoLista.append(lista)
        redoLista.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare : {}".format(ve))
        return lista


def uiModificaRezervare(lista, undoLista, redoLista):
    try:
        id = input("Dati id-ul rezervarii de modificat: ")
        nume = input("Dati noul numele: ")
        clasa = input("Dati noua clasa: ")
        pret = float(input("Dati noul pret: "))
        checkin = input("Dati noul check-in: ")
        rezultat = modificaRezervare(id, nume, clasa, pret, checkin, lista)
        undoLista.append(lista)
        redoLista.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare : {}".format(ve))
        return lista


def uiUpperClass(lista, undoLista, redoLista):
    try:
        nume = input("Dati numele pe care sunt facute rezervarile:")
        listaInitiala= deepcopy(lista)
        rezultat = upperclass(nume, lista)
        undoLista.append(listaInitiala)
        redoLista.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare : {}".format(ve))
        return lista


def uiReducere(lista, undoLista, redoLista):
    try:
        p = int(input("Dati procentul cu care se vor ieftini biletele: "))
        listaInitiala= deepcopy(lista)
        undoLista.append(listaInitiala)
        reducere(lista, p)
        redoLista.clear()


    except ValueError as ve:
        print("Eroare : {}".format(ve))



def uiMaxim_pe_clase(lista):
    x, y, z = maxim_pe_clase(lista)
    print("economy: ", x)
    print("economy plus", y)
    print("business", z)


def uiOrdonare(lista, undoLista, redoLista):
    rezultat = ordonare(lista)
    undoLista.append(lista)
    redoLista.clear()
    return rezultat


def uiSumaPreturi(lista):
    print("Nume:", "\t\tTotal")
    x, y = sumapreturi(lista)
    for i in range(len(x)):
        print(x[i], "\t\t", y[i])


def showAll(lista):
    for rezervare in range(len(lista)):
        print(toString(lista[rezervare]))


def runMenu(lista):
    undoLista = []
    redoLista = []
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaRezervare(lista, undoLista, redoLista)
        elif optiune == "2":
            lista = uiStergeRezervare(lista, undoLista, redoLista)
        elif optiune == "3":
            lista = uiModificaRezervare(lista, undoLista, redoLista)
        elif optiune == "4":
            lista = uiUpperClass(lista, undoLista, redoLista)
        elif optiune == "5":
            uiReducere(lista, undoLista, redoLista)
        elif optiune == "6":
            lista = uiMaxim_pe_clase(lista)
        elif optiune == "7":
            lista = uiOrdonare(lista, undoLista, redoLista)
        elif optiune == "8":
            uiSumaPreturi(lista)
        elif optiune == "u":
            if len(undoLista) > 0:
                redoLista.append(lista)
                lista = undoLista.pop()
            else:
                print("Nu se poate face undo!")
        elif optiune == "r":
            if len(redoLista) > 0:
                undoLista.append(lista)
                lista = redoLista.pop()
            else:
                print("Nu se poate face redo!")
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
