#belajar object dan class

class kocheng: 
    warna = None
    usia = None
    
class icikiwir:
    merk = None
    kecepatan = None

#membuat instance/fariable sebagai "objek nyata"
kocheng1 = kocheng()
kocheng1.warna = "black"
kocheng1.usia = "4 bulan"

kocheng2 = kocheng()
kocheng2.warna = "putih"
kocheng2.usia = "3 bulan"

#print(kocheng1.warna, kocheng1.usia)
#print(kocheng2.warna, kocheng2.usia) 

pembalap_handal = kocheng()
pembalap_handal = icikiwir()
pembalap_handal.warna = "hitam"
pembalap_handal.merk = "honda karbu"
pembalap_handal.kecepatan = "100km"

print (pembalap_handal.warna)