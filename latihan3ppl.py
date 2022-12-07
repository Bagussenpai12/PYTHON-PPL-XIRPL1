# membuat variabel atau boc bernama buah

buah = [
    "apel", "durian", "kiwi", "alpukat", "mangga"
]

sayur = [
    "pokcoy", "sledri", "kangkung", "bayem", "asem"
]



# cara menambah nilai di dalam list
#buah.append("anggur merah")

#cara menghapus yang ada di dalam buah
#buah.remove("kiwi")

#cara memotong nilai yang ada di dalam box buah
#print (buah[0:4])

# tampilkan data yang ada di variabel buah
#print(buah)

# tampilka data berurutan dari awal hingga akhir
#for grobak in buah:
#    print(grobak)

#print (buah[0], buah[2])

#operasi aritmatika tipe data list
dagang_hari_ini = buah + sayur
print (dagang_hari_ini)

for grobak in dagang_hari_ini:
    print (grobak)
    
    
kasir = input("mau tambah buah apalagi :")
buah.append(kasir)
print(buah)