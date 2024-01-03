def dekripsi_chat(encrypted_chat):
    hasil_dekripsi = ""
    for karakter in encrypted_chat:
        if karakter.isalpha():
            # Mendekripsi huruf-huruf
            if karakter.islower():
                hasil_dekripsi += chr((ord(karakter) - 97 - 5) % 26 + 97)
            else:
                hasil_dekripsi += chr((ord(karakter) - 65 - 5) % 26 + 65)
        else:
            # Menambahkan karakter selain huruf tanpa perubahan
            hasil_dekripsi += karakter
    return hasil_dekripsi

# Isi Chat Terenkripsi
isi_encrypted_chat = "xfqfr bfmdz\ngjxtp lzj rfz ifkyfw jxi snm\ngwt, gjxtp qz rfz rfpfs in bfwlty lfp?\nfpz xfdfsl pfrz, rfz lfp ofin ufhfwpz\ndfsl pnwnr xynhpjw otrtp pz pnhp ifwn lwzu"

# Mendekripsi isi chat
isi_chat_didekripsi = dekripsi_chat(isi_encrypted_chat)

# Menampilkan hasil dekripsi
print(isi_chat_didekripsi)