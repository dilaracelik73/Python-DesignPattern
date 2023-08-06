
# MEDIATOR DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

class Mediator:
    def __init__(self):
        self.kullanicilar = []
# kullanıcılar adında bir dizi oluşturulup elemanlar oraya eklenecektir.
    def kayit_ol(self, kullanici):
        self.kullanicilar.append(kullanici)
# eğer gönderen ve alan kişi aynı kişi değilse mesaj al fonksiyonu çalışacaktır.
    def mesaj_gonder(self, gonderen, mesaj):
        for kullanici in self.kullanicilar:
            if kullanici != gonderen:
                kullanici.mesaj_al(mesaj)

class Kullanici:
    def __init__(self, ad, mediator,zaman):
        self.ad = ad
        self.mediator = mediator
        self.zaman= zaman
# tüm tanımlamalar yapıldıktan sonra atılan mesaj hakkında, alan veya gönderen kişi hakkında ve
# mesaj zamanı hakkında bilgi verilir..
    def mesaj_gonder(self, mesaj):
        print(f" Gönderen: {self.ad} isimli kullanıcı, ' Gönderilen Mesaj: {mesaj}', 'Mesaj Zamanı : {self.zaman}'")
        self.mediator.mesaj_gonder(self, mesaj)

    def mesaj_al(self, mesaj):
        print(f" Alıcı: {self.ad} isimli kullanıcı, ' Alınan Mesaj: {mesaj}',' Mesaj Zamanı: {self.zaman}'")

if __name__ == "__main__":
    mediator = Mediator()

    kullanici1 = Kullanici("Dilara", mediator,"1 PM")
    kullanici2 = Kullanici("Elif", mediator,"1.20 PM")
    kullanici3 = Kullanici("Demet", mediator,"1.22 PM")

    mediator.kayit_ol(kullanici1)
    mediator.kayit_ol(kullanici2)
    mediator.kayit_ol(kullanici3)

#isteğe bağlı olarak mesaj ve kişiler hakkında bilgilendirmeler input olarakta alınabilir.

    kullanici1.mesaj_gonder("Bu ilk mesajdır!")
    kullanici2.mesaj_gonder("Bu ikinci mesajdır!")
