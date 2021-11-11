from domain import *


def adaugaRezervare(id, nume, clasa, pret, checkin, lista):
    rezervare = creeazaRezervare(id, nume, clasa, pret, checkin)
    return lista + [rezervare]


def get_by_id(id, lista):
    for rezervare in lista:
        if get_id(rezervare) == id:
            return rezervare
    return None


def stergeRezervare(id, lista):
    return [rezervare for rezervare in lista if get_id(rezervare) != id]


def modificaRezervare(id, nume, clasa, pret, checkin, lista):
    listaNoua = []
    for rezervare in lista:
        if get_id(rezervare) == id:
            rezervareNoua = creeazaRezervare(id, nume, clasa, pret, checkin)
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua
