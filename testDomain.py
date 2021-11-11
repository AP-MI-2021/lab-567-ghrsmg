from domain import *


def testRezervare():
    rezervare = creeazaRezervare("1", "X", "economy", 100, "da")
    assert get_id(rezervare) == "1"
    assert get_nume(rezervare) == "X"
    assert get_clasa(rezervare) == "economy"
    assert get_pret(rezervare) == 100
    assert get_checkin(rezervare) == "da"
