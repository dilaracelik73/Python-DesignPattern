
# CHAINS OF REPOSIBILITY  DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

class Siparis:
    def __init__(self, siparis_numarasi, urun, miktar):
        self.siparis_numarasi = siparis_numarasi
        self.urun = urun
        self.miktar = miktar
        #siparişlerde genel olan yapıların tanımlaması yapılır.

class Mutfak:
    def __init__(self, sonraki=None):
        self.sonraki = sonraki
        #chain of responsibility yapısında zincirleme bir yapı olduğu için aktarım yapmamız lazım.
        # o yüzden aşağıdaki fonksiyonu her mutfak kategorisinde çalıştırmamız lazım.

    def siparisi_isle(self, siparis):
        if self.sonraki:
            self.sonraki.siparisi_isle(siparis)

class Birinci_Ascı(Mutfak):
    def siparisi_isle(self, siparis):
        if siparis.urun == "Beyti":
            print(f" Birinci aşçı, Sipariş {siparis.siparis_numarasi} için {siparis.miktar} porsiyon Beyti hazırlıyor.")
        else:
            super().siparisi_isle(siparis)

class İkinci_Ascı(Mutfak):
    def siparisi_isle(self, siparis):
        if siparis.urun == "İskender":
            print(f" İkinci aşçı, Sipariş {siparis.siparis_numarasi} için {siparis.miktar} porsiyon İskender yapıyor.")
        else:
            super().siparisi_isle(siparis)

class Kızartıcı(Mutfak):
    def siparisi_isle(self, siparis):
        if siparis.urun == "Sebze Kızartması":
            print(f" Kızartıcı, Sipariş {siparis.siparis_numarasi} için {siparis.miktar} porsiyon Sebze Kızartması kızartıyor.")
        else:
            super().siparisi_isle(siparis)

# toplamda 3 tane mutfak kategorisi fonksiyonu var ve hepsinin en son bağlantı noktası İkinci_Ascı .
# O yüzden , onun  nesnesinden türetilecek.

if __name__ == "__main__":
    kizartici = Kızartıcı()
    asci = Birinci_Ascı(kizartici)
    ascı = İkinci_Ascı(asci)

    siparis1 = Siparis(1, "Beyti", 2)
    siparis2 = Siparis(2, "İskender", 1.5)
    siparis3 = Siparis(3, "Sebze Kızartması", 1)

    ascı.siparisi_isle(siparis1)
    ascı.siparisi_isle(siparis2)
    ascı.siparisi_isle(siparis3)
