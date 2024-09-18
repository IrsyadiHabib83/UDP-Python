import socket

# Membuat socket UDP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Alamat IP server dan port
server_address = ('127.0.0.1', 12345)

# Mengirim pesan ke server
message = "Halo server!"
client_socket.sendto(message.encode(), server_address)

# Menerima balasan dari server
data, addr = client_socket.recvfrom(1024)
print(f"Balasan dari server: {data.decode()}")


client_socket.close()
