
# ADAPTER DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

# Birbirinden farklı iki ses aleti adapter nesnesi ile uyumlu hale getirilmiştir.
class SesCalar:
    def cal(self):
        pass

# MP3 ses formatı çalma sınıfı
class Mp3Calar:
    def cal(self):
        print("MP3 dosyası çalınıyor")


# MP4 ses formatı çalma sınıfı
class Mp4Calar:
    def cal(self):
        print("MP4 dosyası çalınıyor")


# Adapter sınıfı oluşturuldu.
class SesAdapter(SesCalar):
    def __init__(self, ses_calar):
        self.ses_calar = ses_calar

    def cal(self):
        print("Ses formatı uyumlu hale getiriliyor: ")
        self.ses_calar.cal()

if __name__ == "__main__":
    mp3_calar = Mp3Calar()
    mp3_adapter = SesAdapter(mp3_calar)

    mp4_calar = Mp4Calar()
    mp4_adapter = SesAdapter(mp4_calar)

    mp3_adapter.cal()
    mp4_adapter.cal()
