import shutil

def copia(data, origem, destino, arquivo):
    print("\r" + " " * 40 + "\rCopiando...", end="", flush=True)

    shutil.copytree(
        origem,
        destino,
        ignore=shutil.ignore_patterns('.git')
    )

    return f"\n{data}: {arquivo} salva no backup"
