# Sekuensial
print('ibu berkata , "Pergi Ke Toko"')
print('Budi Menjawab , "Baik, apa yg harus saya lakukan di toko?"')
print('ibu menjawab , " Belikan satu botol susu , dan jika ada telur beli 6"')
print('Budi berangkat ketoko')
print('Dan mulai berbelanja')

# Percabangan
jumlah_botol_susu = 128
jumlah_telur = 42325242
print(f"Jumlah botol susu {jumlah_botol_susu}btl")

if jumlah_botol_susu > 0:
    print("Budi mengcek harga nya dan uang nya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 6 botol susu")

else:
    print("Tidak jadi beli botol susu")


print("Budi pulang jalan kerumah")
print("Budi pulang kerumah menyerahkan belanja nya kepada ibu")
