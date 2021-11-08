# Rezervarile si implementarea lor

def single_reservation():
    """
        Creeaza o rezervare ca instanta, intr-un dictionar.
    """
    return {
        'id' : int,
        'name' : str,
        'class' : str,
        'price' : int,
        'checkin' : bool
    }




"""
    Getteri si setteri
"""


def get_reservation_index(reservations, reservation_id):
    for i in range(len(reservations)):
        if reservations[i]['id'] == reservation_id:
            return i
    return False

def get_reservation_id(reservations,  index):
    return reservations[index]['id']

def get_reservations_name(reservations, index):
    return reservations[index]['name']

def get_reservation_class(reservations, index):
    return reservations[index]['class']

def get_reservation_price(reservations, index):
    return reservations[index]['price']

def get_reservation_checkin(reservations, index):
    return reservations[index]['checkin']


def get_reservation_from_list(reservations, reservation_id):
    for i in range(len(reservations)):
        if reservations[i]['id'] == reservation_id:
            return reservations[i]


def set_reservation_type_to_predefined(reservations, index, type, predefined):
    reservations[index][type] = predefined
    return reservations[index][type]