
# VISITOR DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

from abc import ABC

class Visitor(ABC):
    # visitor classı ile şekiller belirlenir ve tanımlamaları yapılır.
    # import ABC ile abstract class oluşumu sağlanmaktadır.

    def visit_kare(self, kare):
        pass
    def visit_daire(self, daire):
        pass
    def visit_yamuk(self,yamuk):
        pass

# alan hesaplamaları için teker teker visit_şekil yapıları oluşturulur.
class AlanHesaplayici(Visitor):
    def visit_kare(self, kare):
        return kare.kenar_uzunlugu ** 2

    def visit_daire(self, daire):
        return 3.14 * daire.yari_cap ** 2

    def visit_yamuk(self,yamuk):
        return (yamuk.alttaban+yamuk.usttaban)*yamuk.yukseklik/2

class Sekil(ABC):
    def accept(self, visitor):
        pass

# şekiller abstract üzerinden kabul gördüğü için accept ile alan hesaplamaları yapılır.
class Kare(Sekil):
    def __init__(self, kenar_uzunlugu):
        self.kenar_uzunlugu = kenar_uzunlugu

    def accept(self, visitor):
        return visitor.visit_kare(self)

class Daire(Sekil):
    def __init__(self, yari_cap):
        self.yari_cap = yari_cap

    def accept(self, visitor):
        return visitor.visit_daire(self)

class Yamuk(Sekil):
    def __init__(self,alttaban,usttaban,yukseklik):
        self.alttaban= alttaban
        self.usttaban=usttaban
        self.yukseklik=yukseklik

    def accept(self,visitor):
        return visitor.visit_yamuk(self)

if __name__ == "__main__":

    # nesne oluşturulur ve hesaplama için gerekli değerler verilir.
    alan_hesaplayici = AlanHesaplayici()
    kare = Kare(5)
    daire = Daire(3)
    yamuk=Yamuk(20,30,5)

    print(f"Kare Alanı: {kare.accept(alan_hesaplayici)} birim kare")
    print(f"Daire Alanı: {daire.accept(alan_hesaplayici)} birim kare")
    print(f"Yamuk Alanı: {yamuk.accept(alan_hesaplayici)} birim kare")
