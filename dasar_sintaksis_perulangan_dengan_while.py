"""
program pengulangan dengan while
"""
jumlah_buku=10
print('Ibu Berkata : "Baca Semua Bukumu"')

jumlah_buku_yg_sudah_dibaca = 0
print(f"jumlah buku yg sudah dibacaP{jumlah_buku_yg_sudah_dibaca}")

while jumlah_buku_yg_sudah_dibaca < jumlah_buku:
    jumlah_buku_yg_sudah_dibaca = jumlah_buku_yg_sudah_dibaca + 1
    print(f"Buku ke {jumlah_buku_yg_sudah_dibaca} sudah dibaca")


print(f"jumlah buku yg sudah dibaca {jumlah_buku_yg_sudah_dibaca}")