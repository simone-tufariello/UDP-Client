import socket

target_host = "www.google.com"
target_port = 9997

# creiamo un oggetto socket
# AF_INET = usiamo indirizzo IPv4
# SOCK_DGRAM = creiamo una socket UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# inviamo dei dati
# invio i dati e specifico il server a cui inviarli
client.sentto(b"INVIO DATI", (target_host, target_port))

# riceviamo risposta (sia i dati che le info relative al server)
data, addr = client.recvfrom(4096)
print(data.decode())
client.close()