daftar_buku = ['40 Lawyers','99 Orang Berpengaruh Di dunia', 'How To Basic ']
print('/ntampilkan variable daftar buku')
print(daftar_buku)

print('\ntampilkan semua daftar buku dengan for')
for buku in daftar_buku:
    print(buku)


print('\ntampilkan isi daftar buku indeks tertentu')
print(daftar_buku[0])
print(daftar_buku[1])

print('\npanjang daftar buku dengan in range')
for i in range(0 , len(daftar_buku)):
    print(daftar_buku[i])

print('/ncara menambahkna buku dengan append')
daftar_buku = ['40 Lawyers','99 Orang Berpengaruh Di dunia', 'How To Basic ']
print('\ntambahkan 1 buku baru')
daftar_buku.append('25 Kisah Nabi')
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nClear List')
daftar_buku.clear()
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nganti elemen pertama')
daftar_buku = ['40 Lawyers','99 Orang Berpengaruh Di dunia', 'How To Basic ']
daftar_buku [0] = '40 Law Of Lawyers'
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nfungsi pop , mengambil elemen ke 2 dari daftar buku')
buku = daftar_buku.pop(1)
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nmenampilkan data yg sudah di pop')
print(buku)

print('\nPerintah Del')
daftar_buku = ['40 Lawyers','99 Orang Berpengaruh Di dunia', 'How To Basic ']
del daftar_buku[:]
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del Start')
daftar_buku = ['40 Lawyers','99 Orang Berpengaruh Di dunia', 'How To Basic ']
del daftar_buku[0:2]
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah Del Step')
daftar_buku = ['40 Lawyers','99 Orang Berpengaruh Di dunia', 'How To Basic ']
del daftar_buku[0::2] #Step Aatau Langkau
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])
