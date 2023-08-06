
# ITERATOR DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

# Kod ana mantığında; foreach ile okunan bir yapıyı iterator atayarak ve index tutarak nasıl
# kodlayabilir ve elimizdeki diziyi nasıl okuyabiliriz, düşüncesi hakimdir.

class KitapIterator:
    def __init__(self, kitaplar):
        self.kitaplar = kitaplar
        self.mevcut_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Bu kısımda liste okuma kısmı yapılmıştır. İndex ve dizi uzunluğu baz alınmıştır.
        if self.mevcut_index < len(self.kitaplar):
            mevcut_kitap = self.kitaplar[self.mevcut_index]
            self.mevcut_index += 1
            return mevcut_kitap
        else:
            raise StopIteration

if __name__ == "__main__":
    kitaplar_dizisi = ["Beyaz Diş", "Küçük Prens", "Sol Ayağım", "Doktor", "Kız Kardeşim Bir Seri Katil"]
    kitap_iterator = KitapIterator(kitaplar_dizisi)

    for kitap in kitap_iterator:
        print("Kitap İsmi: " ,kitap)
