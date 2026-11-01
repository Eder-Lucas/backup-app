from datetime import datetime
from config import ORIGEM01, ORIGEM02, DESTINO01, DESTINO02, LOG_BACKUP
from remove import remove
from copia import copia
import os
import time

def menu():
    print("=== BACKUP PREVENTIVO ===")
    print("[ 1 ] estudos")
    print("[ 2 ] itsMe")
    print("[ 3 ] Todos")
    print("[ 4 ] Consultar logs")

def info():
    menu()
    op = int(input("> "))

    data = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    message = ""

    if op == 1:
        remove(DESTINO01)
        message = copia(data, ORIGEM01, DESTINO01, "ESTUDOS")
    elif op == 2:
        remove(DESTINO02)
        message = copia(data, ORIGEM02, DESTINO02, "itsMe")
    elif op == 3:
        print("Em breve")
        return
    elif op == 4:
        os.startfile(LOG_BACKUP)
        return
    else:
        print("Opção inválida\n")
        return

    print("\r" + " " * 50 + "\rRegistrando Log", end="", flush=True)
    time.sleep(1)

    with open(fr"{LOG_BACKUP}", "a", encoding="utf-8") as txt:
        txt.write(message)

    print("\r" + " " * 50 + "\rBackup realizado!\n")

while True:
    info()