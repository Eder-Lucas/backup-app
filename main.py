from datetime import datetime
from config import ORIGEM01, ORIGEM02, DESTINO01, DESTINO02, LOG_BACKUP
import shutil
import os
import stat
import time

def apagar(func, caminho, exc_func):
    os.chmod(caminho, stat.S_IWRITE)
    func(caminho)

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
        print("Removendo backup antigo", end="")
        shutil.rmtree(DESTINO01, onexc=apagar)

        print("\r" + " " * 40 + "\rCopiando...", end="", flush=True)

        shutil.copytree(ORIGEM01, DESTINO01, ignore=shutil.ignore_patterns('.git'))

        message = f"\n{data}: itsMe salva no backup"
    elif op == 2:
        print("Removendo backup antigo", end="")
        shutil.rmtree(DESTINO02, onexc=apagar)

        print("\r" + " " * 40 + "\rCopiando...", end="", flush=True)

        shutil.copytree(ORIGEM02, DESTINO02, ignore=shutil.ignore_patterns('.git'))

        message = f"\n{data}: itsMe salva no backup"
    elif op == 3:
        print("Em breve")
        return
    elif op == 4:
        print("Em breve")
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