from CRUD import adaugaRezervare
from logic import upperclass, reducere, maxim_pe_clase, ordonare, sumapreturi
from domain import get_clasa, get_pret, get_id, get_nume


def testUpperClass():
    lista = []
    lista = adaugaRezervare("1", "andrei", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "mihai", "economy plus", 150, "nu", lista)
    upperclass("andrei", lista)
    upperclass("mihai", lista)
    assert get_clasa(lista[0]) == 'economy plus'
    assert get_clasa(lista[1]) == 'business'


def testReducere():
    lista = []
    lista = adaugaRezervare("1", "X", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "Y", "economy plus", 150, "nu", lista)
    rezultat = reducere(lista, 10)
    assert get_pret(rezultat[0]) == 90
    assert get_pret(rezultat[1]) == 150


def testMaximPeClase():
    lista = []
    lista = adaugaRezervare("1", "X", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "Y", "economy plus", 150, "nu", lista)
    lista = adaugaRezervare("3", "Z", "business", 200, "da", lista)
    rezultat = maxim_pe_clase(lista)
    assert rezultat[0] == 100
    assert rezultat[1] == 150
    assert rezultat[2] == 200


def testOrdonare():
    lista = []
    lista = adaugaRezervare("1", "X", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "Y", "economy plus", 150, "nu", lista)
    lista = adaugaRezervare("3", "Z", "business", 200, "da", lista)
    rezultat = ordonare(lista)
    assert get_id(rezultat[0]) == "3"
    assert get_pret(rezultat[0]) == 200
    assert get_nume(rezultat[1]) == "Y"
    assert get_id(rezultat[2]) == "1"


def testSumaPreturi():
    lista = []
    lista = adaugaRezervare("1", "X", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "X", "economy plus", 150, "nu", lista)
    lista = adaugaRezervare("3", "Z", "business", 200, "da", lista)
    nume, preturi = sumapreturi(lista)
    assert nume[0] == "X"
    assert preturi[0] == 250
    assert nume[1] == "Z"
    assert preturi[1] == 200
