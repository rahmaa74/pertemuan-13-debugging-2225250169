def hitung_diskon(harga, persen):
    diskon = harga * persen / 100
    total_bayar = harga - diskon
    return total_bayar


harga = 200000
persen = 10

hasil = hitung_diskon(harga, persen)

print("Harga awal:", harga)
print("Persentase diskon:", persen, "%")
print("Total bayar:", hasil)