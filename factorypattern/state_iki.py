
# STATE DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

class Lamba:
    def __init__(self):
        self.acik = False

    def ac(self):
        if not self.acik:
            print("Lamba açıldı.")
            self.acik = True
        else:
            print("Lamba zaten açık.")

    def kapat(self):
        if self.acik:
            print("Lamba kapatıldı.")
            self.acik = False
        else:
            print("Lamba zaten kapalı.")

# Örnek kullanım
if __name__ == "__main__":
    lamba = Lamba()

    lamba.ac()  # Lambayı aç
    lamba.kapat()  # Lambayı kapat

    lamba.ac()  # Lambayı tekrar aç
    lamba.ac()  # Açık lambayı açmaya çalış

    lamba.kapat()  # Açık lambayı kapat
    lamba.kapat()  # Kapalı lambayı tekrar kapatmaya çalış
