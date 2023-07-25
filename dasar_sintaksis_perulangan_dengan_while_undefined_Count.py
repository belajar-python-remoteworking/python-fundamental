"""
program pengulangan dengan while
"""
jumlah_buku=10
total_jumlah_baca = 0
print('Ibu Berkata : "Baca Semua Bukumu"')

jumlah_buku_yg_sudah_dibaca_dan_dipahami = 0
print(f"jumlah buku yg sudah dibaca dan dipahami{jumlah_buku_yg_sudah_dibaca_dan_dipahami}")

while total_jumlah_baca < jumlah_buku *2:
    total_jumlah_baca = total_jumlah_baca + 1
    if jumlah_buku_yg_sudah_dibaca_dan_dipahami == 9:
        print(f"Buku ke {jumlah_buku_yg_sudah_dibaca_dan_dipahami+1} belum paham")
    else:
        jumlah_buku_yg_sudah_dibaca_dan_dipahami = jumlah_buku_yg_sudah_dibaca_dan_dipahami + 1
        print(f"Buku ke{jumlah_buku_yg_sudah_dibaca_dan_dipahami} sudah dibaca dan dipahami")

print(f"jumlah buku yg sudah dibaca dan dipahami {jumlah_buku_yg_sudah_dibaca_dan_dipahami}")
if jumlah_buku_yg_sudah_dibaca_dan_dipahami == jumlah_buku:
    print("Semua jumlah buku sudah di baca dan di pahami")
else:
    print(f'"Tidak Semua Buku bisa dipahami , Saya Hanya bisa memahamai {jumlah_buku_yg_sudah_dibaca_dan_dipahami} buku"')


