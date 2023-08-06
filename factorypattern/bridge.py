
# BRIDGE DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

class ILamba:
    def ac(self):
        pass

    def kapat(self):
        pass

print(" **** Manuel anahtar ile floresan lamba ilişkilendirildi *****")
print(" **** Uzaktan kontrollü anahtar ile halojen lamba ilişkilendirildi ****  \n")


class floresan_lamba(ILamba):
    def ac(self):
        print("Floresan lamba açıldı.")

    def kapat(self):
        print("Floresan lamba kapatıldı.")

class led_lamba(ILamba):
    def ac(self):
        print("Halojen lamba açıldı.")

    def kapat(self):
        print("Halojen lamba kapatıldı.")

class IAnahtar:
    def ac(self):
        pass

    def kapat(self):
        pass


class manuel_anahtar(IAnahtar):
    def __init__(self, lamba):
        self._lamba = lamba

    def ac(self):
        print("Manuel anahtar açıldı.")
        self._lamba.ac()

    def kapat(self):
        print("Manuel anahtar kapatıldı.")
        self._lamba.kapat()

class uzaktan_kontrollu_anahtar(IAnahtar):
    def __init__(self, lamba):
        self._lamba = lamba

    def ac(self):
        print("Uzaktan kontrollü anahtar açıldı.")
        self._lamba.ac()

    def kapat(self):
        print("Uzaktan kontrollü anahtar kapatıldı.")
        self._lamba.kapat()

if __name__ == "__main__":
    flo_lamba = floresan_lamba()
    ledli_lamba = led_lamba()

    manuel_anahtar = manuel_anahtar(flo_lamba)
    uzak_kontrol = uzaktan_kontrollu_anahtar(ledli_lamba)

    manuel_anahtar.ac()
    manuel_anahtar.kapat()

    uzak_kontrol.ac()
    uzak_kontrol.kapat()
