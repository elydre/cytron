print('''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
██
--|~|--|~|--|~|--|~|--|~|--|~|--

        GPL-3.0 Licence

--|~|--|~|--|~|--|~|--|~|--|~|--
''')

import os
import sys

from urllib.request import urlopen
from urllib.error import HTTPError

# chemin de l'installation

versions = urlopen("https://raw.githubusercontent.com/pf4-DEV/cytron/main/version/index.txt").read().decode('utf-8').split('\n')

while True:
    v = input(f"\nchoisissez une version\n[{versions[-1]}]: ")
    if v == "": v = versions[-1]
    if v in versions: break
    else: print(f"ERREUR: version inconnue ({', '.join(versions)})")

while True:
    mode = input("\nchoisissez un mode d'installation programme/module\n[module]: ")
    if mode == "": mode = "module"
    if mode.lower()[0] == "p":
        mode = "programme"
        break
    elif mode.lower()[0] == "m":
        mode = "module"
        break
    else: print("ERREUR: mode inconnu (programme, module)")

PATH = f"{os.path.dirname(sys.executable)}\Lib\site-packages" if mode == "module" else os.getcwd()
PATH = PATH.replace("\\", "/")

while True:
    perm = input(f"\nacceptez-vous d'installer cytron {v} dans {PATH} en tant que {mode}?\n[o]: ")
    if perm.lower() in ["o", "oui", "yes", "oe", "oep", "y", ""]: break
    elif perm.lower() in ["n", "non", "no", "nop", "clc"]:
        print("abandon")
        sys.exit()
    else: print("ERREUR: o/n")

def mkdir(path):
    try:
        os.mkdir(path)
        print(f"creation de '{path}' avec succes")
    except FileExistsError:
        print(f"le dossier '{path}' existe deja")

def wget(chem, url):
    try:
        open(chem, 'wb').write(urlopen(url).read())
        print(f"telechargement de '{chem}' avec succes")
    except HTTPError:
        print(f"erreur de telechargement de '{chem}'")

print()

if mode == "programme":
    wget(f"{PATH}/cytron.py", f"https://raw.githubusercontent.com/pf4-DEV/cytron/main/version/v{v}.py")

elif mode == "module":
    mkdir(f"{PATH}/cytron")
    wget(f"{PATH}/cytron/__init__.py", f"https://raw.githubusercontent.com/pf4-DEV/cytron/main/version/v{v}.py")

else:
    print("ERREUR: wtf")

print(f"\nmerci d'avoir installer cytron {v}, pour plus d'informations: https://github.com/pf4-DEV/cytron")