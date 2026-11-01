import time
from config import LOG_BACKUP

def geraLogs(message):
    print("\r" + " " * 50 + "\rRegistrando Log", end="", flush=True)
    time.sleep(1)

    with open(fr"{LOG_BACKUP}", "a", encoding="utf-8") as txt:
        txt.write(message)

    print("\r" + " " * 50 + "\rBackup realizado!\n")

def logInicial():
    with open(fr"{LOG_BACKUP}", "a", encoding="utf-8") as txt:
        txt.write("\n--- Backup em sequência iniciado ---")

def logFinal(): 
    with open(fr"{LOG_BACKUP}", "a", encoding="utf-8") as txt:
        txt.write("\n--- Backup em sequência finalizado ---")