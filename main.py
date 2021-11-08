import domain
import ui
import logic
import CRUD
import tests


def Start():
    reservations_history = [[]]
    reservations = []
    ui.help()

    tests.testing()

    while True:

        command = ui.input_command()
        command_mul = ui.string_split_for_multiple_commands(command)

        if command != command_mul:

            for cmd in command_mul:

                cmd = ui.string_split(cmd)

                if cmd[0] == 'help':
                    ui.cmd_list()


                elif cmd[0] == 'adauga':
                    res = ui.input_reservation()
                    if CRUD.add_wrong_input(res) == None:
                        logic.add_reservation_to_list(reservations, res)
                        logic.rez_backup(reservations_history, reservations)
                    else:
                        print(CRUD.add_wrong_input(res))


                elif cmd[0] == 'sterge':
                    res_id = int(cmd[1])
                    if CRUD.remove_not_possible(reservations, res_id):
                        res_index = domain.get_reservation_index(reservations, res_id)
                        logic.remove_reservation_from_list(reservations, res_index)
                        logic.rez_backup(reservations_history, reservations)
                    else:
                        print(CRUD.remove_not_possible(reservations, res_id))


                elif cmd[0] == 'modifica':
                    res_id = int(cmd[1])
                    if CRUD.modify_not_possible(reservations, res_id):
                        res = ui.input_reservation()
                        reservations = logic.modify_reservation_from_list(reservations, res_id, res)
                        logic.rez_backup(reservations_history, reservations)
                    else:
                        print(CRUD.modify_not_possible(reservations, res_id))


                elif cmd[0] == 'creste':
                    if CRUD.class_upper_not_possible(reservations, cmd[1]) == None:
                        logic.class_upper(reservations, cmd[1])
                        logic.rez_backup(reservations_history, reservations)
                    else:
                        print(CRUD.class_upper_not_possible(reservations, cmd[1]))

                elif cmd[0] == 'reduce':
                    if cmd[1].isnumeric():
                        proc = int(cmd[1])
                        logic.lower_if_checkin_done(reservations, proc)
                        logic.rez_backup(reservations_history, reservations)
                    else:
                        ui.wrong_input()


                elif cmd[0] == 'maxim':
                    eco, eco_plus, business = logic.max_for_class(reservations)
                    ui.print_by_class(eco, eco_plus, business)

                elif cmd[0] == 'ordoneaza':
                    reservations = logic.sort_reservations_by_price(reservations)

                elif cmd[0] == 'afiseaza':
                    rez_name, rez_price = logic.sum_of_rez_prices_by_name(reservations)
                    ui.print_by_name(rez_name, rez_price)

                elif cmd[0] == 'afisare':
                    ui.print_list(reservations)

                elif cmd[0] == 'undo':
                    reservations = logic.undo(reservations_history, reservations)

                elif cmd[0] == 'exit':
                    return

                else:
                    ui.wrong_input()


        else:
            cmd = ui.string_split(command)

            if cmd[0] == 'help':
                ui.cmd_list()


            elif cmd[0] == 'adauga':
                res = ui.input_reservation()
                if CRUD.add_wrong_input(res) == None:
                    logic.add_reservation_to_list(reservations, res)
                    logic.rez_backup(reservations_history, reservations)
                else:
                    print(CRUD.add_wrong_input(res))


            elif cmd[0] == 'sterge':
                res_id = int(cmd[1])
                if CRUD.remove_not_possible(reservations, res_id) == None:
                    logic.remove_reservation_from_list(reservations, res_id)
                    logic.rez_backup(reservations_history, reservations)
                else:
                    print(CRUD.remove_not_possible(reservations, res_id))


            elif cmd[0] == 'modifica':
                res_id = int(cmd[1])
                if CRUD.modify_not_possible(reservations, res_id) == None:
                    logic.modify_reservation_from_list(reservations, res_id)
                    logic.rez_backup(reservations_history, reservations)
                else:
                    print(CRUD.modify_not_possible(reservations, res_id))


            elif cmd[0] == 'creste':
                if CRUD.class_upper_not_possible(reservations, cmd[1]) == None:
                    logic.class_upper(reservations, cmd[1])
                    logic.rez_backup(reservations_history, reservations)
                else:
                    print(CRUD.class_upper_not_possible(reservations, cmd[1]))

            elif cmd[0] == 'reduce':
                if cmd[1].isnumeric():
                    proc = int(cmd[1])
                    logic.lower_if_checkin_done(reservations, proc)
                    logic.rez_backup(reservations_history, reservations)
                else:
                    ui.wrong_input()


            elif cmd[0] == 'maxim':
                eco, eco_plus, business = logic.max_for_class(reservations)
                ui.print_by_class(eco, eco_plus, business)

            elif cmd[0] == 'ordoneaza':
                reservations = logic.sort_reservations_by_price(reservations)

            elif cmd[0] == 'afiseaza':
                rez_name, rez_price = logic.sum_of_rez_prices_by_name(reservations)
                ui.print_by_name(rez_name, rez_price)

            elif cmd[0] == 'afisare':
                ui.print_list(reservations)

            elif cmd[0] == 'undo':
                reservations = logic.undo(reservations_history, reservations)

            elif cmd[0] == 'exit':
                return

            else:
                ui.wrong_input()


Start()