
# STATE DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

from abc import ABC, abstractmethod

#durumların oluşturulduğu abstract sınıfımız.
class Durum(ABC):

    def para_cek(self, miktar):
        pass

    def para_yatir(self, miktar):
        pass

#durumların özellikleri atanan sınıflarımız.
class bekleme_durumu_sınıfı(Durum):
    def para_cek(self, miktar):
        print(f"çekilen para: {miktar} ")
        return para_cekildi_durumu()

    def para_yatir(self, miktar):
        print(f" yatırılan para: {miktar} ")

class para_cekildi_durumu(Durum):
    def para_cek(self):
        print("Lütfen bekleyin, önceki işlem tamamlanmadı.")

    def para_yatir(self, miktar):
        print(f" yatırılan para: {miktar}.")
        return bekleme_durumu_sınıfı()

# genel sınıf düzenlemesi yapılır.
class ATM:
    def __init__(self):
        self.durum = bekleme_durumu_sınıfı()

    def durumu_degistir(self, yeni_durum):
        self.durum = yeni_durum

    def para_cek(self, miktar):
        self.durum = self.durum.para_cek(miktar)

    def para_yatir(self, miktar):
        self.durum = self.durum.para_yatir(miktar)

# çalıştırma alanı
if __name__ == "__main__":
    atm = ATM()

    atm.para_cek(350)
    atm.para_yatir(1000)
    atm.para_cek(755)
    atm.para_yatir(2547)
