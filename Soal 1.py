def analisis_rating(reviews):
    # Menentukan rating terendah
    rating_terendah = min(reviews)

    # Menentukan rating tertinggi
    rating_tertinggi = max(reviews)

    # Menghitung rata-rata rating
    rata_rata_rating = sum(reviews) / len(reviews)

    # Mengembalikan hasil dalam bentuk list
    return [rating_terendah, rating_tertinggi, round(rata_rata_rating, 1)]

# Menggunakan loop untuk menginputkan review
jumlah_review = int(input("Masukkan jumlah rating:"))
reviews = []

for i in range(jumlah_review):
    rating = float(input(f"Masukkan rating aplikasi ke-{i + 1}: "))
    reviews.append(rating)

# Memanggil fungsi analisis_rating dengan list reviews
hasil_analisis = analisis_rating(reviews)
print(hasil_analisis)
