
urutan_kedatangan = ['Ningguang', 'Hutao', 'Xiao', 'Childe']

kebiasaan = {
    'Ningguang': 'Memeriksa kue',
    'Hutao': 'Langsung memberikan kado',
    'Xiao': 'Memotret apa pun yang dilihat pertama kali',
    'Childe': 'Membawa air mineral dan meletakkannya di meja'
}

kue_utuh = True

pencuri_kue = None

for tamu in urutan_kedatangan:
    if kue_utuh:
        if kebiasaan[tamu] != 'Memeriksa kue':
            pencuri_kue = tamu
            break
    else:
        if kebiasaan[tamu] == 'Memeriksa kue':
            pencuri_kue = tamu
            break

if pencuri_kue:
    print(f"Misteri terpecahkan! {pencuri_kue} adalah yang paling mungkin mengambil kue.")
else:
    print("Semua tamu tampaknya bersikap adil terhadap kue.")
