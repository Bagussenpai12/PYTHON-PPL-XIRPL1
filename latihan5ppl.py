#Buat 3 Objek Orang, Pelajar, Pekerja
#orang = kelas induk
#pelajar, pekerja = kelas turunan

class orang:
    def __init__(self, nama, asal):
        self.nama = nama
        self.asal = asal

    def perkenalan(self):
        print("Hallo nama saya",self.nama,"dari",self.asal)

class pelajar(orang):
    def __init__(self,nama,asal,sekolah):
        orang.__init__(self,nama,asal)
        self.sekolah = sekolah
     

class pekerja(orang):
    def __init__(self,nama,asal,kantor):
        super().__init__(nama,asal)
        self.kantor = kantor

andi = orang('andi','jakarta\n')
andi.perkenalan()

tito = pelajar('tito','subang','smkjp1')
tito.perkenalan()
print(f'saya sekolah di {tito.sekolah}\n')

cahyo = pekerja('cahyo','bandung','smkjp1')
cahyo.perkenalan()
print(f'saya kerja di {cahyo.kantor}\n')
