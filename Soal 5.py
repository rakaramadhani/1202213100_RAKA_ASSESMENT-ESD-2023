from math import factorial

def hitung_kombinasi(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))

def hitung_kombinasi_username(nama_lengkap):
    # Menggabungkan nama dan mengonversi menjadi huruf kecil
    nama_lengkap = nama_lengkap.lower()

    # Menghitung panjang nama
    panjang_nama = len(nama_lengkap)

    # Menghitung jumlah kombinasi untuk panjang username 1 hingga 6
    total_kombinasi = 0
    for panjang_username in range(1, min(panjang_nama, 6) + 1):
        total_kombinasi += hitung_kombinasi(panjang_nama, panjang_username)

    return total_kombinasi

# Nama lengkap Naip Lovyu
nama_lengkap = input("Masukkan nama lengkap :")

# Hitung jumlah kombinasi username
jumlah_kombinasi = hitung_kombinasi_username(nama_lengkap)

print(f"Jumlah kombinasi username yang mungkin: {jumlah_kombinasi}")
