def palindrom(kata):
    kata = kata.replace(" ", "").lower()

    if kata == kata[::-1]:
        return "Eureeka!"
    else:
        return "Suka blyat"
input_kata = input("Masukkan kata atau kalimat: ")
hasil_cekJikaPalindrom = palindrom(input_kata)
print(hasil_cekJikaPalindrom)
