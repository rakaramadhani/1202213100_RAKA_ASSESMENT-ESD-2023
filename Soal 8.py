class Produk:
    def __init__(self, nama, kategori, harga):
        self.nama = nama
        self.kategori = kategori
        self.harga = harga

class Pelanggan:
    def __init__(self, nama, minat):
        self.nama = nama
        self.minat = minat

def rekomendasi_produk(pelanggan, daftar_produk):
    produk_rekomendasi = []
    for produk in daftar_produk:
        if produk.kategori in pelanggan.minat:
            produk_rekomendasi.append(produk.nama)
    return produk_rekomendasi

produk_list = [
    Produk("TV", "elektronik", 1000),
    Produk("headphone", "elektronik", 200),
    Produk("baju", "fashion", 50),
    Produk("gitar", "musik", 300),
    Produk("sepatu", "olahraga", 80),
    Produk("kamera", "elektronik", 600)
]

pelanggan_list = [
    Pelanggan("Rina", ["elektronik", "musik", "fashion", "olahraga"]),
    Pelanggan("Budi", ["musik", "olahraga", "elektronik"])
]

for pelanggan in pelanggan_list:
    print(f"Rekomendasi produk untuk {pelanggan.nama}: {rekomendasi_produk(pelanggan, produk_list)}")