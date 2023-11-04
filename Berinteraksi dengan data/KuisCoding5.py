"""
TODO:
Sebuah variabel array diberikan dengan ketentuan berikut.
- Variabel array bernama "var_array" dengan nilai dari 0 hingga 100.
- Hitung nilai rata-rata dari elemen array tersebut.
- Simpan hasil perhitungan dalam variabel bernama "result".

Tips:
- Rumus menghitung rata-rata adalah jumlah seluruh elemen dibagi banyaknya elemen.
- Gunakan percabangan dan perulangan untuk mempermudah, 
  Anda tidak diperbolehkan memberikan nilai secara langsung.
"""
# Jangan ubah kode ini
var_array = [i for i in range(101)]

# TODO: Silakan buat kode Anda di bawah ini.
# Inisialisasi variabel untuk menyimpan jumlah elemen dan jumlah total
jumlah_elemen = 0
jumlah_total = 0

# Loop melalui elemen-elemen dalam array
for elemen in var_array:
    jumlah_total += elemen
    jumlah_elemen += 1

# Hitung rata-rata
if jumlah_elemen > 0:
    result = jumlah_total / jumlah_elemen
else:
    result = 0

# Cetak hasil
print("Rata-rata dari elemen-elemen dalam var_array adalah:", result)
