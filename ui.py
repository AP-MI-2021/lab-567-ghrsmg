# Interfata
from domain import single_reservation
from CRUD import add_wrong_input, remove_not_possible, modify_not_possible


def input_command():
    return input(">>> ")


def string_lower(string):
    x = string.lower()
    return x

def string_split(string):
    x = string_lower(string)
    x = x.split(maxsplit = 1)
    return x

def string_split_for_multiple_commands(stringg):
    string_lower(stringg)
    x = stringg.split('; ')
    return x

def input_reservation():
    """
        Creeaza o rezervare cu date specifice.
    """
    reservation = single_reservation()
    reservation['id'] = (input("ID: "))
    reservation['name'] = (input("Nume: "))
    reservation['class'] = (input("Clasa: "))
    reservation['price'] = (input("Pret: "))
    reservation['checkin'] = input("Check-in: ")

    reservation['checkin'] = string_lower(reservation['checkin'])

    reservation['class'] = string_lower(reservation['class'])

    return reservation


def wrong_input():
    print("Comanda introdusa este gresita, va rugam incercati din nou")


def help():
    print("Pentru lista de comenzi, tastati 'help'")

def cmd_list():
    print()
    print("adauga - pentru a adauga o rezervare noua in lista")
    print("sterge <introdu ID-ul rezervarii> - pentru a elimina o rezervare deja existenta in lista")
    print("modifica <introdu ID-ul rezervarii> - pentru a modifica o datele unei rezervari din lista")
    print("creste <introdu numele pe care s-a facut rezervarea> - creste clasa fiecarei rezervari pe acel nume")
    print("reduce <introdu procent> - ieftineste cu procentul dat toate rezervarile cu check-in facut")
    print("maxim - afiseaza pretul maxim al rezervarilor facute, in functie de clasa")
    print("ordoneaza - ordoneaza descrescator toate rezervarile, in functie de pret")
    print("afiseaza dupa nume - va afisa numele fiecarui client, impreuna cu suma totala a rezervarilor facute de el")
    print("afisare lista - afiseaza lista de rezervari")
    print("undo - anuleaza ultima comanda")
    print("exit - iesirea din program")


def print_by_name(rez_name, rez_price):
    print('Nume:', '\t\tTotal:')
    for i in range(len(rez_name)):
        print(rez_name[i], "\t\t", rez_price[i])

def print_by_class(eco, eco_plus, business):
    print("economy: ", eco)
    print("economy plus: ", eco_plus)
    print("business: ", business)


def print_list(reservations):
    print("ID", "\tNume", "\tClasa", "\tPret", "\tCheck-in")
    for i in range(len(reservations)):
        print(reservations[i]['id'], '\t', reservations[i]['name'], '\t', reservations[i]['class'], '\t', reservations[i]['price'], '\t', reservations[i]['checkin'])