
def saisir() :  
    nb = ""
    while nb == "":
        nb_str = input("Saisir votre moyenne: ")
        try:
            nb = float(nb_str)
        except:
            print("Vous n'avez pas saisi une valeur numérique!")
            nb = ""
        else:   
            if nb > 20:
                print("Vous ne pouvez pas avoir plus que 20")
                nb = ""

            elif nb < 0:
                print("Vous avez saisi une valeur négative!")
                nb = ""
    return nb

def apprecier(moyenne):
    if 14< moyenne <= 20:
        print("Très bien")
    elif  10<= moyenne <= 14:
        print("Assez bien")
    elif 5 <= moyenne < 10:
        print("Insuffisant")
    elif moyenne < 5:
        print("Catastrophique")


moyenne = saisir()
print(f"Votre moyenne est {moyenne}")
apprecier(moyenne)