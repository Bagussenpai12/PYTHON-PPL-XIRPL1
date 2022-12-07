#jenis enkapsulasi : public, protected, private

#membuat public class
class segitiga:
    def __init__(self, alas, tinggi):
        self.alas = alas
        self.tinggi = tinggi
        self.luas = 0.5 * alas * tinggi;

#inisiasi 
segitiga_besar = segitiga(50, 40)

#print
print('ini adalah public class')
print (f'alas : {segitiga_besar.alas}')
print (f'tinggi : {segitiga_besar.tinggi}')
print (f'luas : {segitiga_besar.luas}')

#membuat protected class
class mobil: #class induk
    def __init__(self, merk):
        self._merk = merk #protected class declaration
        
class f1(mobil):
    def __init__(self, merk, total_gear):
        super().__init__(merk)
        self._toal_gear = total_gear
        
    def pamer(self):
        #hak akses_merk dari subclass
        print (f'ini mobil {self._merk} gear nya {self._toal_gear}\n')
        
#instantiasi
print('ini adalah protected class')
ferrari = f1('ferrari', 8)
ferrari.pamer()        
        
#membuat private calss
class motor:
    def __init__(self, merk):
        self.__merk = merk #private class declaration
        
    def tampilkan_merk(self):
        print(f'merk mototrnya : {self.__merk}')
        
        
#instantiasi
moge = motor('harley')
moge.tampilkan_merk()