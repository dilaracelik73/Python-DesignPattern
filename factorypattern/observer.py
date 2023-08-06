
# OBSERVER DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

# her yeni eklenim yapıldığında -- bu hem kişi hem de video için geçerli -- bildirim yollanacak.
class video_paylasım_sınıfı:
    def __init__(self):
        self.izleyiciler_dizisi = []
        self.eklenen_video = None

    def izleyici_ekle(self, izleyici):
        self.izleyiciler_dizisi.append(izleyici)

    def yeni_video_yukle(self, video):
        self.eklenen_video = video
        self.bildirim_gonder()

    def bildirim_gonder(self):
        for izleyici in self.izleyiciler_dizisi:
            izleyici.guncelle(self.eklenen_video)

#bilgi gösterimi yapılacak.
class izleyici_sınıfı:
    def __init__(self, isim):
        self.isim = isim

    def guncelle(self, video):
        print(f" İzleyici İsmi: {self.isim} , İzlenen Video: '{video}' ")


# Çalışma kısmı:
platform = video_paylasım_sınıfı()
 # isteğe bağlı olarak dışardan istemde yapılabilir.
izleyici1 = izleyici_sınıfı("Dilara")
izleyici2 = izleyici_sınıfı("Elif")
izleyici3 = izleyici_sınıfı("Demet")

platform.izleyici_ekle(izleyici1)
platform.izleyici_ekle(izleyici2)
platform.izleyici_ekle(izleyici3)

platform.yeni_video_yukle("Yolculukların Uzun Sürmesi")
platform.yeni_video_yukle("Oyunları Kazanma Yolları")

