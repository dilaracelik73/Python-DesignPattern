
# BUILD DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

# İstemler isteğe bağlı olarak dışarıdan da alınabilir.
islemci=input("işlemci giriniz:")
bellek=input("bellek giriniz:")
depolama=input("depolama giriniz:")
ekran_karti=input("ekran kartı giriniz:")
ram=input("ram giriniz:")

# Product sınıfı oluşturuldu. None ataması yapıldı.
class Bilgisayar:
    def __init__(self):
        self.islemci = islemci
        self.bellek = bellek
        self.depolama = depolama
        self.ekran_karti = ekran_karti
        self.ram = ram

    def __str__(self):
        return f"Bilgisayar: İşlemci={self.islemci}, Bellek={self.bellek}, Depolama={self.depolama}," \
               f" Ekran Kartı={self.ekran_karti}, RAM={self.ram}"


# Builder sınıfı ile fonksiyonlar oluşturuldu.
class bilgisayar_oluştur:
    def islemci_ekle(self):
        pass

    def bellek_ekle(self):
        pass

    def depolama_ekle(self):
        pass

    def ekran_karti_ekle(self):
        pass

    def ram_ekle(self):
        pass

    def bilgisayar_al(self):
        pass


# Oluşturucu sınıfını oluşturuyoruz.
class oyun_bilgisayarı_oluştur (bilgisayar_oluştur):
    def __init__(self):
        self.bilgisayar = Bilgisayar()

    def islemci_ekle(self):
        self.bilgisayar.islemci = islemci

    def bellek_ekle(self):
        self.bilgisayar.bellek = bellek

    def depolama_ekle(self):
        self.bilgisayar.depolama = depolama

    def ekran_karti_ekle(self):
        self.bilgisayar.ekran_karti = ekran_karti

    def ram_ekle(self):
        self.bilgisayar.ram = ram

    def bilgisayar_al(self):
        return self.bilgisayar


# Director sınıfı oluşturuldu.
class bilgisayar_yönetici_oluştur:
    def __init__(self, oluşturucu):
        self.oluşturucu = oluşturucu

    def bilgisayar_olustur(self):
        self.oluşturucu.islemci_ekle()
        self.oluşturucu.bellek_ekle()
        self.oluşturucu.depolama_ekle()
        self.oluşturucu.ekran_karti_ekle()
        self.oluşturucu.ram_ekle()

    def bilgisayar_al(self):
        return self.oluşturucu.bilgisayar_al()


# Kullanım Örneği
if __name__ == "__main__":
    oyun_bilgisayari_olusturucu = oyun_bilgisayarı_oluştur()
    bilgisayar_yönetici = bilgisayar_yönetici_oluştur(oyun_bilgisayari_olusturucu)

    bilgisayar_yönetici.bilgisayar_olustur()
    oyun_bilgisayari = bilgisayar_yönetici.bilgisayar_al()
    print(oyun_bilgisayari)
