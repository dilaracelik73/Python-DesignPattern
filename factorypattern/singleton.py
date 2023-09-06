
# SINGLETON DESIGN PATTERN KOD ÖRNEĞİ- PYTHON:
#Bunun çalışma mantığında ise asıl olay; tüm işlemlerin tek taraftan çağrılabilir olmasıdır.

class Singleton:
    örnek = None
# super() ile bir üst sınıftaki  metodlar çağrılır.
    def __new__(classımız):
        if classımız.örnek is None:
            classımız.örnek = super().__new__(classımız)
            classımız.örnek.data = []
        return classımız.örnek

    def add_data(self, value):
        self.data.append(value)

    def get_data(self):
        return self.data

# Çalışma alanı:
if __name__ == "__main__":
    singleton1 = Singleton()
    singleton1.add_data("Eklenen yapı 1")
    singleton1.add_data("Eklenen yapı 2")
    print("Singleton 1 :", singleton1.get_data())

    singleton2 = Singleton()
    singleton2.add_data("Eklenen yapı 3")
    print("Singleton 2 :", singleton2.get_data())

    print(singleton1 == singleton2)  # Çıktı: True
    # her ikiside aynı sınıftann türetildi.
