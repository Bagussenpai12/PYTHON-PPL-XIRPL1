#PRAKTEK ENKAPSULASI
#Buatlah masing masing parameter:
# Siswa - Public
# Guru - Protected
# Kepsek - Private 

#Tampilkan
# 1. Siswa Kami Bernama Euroski Ganteng
# 2. Guru Kami Bernama BU Anita Yang Cantik
# 3. Kepsek Kami Bernama Pak Lilik

class  siswa:
    def __init__(self, nama):
        self.nama = nama

perkenalan = siswa('Euroski')

print(f'siswa Kami Bernama {perkenalan.nama} Ganteng')

class guru:
    def __init__(self, nama):
        self.nama = nama

class guruotkp:
    def __ini__(self, nama, cantik):
        super().__init__()
        self._cantik = cantik

    def perkenalan(self):
        print(f'Guru Kami Bernama {self._nama} yang {self._cantik}')

BuAnita = guruotkp('Bu Anita','Cantik')
BuAnita.pamer()

class kepsek:
    def __init__(self, nama):
        self._nama = nama

    def lilik(self):
         print(f'kepsek kami bernama {self._nama}')

l = kepsek('lilik')
l.lilk()