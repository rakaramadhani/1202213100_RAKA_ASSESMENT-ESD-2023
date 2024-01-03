def harga_total(item, harga):
    total = 0
    if item in ['ayam_bakar', 'ayam_puk_puk']:
        total = harga * (1 + 0.05) * (1 + 0.15)
    elif item in ['es_teh', 'es_jeruk']:
        total = harga * (1 + 0.03) * (1 + 0.15)
    return total

menu = {
    'ayam_goreng_krispi': 15000,
    'ayam_puk_puk': 13000,
    'ayam_bakar': 20000,
    'es_teh': 5000,
    'es_jeruk': 7000
}

pesanan = {
    'rehan_whangsap': ['ayam_bakar', 'ayam_bakar', 'es_teh'],
    'amba_roni': ['ayam_puk_puk', 'es_teh', 'es_teh', 'es_teh'],
    'faiz_ngawi': ['ayam_goreng_krispi', 'ayam_puk_puk', 'ayam_bakar', 'es_teh', 'es_jeruk']
}

biaya = {}
for sahabat, items in pesanan.items():
    total = 0
    for item in items:
        total += harga_total(item, menu[item])
    biaya[sahabat] = total

for sahabat, total in biaya.items():
    print(f"Biaya {sahabat} adalah Rp {total:.0f}")