import os, sys

cy_path = os.path.dirname(sys.argv[0])

def cy_mkdire(chem, nom):
    cy_temp = cy_path + chem + "/" + nom
    try:
        os.makedirs(cy_temp)
        print("done")
    except:
        pass

def cy_mkfil(chem, nom, text):
    cy_temp = cy_path + chem + "/" + nom
    fil = open(cy_temp, "w")
    fil.write(text)
    fil.close()

def cy_rfil(chem, nom):
    cy_temp = cy_path + chem + "/" + nom
    fil = open(cy_temp, "r")
    return(fil.read())