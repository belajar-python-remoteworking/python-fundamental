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
