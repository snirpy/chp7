logs = [('192.168.1.50', '2024-09-12 12:15:10'), 
        ('192.168.1.10', '2024-09-12 13:15:10'), 
        ('192.168.1.20', '2024-09-12 14:16:15'), 
        ('192.168.1.30', '2024-09-12 15:20:20'), 
        ('192.168.1.10', '2024-09-12 16:20:20'),
        ('192.168.1.30', '2024-09-12 17:20:20'),  
        ('192.168.1.40', '2024-09-12 18:00:25'), 
        ('192.168.1.20', '2024-09-12 18:16:15'), 
        ('192.168.1.10', '2024-09-12 19:20:20'),
        ('192.168.1.100', '2024-09-12 20:35:30') 
        ] 
ips= []
horaires= []
# print(len(logs))
for ip, horaire in logs:
    ips.append(ip)
    horaires.append(horaire)

# print(ips)
# print(horaires)


ip_unique_liste = []
ip_suspect_liste = []
ip_suspect_unique_liste = []
occurence=[]

for log in logs:
    if  log[0] not in ip_unique_liste:
        ip_unique_liste.append(log[0])

    else:
        ip_suspect_liste.append(log[0])

for ip in ip_suspect_liste:
    if ip not in ip_suspect_unique_liste:
        ip_suspect_unique_liste.append(ip)

for ip in ip_unique_liste:
    occurence.append(ip_suspect_liste.count(ip)+1)

# print(f"Les suspectes: {ip_suspect_unique_liste}")
# print(f"Les bonnes: {ip_unique_liste}")
# print(f"Les occurences: {occurence}")
print("IP connectée 3 fois ou plus:\n")
for ip in ip_suspect_unique_liste:
    # print("index:",index)
    # print("ip:",ip)
    # if ip in ip_suspect_unique_liste:
    indices_de_ip = [i for i, x in enumerate(ips) if x == ip]
    # print(indices_de_ip)
    # print(f"{ip} : occurence : {ips.count(ip)} {horaires[ips.index(ip)]}")
    # print(f"{ip} : occurence : {ips.count(ip)} {horaires[indices_de_ip[-1]]}")
    print(f"{ip} : première connexion {horaires[ips.index(ip)]}")
    print(f"{ip} : dernière connexion {horaires[indices_de_ip[-1]]}")
    print()
print("Nombre total de connexion unique: ",len(ip_unique_liste))
