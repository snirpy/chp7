def saisir_poids():
    poids = ""
    while poids == "":
        poids = input("Entrez votre poids en kg: ")
        try:
            poids = int(poids)
        except:
            print("Vous n'avez pas saisi une valeur numérique ")
            poids = ""
        else:
            if poids == 0:
                print("Vous avez saisi zéro")
                poids = ""
            elif poids < 0:
                print("Vous avez saisi une valeur négative")
                poids = ""
            elif poids > 300 or poids < 30:
                print("Valeur hors limite")
                poids = ""
    return poids

def saisir_taille():
    taille = ""
    while taille == "":
        taille = input("Entrez votre taille en cm: ")
        try:
            taille = float(taille)
        except:
            print("Vous n'avez pas saisi une valeur numérique ")
            taille = ""
        else:
            if taille == 0:
                print("Vous avez saisi zéro")
                taille = ""
            elif taille < 0:
                print("Vous avez saisi une valeur négative")
                taille = ""
            elif taille > 2.6 or taille < 0.4:
                print("Valeur hors limite")
                taille = ""
    
    return taille

def calculer_IMC():
    poids = saisir_poids()
    taille = saisir_taille()
    imc = poids/(taille**2)
    return imc

def afficher():
    imc = calculer_IMC()
    if imc<18:
        print("Vous êtes trop maigre! Votre IMC = ",imc)
    elif imc>=18 and imc < 25:
        print("Vous êtes Normal.Votre IMC = ",imc)
    elif imc>=25 and imc < 30:
        print("Vous êtes en surpoids.Votre IMC = ",imc)
    elif imc>=30 and imc < 35:
        print("Vous êtes obèse.Votre IMC = ",imc)
    elif imc>=35 :
        print("Vous êtes très obèse.Votre IMC = ",imc)

    
afficher()


