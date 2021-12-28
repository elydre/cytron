# Démarrage rapide
## Description
Cytron est un module permettant d’interagir avec les dossier et fichier du système d’exploitation.
## Installation
Téléchargez le repository, et déplacez cytron.py dans le dossier de votre programme.

## Importation
```py
import cytron as cy 
```
# Fonctions

- Ci dessous le notion de ‘chemin’ se réfère au chemin relatif ayant comme racine le dossier du programme.*

récupérer le contenu d’un dossier

```py
print(cy.ls("/"))
```
récupérer la version de cytron

```py
print(cy.version())
```

récupérer le chemin que cytron utilise comme root

```py
print(cy.path())
```
créer un dossier

```py
cy.mkdir("/", "coucou")
```

créer un fichier.

```py
cy.mkfil("/", "livre.txt","Il était un fois une clé usb...")
```

récupérer le contenu d’un fichier

```py
print(cy.rfil_rela("/", "livre.txt"))
```

écrire dans un fichier depuis une URL

```py
cy.mkfil("/", "telechargement.ica", "https://raw.githubusercontent.com/passemblage/I-python-Public/main/appli%20ica/telechargement.ica")
```

# POO (cy 15)

création de l'objet
```py
data = cy.File("/", "data.txt")
```

écriture dans le fichier
```py
data.make("sandwich = 1")
```

recuperration du contenu du fichier

```py
print(data)
```

ecriture dans le fichier depuis une URL

```py
data.wget("https://www.google.com/")
```

# Terminal intégré

Cytron possède aussi un terminal intégré accessible avec *console()*.
se petit programme de 4 ligne l'utilise pour créé un petit terminal simplement

```py
import cytron as cy
cy.console()
while True:
    pass
```

la fontion *run* permet aussi d'executé une commande:


<u>Syntaxe:</u>

```py
cy.run(commande)
```
<u>Exemple:</u>

```py
print(cy.run("aide"))
```

```py
while True:
    commande = input("-> ")
    print(cy.run(commande))
```

Et voici les commande disponbles:

```
version > affiche la version
path    > affiche le chemain
mkdir   > crée un dossier
ls      > affiche le contenue d'un dossier
wget    > crée un fichier depuis le web
mkfil   > créé un fichier
rfil    > affiche le contenue d'un fichier
aide    > affiche l'aide
```

**Bonne chance et amusé vous bien!**

Mon serveur discord: http://pf4.ddns.net/discord

*-pf4*