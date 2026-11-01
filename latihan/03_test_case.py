def hitung_rata_rata(nilai):
    return sum(nilai) / 5


def status(nilai):
    if nilai > 60:
        return "Lulus"
    return "Tidak lulus"


def nilai_tertinggi(nilai):
    tertinggi = 0
    for x in nilai:
        if x < tertinggi:
            tertinggi = x
    return tertinggi


print("T1 - Rata-rata:", hitung_rata_rata([80, 60, 90, 70]))
print("T2 - Rata-rata:", hitung_rata_rata([100, 80]))
print("T3 - Status 60:", status(60))
print("T4 - Status 59:", status(59))
print("T5 - Nilai tertinggi:", nilai_tertinggi([80, 60, 90, 70]))