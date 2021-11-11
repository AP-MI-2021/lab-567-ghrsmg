from CRUD import adaugaRezervare, get_by_id, stergeRezervare
from domain import get_id, get_nume, get_pret, get_checkin, get_clasa

def test_adauga_rezervare():
    lista = []
    lista = adaugaRezervare("1", "X", "economy", 100, "da", lista)
    assert get_id(get_by_id("1", lista)) == "1"
    assert get_nume(get_by_id("1", lista)) == "X"
    assert get_clasa(get_by_id("1", lista)) == "economy"
    assert get_pret(get_by_id("1", lista)) == 100
    assert get_checkin(get_by_id("1", lista)) == "da"


def test_sterge_rezervare():
    lista = []
    lista = adaugaRezervare("1", "X", "economy", 100, "da", lista)
    lista = adaugaRezervare("2", "Y", "economy plus", 150, "nu", lista)
    lista = stergeRezervare("1", lista)
    assert len(lista) == 1
    assert get_by_id("1", lista) is None
