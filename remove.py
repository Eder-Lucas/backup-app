import shutil
import os
import stat

def apagar(func, caminho, exc_func):
    os.chmod(caminho, stat.S_IWRITE)
    func(caminho)

def remove(origem):
    print("Removendo backup antigo", end="")
    shutil.rmtree(origem, onexc=apagar)