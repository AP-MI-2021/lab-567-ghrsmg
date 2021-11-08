import domain


def add_wrong_input(reservation):
    """
        In cazul in care datele introduse pentru o rezervare nu sunt corecte, utilizatorul
    va primi un mesaj de eroare in acest sens, explicandu-i care date introduse nu sunt corecte.
    """
    try:
        assert reservation['id'].isnumeric() == True
    except AssertionError:
        return "Campul ID trebuie sa fie de tip int."

    try:
        assert reservation['class'] in ['economy', 'economy plus', 'business']
    except AssertionError:
        return "Campul Clasa trebuie sa fie economy, economy plus, sau business."

    try:
        assert reservation['price'].isnumeric() == True
    except AssertionError:
        return "Campul Pret trebuie sa fie de tip int."

    try:
        assert reservation['checkin'] in ['da', 'nu']
    except AssertionError:
        return "Valoarea introdusa pentru check-in nu este corecta."


def remove_not_possible(reservations, rez_id):
    """
        Explica de ce operatia 'sterge' nu se poate realiza
    """
    try:
        assert type(domain.get_reservation_index(reservations, rez_id)) == int
    except AssertionError:
        return "ID-ul introdus nu corespunde cu nicio rezervare din lista."


def modify_not_possible(reservations, rez_id):
    """
        Explica de ce operatia 'modifica' nu se poate realiza
    """
    res = domain.get_reservation_from_list(reservations, rez_id)
    try:
        assert res in reservations
    except AssertionError:
        return "ID-ul introdus nu corespunde cu nicio rezervare din lista."


def class_upper_not_possible(reservations, rez_name):
    """
        Explica de ce operatia 'creste' nu se poate realiza
    """
    for i in range(len(reservations)):
        if reservations[i]['name'].lower() == rez_name.lower():
            return None
    return "Numele introdus nu corespunde cu nicio rezervare din lista."