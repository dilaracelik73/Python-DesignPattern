
# STRATEGY DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

from abc import ABC, abstractmethod

# Sıralama stratejisi için abstract kullanıldı.
class SiralamaStratejisi(ABC):
    @abstractmethod
    def sirala(self, liste):
        pass

# Bazı sınıflar sıralama olaylarını organize etmek için yapıldı.
class KabarcikSiralama(SiralamaStratejisi):
    def sirala(self, liste):
        print("Kabarcık sıralaması :")
        return sorted(liste)

class HizliSiralama(SiralamaStratejisi):
    def sirala(self, liste):
        print("Hızlı sıralama :")
        return sorted(liste)

class SecmeliSiralama(SiralamaStratejisi):
    def sirala(self, liste):
        print("Seçmeli sıralama :")
        return sorted(liste)

# Sıralama işlemi  sınıfı
class Siralayici:
    def __init__(self, strateji):
        self.strateji = strateji

    def sira(self, liste):
        return self.strateji.sirala(liste)

    def strateji_degistir(self, yeni_strateji):
        self.strateji = yeni_strateji


if __name__ == "__main__":
    kabarcik = KabarcikSiralama()
    hizli = HizliSiralama()
    secmeli = SecmeliSiralama()

    siralayici = Siralayici(kabarcik)
    liste = [10, 3, 7, 1, 5]

    siralanan_liste = siralayici.sira(liste)
    print("En son liste:", siralanan_liste)

    siralayici.strateji_degistir(hizli)
    siralanan_liste = siralayici.sira(liste)
    print("En son liste:", siralanan_liste)

    siralayici.strateji_degistir(secmeli)
    siralanan_liste = siralayici.sira(liste)
    print("En son liste:", siralanan_liste)
