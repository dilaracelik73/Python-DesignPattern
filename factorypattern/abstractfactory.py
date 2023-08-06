
# ABSTRACT FACTORY DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

print(" Üretilecek parça kullanıcı tarafından seçilecektir,\n onun dışında otomatik üretimde yapılmaktadır!!")
parca_adı = input("lütfen üretilecek parçanın adını giriniz...")


# Abstract sınıfı gösterilmiştir:
class arac_parca:
    def üretim(self):
        pass


# Herhangi bir parçanın üretimi yapılacak, kullanıcıdan istenecek.
class HerhangiBirParça(arac_parca):
    def üretim(self):
        return f"{parca_adı} parçasının üretimi yapılacak."


#Arabanın motoru üretildi.
class arac_motoru(arac_parca):
    def üretim(self):
        return "Arabanın motoru üretildi."


# Arabanın kapıları üretildi.
class arac_kapı_on_sol(arac_parca):
    def üretim(self):
        return "Arabanın  ön sol kapısı üretildi."
class arac_kapı_on_sag(arac_parca):
    def üretim(self):
        return "Arabanın ön sağ kapısı üretildi."
class arac_kapı_arka_sol(arac_parca):
    def üretim(self):
        return "Arabanın arka sol  kapısı üretildi."
class arac_kapı_arka_sag(arac_parca):
    def üretim(self):
        return "Arabanın arka sağ kapısı üretildi."


# Soyut Araç Fabrikası (Abstract Car Factory) sınıfı
class car_factory:
    def create_motor(self):
        pass
    def create_onsol(self):
        pass
    def create_arkasol(self):
        pass
    def create_onsag(self):
        pass
    def create_arkasag(self):
        pass
    def create_something(self):
        pass


# Türkiye Araç Fabrikası (Turkish Car Factory) sınıfı
class Turk_fabrikası(car_factory):
    def create_motor(self):
        return arac_motoru()

    def create_onsol(self):
        return arac_kapı_on_sol()

    def create_onsag(self):
        return arac_kapı_on_sag()

    def create_arkasol(self):
        return arac_kapı_arka_sol()

    def create_arkasag(self):
        return arac_kapı_arka_sag()

    def create_something(self):
        return HerhangiBirParça()


# Almanya Araç Fabrikası (German Car Factory) sınıfı
class Alman_arac(car_factory):
    def create_motor(self):
        return arac_motoru()

    def create_onsol(self):
        return arac_kapı_on_sol()

    def create_onsag(self):
        return arac_kapı_on_sag()

    def create_arkasol(self):
        return arac_kapı_arka_sol()

    def create_arkasag(self):
        return arac_kapı_arka_sag()

    def create_something(self):
        return HerhangiBirParça()


# Araç Üretim Hattı (Car Production Line) sınıfı
class arac_uretim_hattı:
    def __init__(self, factory):
        self.motor = factory.create_motor()
        self.onsol = factory.create_onsol()
        self.onsag = factory.create_onsag()
        self.arkasol = factory.create_arkasol()
        self.arkasag = factory.create_arkasag()
        self.part = factory.create_something()

    def arac_uretim(self):
        print(self.motor.üretim())
        print(self.onsol.üretim())
        print(self.onsag.üretim())
        print(self.arkasol.üretim())
        print(self.arkasag.üretim())
        print(self.part.üretim())


# Kullanım Örneği
if __name__ == "__main__":
    # Türkiye için araç üretimi
    turkfabrika = Turk_fabrikası()
    arac_uretim_turk = arac_uretim_hattı(turkfabrika)
    print("Türkiye Üretimi:\n")
    arac_uretim_turk.arac_uretim()

    # Almanya için araç üretimi
    almanfabrika = Alman_arac()
    arac_uretim_alman = arac_uretim_hattı(almanfabrika)
    print("\nAlmanya Üretimi:")
    arac_uretim_alman.arac_uretim()

