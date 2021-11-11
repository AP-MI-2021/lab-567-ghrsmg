from testDomain import testRezervare
from testCRUD import test_adauga_rezervare, test_sterge_rezervare


def runAllTests():
    testRezervare()
    test_adauga_rezervare()
    test_sterge_rezervare()
