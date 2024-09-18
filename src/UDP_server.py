import socket

# Membuat socket UDP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind ke alamat dan port tertentu
server_socket.bind(('127.0.0.1', 12345))

print("Server UDP siap menerima data...")

while True:
    # Menerima data dari client (sebagai contoh buffer size disini 1024 (dapat disesuaikan))
    data, addr = server_socket.recvfrom(1024)
    print(f"Pesan diterima dari {addr}: {data.decode()}")

    # Kirim balasan ke client
    server_socket.sendto(b"Pesan diterima", addr)
