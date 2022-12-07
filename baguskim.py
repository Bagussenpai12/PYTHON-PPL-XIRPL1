class Agama:
    def __init__(self, nama, agama):
        self.nama = nama
        self.agama = agama
    
    def perkenalan(self):
        print(self.nama, "Beragama", self.agama )

class Islam(Agama):
    def __init__(self, nama, agama, sholat):
        Agama.__init__(self, nama, agama)
        self.sholat = sholat

class kristen(Agama):
    def __init__(self, nama, agama, berdoa):
        Agama.__init__(self, nama, agama)
        self.berdoa = berdoa

hisyam = Islam('Hisyam', 'Islam', 'Sholat')
hisyam.perkenalan()
print(f'{hisyam.nama} beribadah dengan melakukan {hisyam.sholat}')

abraham = kristen('Abraham', 'Kristen', 'Berdoa')
abraham.perkenalan()
print(f'{abraham.nama} beribadah dengan melakukan {abraham.berdoa}')