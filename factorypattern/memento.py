#Memento design pattern de ana mantık; önceden yapılan işlemlerin hafızada tutulması ve bunun üzerine 
#sonraki aşamalarda çağrılabilmesidir.

class Memento:
    def __init__(self, durum):
        self.durum = durum


class Orijinator:
    def __init__(self):
        self.durum = None

    def durum_ayarla(self, durum):
        print("Orijinator: Durum ayarlandı ->", durum)
        self.durum = durum

    def memento_olustur(self):
        print("Orijinator: Memento oluşturuldu.")
        return Memento(self.durum)

    def mementodan_geri_yukle(self, memento):
        self.durum = memento.durum
        print("Orijinator: Durum geri yüklendi ->", self.durum)


class Bakici:
    def __init__(self):
        self.mementolar = []

    def memento_ekle(self, memento):
        self.mementolar.append(memento)

    def memento_al(self, indeks):
        return self.mementolar[indeks]


if __name__ == "__main__":
    orijinator = Orijinator()
    bakici = Bakici()

    orijinator.durum_ayarla("Durum 1")
    bakici.memento_ekle(orijinator.memento_olustur())

    orijinator.durum_ayarla("Durum 2")
    bakici.memento_ekle(orijinator.memento_olustur())

    orijinator.durum_ayarla("Durum 3")
    print("Mevcut durum:", orijinator.durum)

    orijinator.mementodan_geri_yukle(bakici.memento_al(1))
    print("Geri yüklenen durum:", orijinator.durum)
