from CRUD import *
from domain import *
from logic import *


def printMenu():
    print("1.Adaugare rezervare")
    print("2.Stergere rezervare")
    print("3.Modificare rezervare")
    print("4.Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară")
    print("a.Afisare rezervari")
    print("x.Iesire")


def uiAdaugaRezervare(lista):
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

    return adaugaRezervare(id, nume, clasa, pret, checkin, lista)


def uiStergeRezervare(lista):
    id = input("Dati id-ul rezervarii de sters: ")
    return stergeRezervare(id, lista)


def uiModificaRezervare(lista):
    id = input("Dati id-ul rezervarii de modificat: ")
    nume = input("Dati noul numele: ")
    clasa = input("Dati noua clasa: ")
    pret = float(input("Dati noul pret: "))
    checkin = input("Dati noul check-in: ")
    return modificaRezervare(id, nume, clasa, pret, checkin, lista)


def uiUpperClass(lista):
    nume = input("Dati numele pe care sunt facute rezervarile:")
    upperclass(nume, lista)
    return lista


def showAll(lista):
    for rezervare in range(len(lista)):
        print(toString(lista[rezervare]))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugaRezervare(lista)
        elif optiune == "2":
            lista = uiStergeRezervare(lista)
        elif optiune == "3":
            lista = uiModificaRezervare(lista)
        elif optiune == "4":
            lista = uiUpperClass(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")
