from config import ORIGEM01, ORIGEM02, DESTINO01, DESTINO02
from remove import remove
from copia import copia
from logs import geraLogs, logFinal, logInicial

def todos(data):
    logInicial()

    remove(DESTINO01)
    message1 = copia(data, ORIGEM01, DESTINO01, "ESTUDOS")
    geraLogs(message1)

    remove(DESTINO02)
    message2 = copia(data, ORIGEM02, DESTINO02, "itsMe")
    geraLogs(message2)

    logFinal()