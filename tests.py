# Modulul de teste
from domain import single_reservation
import domain
from ui import input_reservation
import logic

def test_add_reservation(test_reservations, test_reservations_history):
    reservation = single_reservation()
    reservation['id'] = "1"
    reservation['name'] = "A"
    reservation['class'] = "economy"
    reservation['price'] = "10"
    reservation['checkin'] = "da"
    logic.add_reservation_to_list(test_reservations, reservation)
    logic.rez_backup(test_reservations_history, test_reservations)
    assert reservation in test_reservations
    reservation = single_reservation()
    reservation['id'] = "2"
    reservation['name'] = "B"
    reservation['class'] = "economy plus"
    reservation['price'] = "14"
    reservation['checkin'] = "da"
    logic.add_reservation_to_list(test_reservations, reservation)
    logic.rez_backup(test_reservations_history, test_reservations)
    assert reservation in test_reservations
    reservation = single_reservation()
    reservation['id'] = "3"
    reservation['name'] = "C"
    reservation['class'] = "business"
    reservation['price'] = "7"
    reservation['checkin'] = "nu"
    logic.add_reservation_to_list(test_reservations, reservation)
    logic.rez_backup(test_reservations_history, test_reservations)
    assert reservation in test_reservations
    return test_reservations

def test_remove_reservation_from_list(test_reservations, test_reservations_history):
    logic.remove_reservation_from_list(test_reservations, 1)
    logic.rez_backup(test_reservations_history, test_reservations)
    reservation = single_reservation()
    reservation['id'] = "2"
    reservation['name'] = "B"
    reservation['class'] = "economy plus"
    reservation['price'] = "14"
    reservation['checkin'] = "da"
    assert reservation not in test_reservations
    return test_reservations

def test_modify_reservation_from_list(test_reservations, test_reservations_history):
    reservation = single_reservation()
    reservation['id'] = "4"
    reservation['name'] = "D"
    reservation['class'] = "economy"
    reservation['price'] = "20"
    reservation['checkin'] = "da"
    test_reservations = logic.modify_reservation_from_list(test_reservations, 1, reservation)
    logic.rez_backup(test_reservations_history, test_reservations)
    assert reservation in test_reservations
    return test_reservations


def test_lower_if_checkin_done(test_reservations, test_reservations_history):
    logic.lower_if_checkin_done(test_reservations, 10)
    logic.rez_backup(test_reservations_history, test_reservations)
    assert test_reservations[0]['price'] == 18

def test_class_upper(test_reservations, test_reservations_history):
    logic.class_upper(test_reservations, "D")
    logic.rez_backup(test_reservations_history, test_reservations)
    reservation = single_reservation()
    reservation['id'] = "4"
    reservation['name'] = "D"
    reservation['class'] = "economy plus"
    reservation['price'] = 18.0
    reservation['checkin'] = "da"
    assert reservation in test_reservations

def test_max_for_class(test_reservations, test_reservations_history):
    eco, eco_plus, business = logic.max_for_class(test_reservations)
    logic.rez_backup(test_reservations_history, test_reservations)
    assert eco == 0 and eco_plus == 18 and business == 7

def test_sort_reservations_by_price(test_reservations, test_reservations_history):
    logic.sort_reservations_by_price(test_reservations)
    reservation = single_reservation()
    reservation['id'] = "4"
    reservation['name'] = "D"
    reservation['class'] = "economy plus"
    reservation['price'] = 18.0
    reservation['checkin'] = "da"
    assert reservation == test_reservations[0]
    reservation = single_reservation()
    reservation['id'] = "3"
    reservation['name'] = "C"
    reservation['class'] = "business"
    reservation['price'] = "7"
    reservation['checkin'] = "nu"
    assert reservation == test_reservations[1]


def test_undo():
    reservations = []
    reservations_history = [[]]
    reservations.append(input_reservation)
    logic.rez_backup(reservations_history, reservations)
    assert logic.undo(reservations_history, reservations) == []

def testing():
    test_reservations_history = [[]]
    test_reservations = []
    test_add_reservation(test_reservations, test_reservations_history)
    test_remove_reservation_from_list(test_reservations, test_reservations_history)
    test_reservations = test_modify_reservation_from_list(test_reservations, test_reservations_history)
    test_lower_if_checkin_done(test_reservations, test_reservations_history)
    test_class_upper(test_reservations, test_reservations_history)
    test_max_for_class(test_reservations, test_reservations_history)
    test_sort_reservations_by_price(test_reservations, test_reservations_history)
    test_undo()
