# 🧩 Python Design Patterns

Bu repo, Python dili ile **tasarım desenleri (Design Patterns)** ve **MVC (Model–View–Controller)** mimarisinin temel örneklerini içerir.  
Amaç: Tasarım desenlerini pratik örneklerle öğrenmek, yazılım geliştirmede tekrar eden problemlere standart çözümler geliştirmektir.


## 🎯 Design Pattern Nedir?
**Design Pattern (Tasarım Deseni)**: Yazılım geliştirme sürecinde sık karşılaşılan problemlere yönelik, tekrar kullanılabilir ve test edilmiş çözüm şablonlarıdır.  

**Avantajları:**
- Kodun **tekrar kullanılabilirliğini** artırır  
- **Bakımı** kolaylaştırır  
- Yazılımda **esneklik** ve **genişletilebilirlik** sağlar  
- Ortak bir **dil/standart** kazandırır  

> Örneğin: "Factory" ile nesne oluşturma sorumluluğunu soyutlayabilir, "Observer" ile bir nesnedeki değişikliği diğer nesnelere otomatik yansıtabilirsin.



## 🧭 MVC Nedir?
**Model–View–Controller (MVC)**:  
Bir uygulamanın iş mantığını (Model), kullanıcı arayüzünü (View) ve kontrol akışını (Controller) birbirinden ayıran yazılım mimarisidir.

- **Model:** Veri ve iş kurallarını barındırır (örn. `User`, `Todo`).  
- **View:** Kullanıcıya gösterilen kısım (örn. HTML şablonu, CLI çıktısı).  
- **Controller:** Model ve View arasında köprü görevi görür; akışı yönetir.  

**Faydası:** Kodun sorumluluklara ayrılması sayesinde daha **modüler, test edilebilir ve sürdürülebilir** yazılım geliştirilir.


## 🧠 Klasördeki Design Pattern Örnekleri

### Creational Patterns (Yaratımsal)
- **Factory (factory_uc.py, factory_iki.py)** → Nesne üretimini merkezi yapıya devreder.
- **Abstract Factory (abstractfactory.py)** → Birbiriyle uyumlu ürün ailelerini birlikte üretir.
- **Builder (build.py)** → Karmaşık nesneyi adım adım inşa eder.
- **Singleton (singleton.py)** → Uygulama boyunca tek örnek garantisi verir.

### Structural Patterns (Yapısal)
- **Adapter (adapter.py, adapter_iki.py)** → Farklı arayüzleri uyumlu hale getirir.
- **Bridge (bridge.py)** → Soyutlama ile implementasyonu ayırır.
- **Composite (—)** → (Eğer eklenecekse) Ağaç yapıları temsil eder.
- **Decorator (decorator.py)** → Sınıfa dokunmadan davranış ekler.
- **Facade (facade.py, facade_iki.py)** → Karmaşık alt sistemlere tek basit arayüz sunar.

### Behavioral Patterns (Davranışsal)
- **Chain of Responsibility (chainofres.py)** → İstekleri sırayla işleyen handler zinciri.
- **Iterator (iterator.py)** → Koleksiyon öğelerine sıralı erişim sağlar.
- **Mediator (mediator.py)** → Nesneler arası iletişimi merkezi aracı ile yönetir.
- **Memento (memento.py, memento_iki.py)** → Nesnenin durumunu kaydedip geri yükler.
- **Observer (observer.py)** → Bir nesnedeki değişiklikleri diğerlerine bildirir.
- **State (state.py, state_iki.py)** → Nesnenin davranışı durumuna göre değişir.
- **Strategy (strategy.py)** → Algoritmaların birbirinin yerine geçebilir şekilde tanımlanması.
- **Visitor (visitor.py)** → Nesne yapısına yeni operasyon eklemeden farklı işlemler uygular.

---

🔎 **Not:** Her dosya bağımsız, minimal bir Python örneği içerir. Çalıştırmak için:  
```bash

## ▶️ Çalıştırma
Her dosya **bağımsız çalıştırılabilir** bir Python örneği içerir:
python abstractfactory.py
python strategy.py
# vs.

```bash
# Örnek: Factory pattern
cd factorypattern
python factory_uc.py

# Örnek: Strategy pattern
python strategy.py

# MVC örneği
cd ../mvc
python main.py

```

## 🤝 Katkı

Katkılar memnuniyetle kabul edilir!
- Fork’la
- Branch aç: feature/isim
- Değişikliklerini yap + test et
- PR aç: değişiklik özetini ve nedenini yaz

## 📜 Lisans
MIT © 2025 Dilara Çelik
