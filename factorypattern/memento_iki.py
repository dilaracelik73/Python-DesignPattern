
# MEMENTO DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

# bunun ana mantığı ilk seferde elinde bir şey yok,
# ikinci seferde ilk yazılan yapı eklenecek ve kayıt altına alınacak.
# üçüncü seferde son ekleme yapılacak ve kaydedilecek.
# eğer geriye dönmek istersek geçmiş kayıtlara memento ile ulaşabileceğiz. (Oyun mantığı)

class metin_editoru_sınıfı:
    def __init__(self):
        self.metin = ""

    def yaz(self, metin):
        self.metin += metin

    def kaydet(self):
        return memento_sınıfı(self.metin)

    def geri_al(self, memento):
        self.metin = memento.getir_kayitli_metin()


class memento_sınıfı:
    def __init__(self, metin):
        self.kayitli_metin = metin

    def getir_kayitli_metin(self):
        return self.kayitli_metin


class metin_gecmis_sınıfı:
    def __init__(self):
        self.gecmis = []

    def ekle(self, memento):
        self.gecmis.append(memento)

    def pop(self):
        return self.gecmis.pop()


metin_editoru = metin_editoru_sınıfı()
metin_gecmisi = metin_gecmis_sınıfı()

metin_editoru.yaz("Bu ilk kayıt, ")
print(metin_gecmisi.ekle(metin_editoru.kaydet()))  # Durumu kaydet, None olur.

metin_editoru.yaz("bu ikinci kayıt!")
print(metin_editoru.metin)  # Çıktı: Bu ilk kayıt, bu ikinci kayıt  olur

metin_editoru.geri_al(metin_gecmisi.pop())  # Önceki duruma geri al
print(metin_editoru.metin)  # Çıktı: Bu ilk kayıt,

