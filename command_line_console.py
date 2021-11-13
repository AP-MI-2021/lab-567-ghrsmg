from ui import *


def help():
    print("Daca doriti sa adaugati o rezervare, tastati in primul rand '1', iar mai apoi "
          "despartite printr-o virgula si fara spatii intre ele: "
          "id-ul, numele, clasa, pretul si checkin-ul")
    print("Daca doriti sa stergeti o rezervare, tastati in primul rand '2', iar mai apoi "
          "id-ul rezervarii pe care doriti sa o stergeti")
    print("Daca doriti sa modificati o rezervare, tastati in primul rand '3', iar mai apoi, "
          "despartite printr-o virgula si fara spatii intre ele: "
          "id-ul, numele, clasa, pretul si checkin-ul")
    print("Daca doriti sa efectuati mai multe comenzi deodata, dati valorile asa cum este specificat mai sus, "
          "iar intre doua comenzi,tastati ';'")
    print("Daca doriti sa va opriti tastati 'x'")


def menu(lista):
    ajutor = input("Daca aveti nevoie de ajutor, tastati 'ajutor': ")
    if ajutor == 'ajutor':
        help()
    while True:
        given_string = input("Dati comenzile: ")
        all_commands = given_string.split(';')
        stop = 0
        for i in range(len(all_commands)):
            command = all_commands[i]
            command = command.split(',')
            if command[0] == '1':
                id = command[1]
                nume = command[2]
                clasa = command[3]
                pret = command[4]
                checkin = command[5]
                lista = adaugaRezervare(id, nume, clasa, pret, checkin,lista)
            elif command[0] == '2':
                id = command[1]
                lista = stergeRezervare(id, lista)
            elif command[0] == '3':
                id = command[1]
                nume = command[2]
                clasa = command[3]
                pret = command[4]
                checkin = command[5]
                lista = modificaRezervare(id, nume, clasa, pret, checkin,lista)
            elif command[0] == 'a':
                showAll(lista)
            elif command[0] == 'x':
                stop = 1
        if stop == 1:
            break
