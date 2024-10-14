logs = [
    ('192.168.1.2', '2024-09-12 12:00:10'),
    ('192.168.1.2', '2024-09-12 12:00:10'),
    ('192.168.1.12', '2024-09-12 12:35:30'),
    ('192.168.1.1', '2024-09-12 13:00:15'),
    ('192.168.1.1', '2024-09-12 13:16:15'),
    ('192.168.1.12', '2024-09-12 13:35:30'),
    ('192.168.1.12', '2024-09-12 14:00:30'),
    ('192.168.1.1', '2024-09-12 15:16:15'),
    ('192.168.1.3', '2024-09-12 16:16:15'),
    ('192.168.1.112', '2024-09-12 17:35:30'),
    ('192.168.1.120', '2024-09-12 17:35:30'),
    ('192.168.1.192', '2024-09-12 17:35:30'),
    ('192.168.1.222', '2024-09-12 17:35:30')
]

liste_ip_unique =[]
liste_ip_suspecte =[]
occurence = []
compteur_ip= 0

for element in logs:
    if element[0] not in liste_ip_unique:
        liste_ip_unique.append(element[0])
    else:
        compteur_ip += 1
        liste_ip_suspecte.append(element[0])
        
for element in liste_ip_unique:
    occurence.append(liste_ip_suspecte.count(element)+1) 

print(f"Le nombre d'adresses ip uniques est : {len(liste_ip_unique)}")
print("Adresse suspecte: ")
print(list(set(liste_ip_suspecte)))
# print(compteur_ip)
# print(occurence)
print("Affichage:")
for index, element in enumerate(liste_ip_unique):
    # print(index)
    if occurence[index]>=3:
        print(f"{element} s'est connecté {occurence[index]} fois la première à {[c[1] for c in logs if c[0] == element][0]} ")
        print(f"{element} s'est connecté {occurence[index]} fois la dernière à {[c[1] for c in logs if c[0] == element][-1]} ")
    else:
        print(f"{element} s'est connecté {occurence[index]} fois")
