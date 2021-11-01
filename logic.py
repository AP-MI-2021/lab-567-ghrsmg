import domain

def add_reservation_to_list(reservations):
    reservations.append(domain.input_reservation())
    return reservations


def remove_reservation_from_list(reservations, reservation_index):
    reservations.pop(reservation_index)
    return reservations


def modify_reservation_from_list(reservations, reservation_id):
    reservations_new = []
    for i in range(len(reservations)):
        if reservations[i]['id'] == reservation_id:
            add_reservation_to_list(reservations_new)
        else:
            reservations_new.append(reservations[i])
    return reservations_new

