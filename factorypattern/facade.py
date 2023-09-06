
# FACADE DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

# oluşturulması gereken ana sınıflar oluşturuldu
class motor:
    def baslat(self):
        print("Uçak motoru çalıştırıldı.")

    def durdur(self):
        print("Uçak motoru durduruldu.")


class yakıt_sistemi:
    def pompalamayı_ac(self):
        print("Yakıt dolumu yapıldı.")
        print("Yakıt pompalandı.")

    def pompalamayı_kapat(self):
        print("Yakıt pompalanması durduruldu.")


class elektrik_sistemi:
    def ac(self):
        print("Uçak elektrik sistemi açıldı.")

    def kapat(self):
        print("Uçak elektrik sistemi kapatıldı.")

# facade sınıfı oluşturuldu, nesneler - fonksiyonlar çağrıldı.
class arac_genel:
    def __init__(self):
        self._motor = motor()
        self._yakit_sistemi = yakıt_sistemi()
        self._elektrik_sistemi = elektrik_sistemi()

    def arac_baslat(self):
        print("Uçak çalıştırılmaya başlandı...")
        self._elektrik_sistemi.ac()
        self._yakit_sistemi.pompalamayı_ac()
        self._motor.baslat()
        print("Uçak çalıştırıldı ve kullanıma hazır.")

    def arac_durdur(self):
        print("Uçak durduruluyor...")
        self._motor.durdur()
        self._yakit_sistemi.pompalamayı_kapat()
        self._elektrik_sistemi.kapat()
        print("Uçak durduruldu ve kullanım dışı bırakıldı.")

# çalıştırma işlemleri burada yapılır.
if __name__ == "__main__":
    _arac_genel = arac_genel()

    # Arabayı başlatma
    _arac_genel.arac_baslat()
    print("\n****************")

    # Arabayı durdurma
    _arac_genel.arac_durdur()
