def cek_duplikat(data):
    angka_terlihat = set()

    for angka in data:
        if angka in angka_terlihat:
            return True
        else:
            angka_terlihat.add(angka)
    return False

#testcase
data_input = [20, 1, 3, 2, 4, 6, 8, 5, 7, 9, 11, 13, 15, 10, 12, 14, 16, 18, 20, 17, 19]
hasil_cek_duplikat = cek_duplikat(data_input)

print(hasil_cek_duplikat)
