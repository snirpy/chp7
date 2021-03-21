def saisir():
    n = ""
    while n =="":
        n = input("Saisir la valeur de n:")
        try:
            n = int(n)
        except:
            print("Vous n'avez pas saisi une valeur numérique!")
            n=""
        else:
            if n < 0:
                print("Vous avez saisi une valeur négative")
                n =""
    return n

nb = saisir()

def multiplication():
    for i in range(11):
        print(f"{nb} x {i} = {nb*i}")
    
multiplication()