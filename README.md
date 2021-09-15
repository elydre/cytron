# <b>CYTRON</b>
## <b> Démarrage rapide </b>
### <b> Description </b>
Cytron est un module permettant d’interagir avec les dossier et fichier du système d’exploitation.
### <b> Installation </b>
Téléchargez le repository, et déplacez cytron.py dans le dossier de votre programme.

### <b> Importation </b>
```py
import cytron as cy 
```
## <b> Interaction </b>

<i> Ci dessous le notion de ‘chemin’ se réfère au chemin relatif ayant comme racine le dossier du programme. </i>

### <b>ls:</b>

<i>cy_ls()</i> liste le contenu d'un dossier

<u>Syntaxe:</u>

```py
cy_ls(chemin)
```
<u>Exemple:</u>

```py
print(cy.cy_ls("/"))
```

### <b>version</b>

<i>cy_version()</i> retourne la version de cytron.

<u>Syntaxe:</u>

```py
cy_version()
```
<u>Exemple:</u>

```py
print(cy.cy_version())
```

### <b>path</b>

<i>cy_path</i> retourne le chemin que cytron utilise comme root.

<u>Syntaxe:</u>

```py
cy_path()
```
<u>Exemple:</u>

```py
print(cy.cy_path())
```

### <b>mkdir</b>

<i>cy_mkdir</i> crée des dossiers.

<u>Syntaxe:</u>

```py
cy_mkdir(chemin, nom)
```
<u>Exemple:</u>

```py
cy.cy_mkdir("/", "coucou")
```

### <b>mkfil</b>

<i>cy_mkfil</i> crée des fichiers.

<u>Syntaxe:</u>

```py
cy_mkfil(chemin, nom, ContenuDuFichier)
```
<u>Exemple:</u>

```py
cy.cy_mkfil("/", "livre.txt","Il était un fois une clé usb...")
```

### <b>rfil</b>

<i>cy_rfil_rela</i> retourne le contenu de fichiers.

<u>Syntaxe:</u>

```py
cy_rfil_rela(chemin, nom):
```
<u>Exemple:</u>

```py
print(cy.cy_rfil_rela("/", "livre.txt"))
```

### <b>cy_wget</b>

<i>cy_wget</i> va comme <i>cy_mkfil</i> crée des fichier mais cette fois avec du contenu recupéré de page web.

<u>Syntaxe:</u>

```py
cy_wget(chemin, nom, url):
```
<u>Exemple:</u>

```py
cy.cy_mkfil("/", "telechargement.ica", "https://raw.githubusercontent.com/passemblage/I-python-Public/main/appli%20ica/telechargement.ica")
```

## <b> Terminal intégré </b>

Cytron possède aussi un terminal intégré accessible avec <i>cy_console_print()</i>.
se petit programme de 4 ligne l'utilise pour créé un petit terminal simplement

```py
import cytron as cy
cy.cy_console_print()
while True:
    pass
```

la fontion <i>cy_run</i> permet aussi d'executé une commande:


<u>Syntaxe:</u>

```py
cy.cy_run(commande)
```
<u>Exemple:</u>

```py
print(cy.cy_run("aide"))
```

```py
while True:
    commande = input("-> ")
    print(cy.cy_run(commande))
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

## <b> Programme utilisant cytron </b>

Quelque programme déjà utilise cytron comme I-python

<img src="doc/ip.png">

ou terminal tools

<img src="doc/tt.png">

<b>Bonne chance et amusé vous bien!</b>

Mon serveur discord: https://discord.gg/PFbymQ3d97

<i>-pf4 </i>