# UDP-Python
UDP(User Datagram Protocol) merupakan protokol komunikasi yang digunakan untuk mentransfer data melalui jaringan komputer tanpa harus adanya koneksi yang terbentuk, dengan kata lain protokol udp ini dapat mengirimkan suatu file tanpa harus adanya koneksi yang terbentuk (tidak ada proses 3-way handshake seperti pada TCP). Jadi bisa dibilang UDP lebih cepat dibanding TCP, namun ini bisa menjadi kelemahan UDP karena dengan tidak ada proses koneksi yang harus terbentuk maka akan ada file yang tidak akan terkirim.

Fitur:

1. Connectionless Protocol:
UDP adalah protokol tanpa koneksi, artinya tidak ada proses pembentukan sesi atau koneksi antara pengirim dan penerima sebelum data dikirimkan. Pengirim dapat langsung mengirim paket data ke penerima.

2. No Error Checking and Recovery:
Tidak seperti TCP, UDP tidak menyediakan mekanisme untuk pemeriksaan kesalahan, pengurutan paket, atau pengiriman ulang data yang hilang. Jika paket hilang selama transmisi, UDP tidak akan meminta pengirim untuk mengirim ulang paket tersebut.

3. Low Overhead:
Karena tidak ada proses pembentukan koneksi, kontrol aliran, atau pengurutan data, UDP memiliki overhead yang sangat rendah. Hal ini membuat UDP sangat cepat dan efisien, cocok untuk aplikasi yang memerlukan kecepatan tinggi seperti streaming video atau game online.

4. Best-Effort Delivery:
UDP menggunakan metode best-effort delivery, artinya data dikirim secepat mungkin tanpa menjamin bahwa paket akan tiba secara utuh atau urut. Hal ini dapat menyebabkan beberapa paket hilang atau tiba dalam urutan yang salah.

5. Suitable for Real-Time Applications:
UDP sering digunakan dalam aplikasi real-time seperti VoIP, video conferencing, dan game online, di mana latensi rendah dan kecepatan transmisi lebih penting daripada keandalan. Karena tidak ada pengiriman ulang atau pemeriksaan kesalahan, data dikirim dengan cepat.

6. Multicasting and Broadcasting:
UDP mendukung pengiriman data ke beberapa penerima sekaligus melalui multicast atau broadcast, yang tidak tersedia di TCP. Ini sangat berguna untuk aplikasi seperti siaran langsung atau streaming media.

7. Lightweight Header:
Header UDP hanya terdiri dari 8 byte, jauh lebih kecil dibandingkan dengan TCP yang memiliki 20 byte. Header UDP berisi informasi dasar seperti port sumber, port tujuan, panjang paket, dan checksum (opsional).

How to run:

# Server
1. Buka aplikasi editor teks, lalu simpan file dengan nama tcp_server.py
2. install library socket jika perlu, namun biasanya pada python 3.x sudah terpasang
3. panggil library socket
4. Buat socket UDP dan bind ke alamat IP dan port tertentu
5. Buat kode untuk menerima pesan dari client dan kirimkan balasan kembali
6. simpan dan jalankan file tcp_server.py

# Client
1. buat file baru tcp_client.py
2. panggil library socket
3. Buat socket UDP client dan hubungkan ke alamat server
4. Buat kode untuk mengirim pesan ke server yang telah di-encode
5. Buat variabel untuk menerima balasan dari server
6. simpan dan jalankan

**Note** : Jika anda membutuhkan bantuan kode anda bisa melihat file kode yang tersedia pada repository ini, jika terdapat kekeliruan mohon meninggalkan komentar

**Requirements Python 3.x**




