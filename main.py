from testAll import *
from ui import runMenu
from command_line_console import menu


def main():
    runAllTests()
    x = input("Ce meniu doriti sa folositi:\n"
                 "Apasati '1' pentru meniul vechi\n"
                 "Apasati '2' pentru meniul nou\n" )
    if x == '1':
        runMenu([])
    elif x == '2':
        menu([])
    else:
        print("Eroare! Va rog introduceti '1' sau '2'")





main()
