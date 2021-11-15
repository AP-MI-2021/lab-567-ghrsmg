from testDomain import testRezervare
from testCRUD import test_adauga_rezervare, test_sterge_rezervare
from testLogic import testReducere, testUpperClass, testMaximPeClase, testOrdonare, testSumaPreturi
from test_undo_redo import test_undo_redo


def runAllTests():
    testRezervare()
    test_adauga_rezervare()
    test_sterge_rezervare()
    testReducere()
    testMaximPeClase()
    testUpperClass()
    testOrdonare()
    testSumaPreturi()
    test_undo_redo()
