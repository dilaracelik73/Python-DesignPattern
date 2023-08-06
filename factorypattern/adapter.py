
# ADAPTER DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

# ana sistemde var olan dizinler gösterilmiştir.
class dizinler:
    def listele(self):
        return ["dosya.txt", "ana klasör", "belge.txt", "alt klasör"]

# ana dosyalarımız gösterilmiştir.
class dosyalar:
    def dosyaları_listele(self):
        pass

# adapter sınıfı oluşturulmuştur.
class dizin_adapter(dosyalar):
    def __init__(self, dizin_sistemi):
        self._dizin_sistemi = dizin_sistemi

    def dosyaları_listele(self):
        return self._dizin_sistemi.listele()

# çalıştırma alanı.
if __name__ == "__main__":
    dizin_sistemi = dizinler()
    adapter = dizin_adapter(dizin_sistemi)

    dosya_sistemi = dosyalar()
    print("Dosyalar (Doğrudan Erişim):", dosya_sistemi.dosyaları_listele())
    print("Dosyalar (Adapter Kullanarak):", adapter.dosyaları_listele())
