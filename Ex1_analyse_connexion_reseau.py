packets = [ (500, 'TCP'),
(1000, 'UDP'), 
(2000, 'TCP'), 
(50, 'ICMP'), 
(1600, 'TCP'), 
(800, 'UDP')
]
compteur = 0
udp =0
tcp = 0
print()
print("-"*32)
print("|\ttaille  |  protocole    |")
print("-"*32)

for paquet in packets:
    print(f"|\t{paquet[0]}: \t|\t{paquet[1]}\t|")
    print("-"*32)

print("\nPaquets qui dépassent 1500 ocets:")
for paquet in packets:
    if paquet[0]>1500:
        print(paquet)

for paquet in packets:
    if paquet[1]=="TCP":
        udp += 1
    if paquet[1]=="UDP":
        tcp += 1


pourcentageUDP = (udp / len(packets))*100
pourcentageTCP = (tcp / len(packets))*100

print(f"\nPourcentage paquet UDP: {pourcentageUDP:.2f}%")
print(f"Pourcentag epaquet TCP: {pourcentageTCP:.2f}%")
        
print()
