# Prelucrare rezervari
import domain
import ui
from copy import deepcopy


def add_reservation_to_list(reservations, reservation):
    reservations.append(reservation)
    return reservations


def remove_reservation_from_list(reservations, reservation_index):
    reservations.pop(reservation_index)
    return reservations


def modify_reservation_from_list(reservations, reservation_id, res):
    reservations_new = []
    for i in range(len(reservations)):
        if int(reservations[i]['id']) == int(reservation_id):
            add_reservation_to_list(reservations_new, res)
        else:
            reservations_new.append(reservations[i])
    return reservations_new


def class_upper(reservations, name):
    for i in range(len(reservations)):
        if reservations[i]['name'].lower() == name.lower():
            rez_class = domain.get_reservation_class(reservations, i)
            if rez_class == 'economy':
                rez_class = 'economy plus'
            elif rez_class == 'economy plus':
                rez_class = 'business'
            elif rez_class == 'business':
                pass
            else:
                raise ValueError('Clasa rezervarii nu a fost introdusa corect.')
            reservations[i]['class'] = rez_class


def lower_if_checkin_done(reservations, percentage):
    for i in range(len(reservations)):
        if reservations[i]['checkin'] == 'da':
            price = int(domain.get_reservation_price(reservations, i))
            price = price - (price * percentage) / 100
            reservations[i]['price'] = price
    return reservations


def max_for_class(reservations):
    max_eco = 0
    max_eco_plus = 0
    max_business = 0
    for i in range(len(reservations)):
        if reservations[i]['class'] == 'economy':
            rez_price = int(domain.get_reservation_price(reservations, i))

            if rez_price > max_eco:
                max_eco = rez_price

        elif reservations[i]['class'] == 'economy plus':
            rez_price = int(domain.get_reservation_price(reservations, i))

            if rez_price > max_eco_plus:
                max_eco_plus = rez_price

        else:
            rez_price = int(domain.get_reservation_price(reservations, i))

            if rez_price > max_business:
                max_business = rez_price

    return max_eco, max_eco_plus, max_business


def sort_reservations_by_price(reservations):
    for i in range(len(reservations)):
        for j in range(i, len(reservations)):
            rez_price_i = int(domain.get_reservation_price(reservations, i))
            rez_price_j = int(domain.get_reservation_price(reservations, j))
            if rez_price_j > rez_price_i:
                rez_aux = reservations[j]
                reservations[j] = reservations[i]
                reservations[i] = rez_aux
    return reservations


def sum_of_rez_prices_by_name(reservations):
    rez_name = []
    rez_price = []
    for i in range(len(reservations)):
        if reservations[i]['name'] not in rez_name:
            rez_name.append(reservations[i]['name'])
            rez_price.append(0)

    for i in range(len(rez_name)):
        for j in range(len(reservations)):
            if reservations[j]['name'] == rez_name[i]:
                rez_price[i] = rez_price[i] + int(reservations[j]['price'])
    return rez_name, rez_price


def rez_backup(reservations_history, reservations):
    reservations_history.append(deepcopy(reservations))


def undo(reservations_history, reservations):
    if len(reservations_history) > 2:
        reservations_history.pop(-1)
        return reservations_history.pop(-1)
    else:
        return reservations_history[0]