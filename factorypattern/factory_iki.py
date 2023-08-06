
# FACTORY DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

# Herhangi bir içecek ismi alınır
isim = input("Lütfen içecek ismini giriniz:")

# İçecek  sınıfı oluşturulur.
class Icecek:
    def servis_et(self):
        pass

# Çay  sınıfı oluşturulur.
class Cay(Icecek):
    def servis_et(self):
        return "Çay servisi yapıldı.."

# Kahve  sınıfı oluşturulur.
class Kahve(Icecek):
    def servis_et(self):
        return "Kahve servisi yapıldı."

# Direkt olarak girilen içecek ismine göre servis yapılır.
class HerhangiBiri(Icecek):
    def servis_et(self):
        return f"{isim} servisi yapıldı."

# Factory sınıfı oluşturulur.
class icecek_factory:
    @staticmethod # bunla tek bir yapı alınmasuı sağlandı.
    def icecek_olustur(icecek_turu):
        if icecek_turu == "çay":
            return Cay()
        elif icecek_turu == "kahve":
            return Kahve()
        elif icecek_turu == isim:
            return HerhangiBiri()

# İstemci kod
if __name__ == "__main__":
    fabrika = icecek_factory()

    icecek1 = fabrika.icecek_olustur("çay")
    print(icecek1.servis_et())

    icecek2 = fabrika.icecek_olustur("kahve")
    print(icecek2.servis_et())

    icecek3 = fabrika.icecek_olustur(isim)
    print(icecek3.servis_et())
