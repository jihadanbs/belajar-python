# Membuat Keputusan (Kondisi if, elif, else)

# if: Untuk memeriksa kondisi pertama.
# elif: (singkatan dari else if) Untuk memeriksa kondisi lain jika if sebelumnya salah.
# else: Jika semua kondisi di atas salah, maka ini yang akan dijalankan.
jumlah_percobaan_login = 6

if jumlah_percobaan_login > 5:
    print("Terlalu banyak percobaan. Akun diblokir!")
elif jumlah_percobaan_login > 3:
    print("Peringatan: Percobaan login hampir habis.")
else:
    print("Percobaan login berhasil.")

print("------------------------------")

jumlah_percobaan_login = 3
is_login = True

if jumlah_percobaan_login == 3 and is_login == True:
    print("Login berhasil!")
elif jumlah_percobaan_login >= 3 or jumlah_percobaan_login <= 5:
    print("Peringatan: Percobaan login hampir habis, silahkan coba lagi!")
else:
    print("Terlalu banyak percobaan. Akun diblokir!")
