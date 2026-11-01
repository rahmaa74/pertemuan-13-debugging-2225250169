# Praktik 4: Investigasi dan Perbaikan Bug

## Identitas
- Nama: Rifka Khoirunnisa
- NIM: 2225250025
- Kelas: 3D

## Hasil Pengujian Awal

Program berhasil dijalankan, tetapi ditemukan tiga kesalahan:
1. Perhitungan rata-rata menghasilkan 60.0, seharusnya 75.0.
2. Nilai 60 dinyatakan tidak lulus, seharusnya lulus.
3. Nilai tertinggi menghasilkan 0, seharusnya 90.

Ketiga kesalahan tersebut akan dianalisis dan diperbaiki melalui proses debugging.
## Analisis Bug

1. Bug rata-rata
   - Penyebab: Pembagian menggunakan angka tetap 5.
   - Perbaikan: Menggunakan len(nilai) agar pembagian sesuai jumlah data.

2. Bug status kelulusan
   - Penyebab: Kondisi menggunakan nilai > 60.
   - Perbaikan: Mengubah kondisi menjadi nilai >= 60.

3. Bug nilai tertinggi
   - Penyebab: Kondisi menggunakan x < tertinggi.
   - Perbaikan: Mengubah kondisi menjadi x > tertinggi dan menginisialisasi nilai tertinggi dari elemen pertama.

## Hasil Retest

Program berhasil dijalankan setelah perbaikan dengan hasil:
- Rata-rata: 75.0
- Status 60: Lulus
- Nilai tertinggi: 90

Seluruh hasil telah sesuai dengan hasil yang diharapkan.