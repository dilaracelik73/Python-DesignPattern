
# DECORATOR DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:

from abc import ABC, abstractmethod

# genel yapı için interface oluşturulur.
class IPizza(ABC):
    def aciklama_al(self):
        pass

    def fiyat_al(self):
        pass

# genel yapı için ana class oluşturulur.
class TemelPizza(IPizza):
    def aciklama_al(self):
        return "Temel Pizza"

    def fiyat_al(self):
        return 100.0

# decorator sınıfı oluşturulur.
class PizzaDecorator(IPizza):
    def __init__(self, pizza):
        self._pizza = pizza

    def aciklama_al(self):
        return self._pizza.aciklama_al()

    def fiyat_al(self):
        return self._pizza.fiyat_al()


# Malzeme dekoratörleri
class PeynirDecorator(PizzaDecorator):
    def aciklama_al(self):
        return super().aciklama_al() + ", Peynir"

    def fiyat_al(self):
        return super().fiyat_al() + 25.0

class SucukDecorator(PizzaDecorator):
    def aciklama_al(self):
        return super().aciklama_al() + ", Sucuk"

    def fiyat_al(self):
        return super().fiyat_al() + 50.0

#çalıştırılan alan burada. gösterim temel pizzanın üstüne ekleme ile olur.
if __name__ == "__main__":
    pizza = TemelPizza()
    print("Açıklama: " + pizza.aciklama_al() + ", Fiyat: " + str(pizza.fiyat_al()))

    peynirli_pizza = PeynirDecorator(pizza)
    print("Açıklama: " + peynirli_pizza.aciklama_al() + ", Fiyat: " + str(peynirli_pizza.fiyat_al()))

    sucuklu_peynirli_pizza = SucukDecorator(peynirli_pizza)
    print("Açıklama: " + sucuklu_peynirli_pizza.aciklama_al() + ", Fiyat: " + str(sucuklu_peynirli_pizza.fiyat_al()))
