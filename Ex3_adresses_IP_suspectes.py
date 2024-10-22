blacklist = ['192.168.1.5', '10.0.0.7', '172.16.0.10']
ips_connected = ['192.168.1.1', '192.168.1.5', '192.168.1.10', '10.0.0.7']

# 1. Détection des IP suspectes
malicious_ips = [ip for ip in ips_connected if ip in blacklist]

## ou bien
#malicious_ips = []
#for ip in ips_connected:
#    if ip in blacklist:
#        malicious_ips.append(ip)

print("IP suspectes détectées :")
for ip in malicious_ips:
    print(ip)

if malicious_ips:
    print("\nAction suggérée : Bloquer ces IPs.")
else:
    print("\nAucune IP suspecte détectée.")
