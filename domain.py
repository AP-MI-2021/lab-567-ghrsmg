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


def yes_no_to_bool(checkin):
    if checkin == 'yes':
        return True

    elif checkin == 'no':
        return False

    else:
        return


def string_lower(checkin):
    x = checkin.lower()
    return x


def input_reservation():
    """
        Creeaza o rezervare cu date specifice.
    """
    reservation = single_reservation()
    reservation['id'] = int(input("ID: "))
    reservation['name'] = str(input("Name: "))
    reservation['class'] = str(input("Class: "))
    reservation['price'] = int(input("Price: "))
    reservation['checkin'] = input("Check-in: ")

    reservation['checkin'] = string_lower(reservation['checkin'])
    reservation['checkin'] = yes_no_to_bool(reservation['checkin'])

    reservation['class'] = string_lower(reservation['class'])

    return reservation


def get_reservation_index(reservations, reservation_id):
    for i in len(reservations):
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


def set_reservation_type_to_predefined(reservations, index, type, predefined):
    reservations[index][type] = predefined
    return reservations[index][type]
