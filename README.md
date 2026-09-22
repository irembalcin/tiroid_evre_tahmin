# tiroid_evre_tahmin
# 🩺 Tiroid Kanseri Karar Destek Sistemi

Bu proje, makine öğrenmesi algoritmaları kullanılarak tiroid kanseri hastalarının klinik bulgularına göre hastalık evresini (Stage) tahmin eden interaktif bir web uygulamasıdır. 

## 📌 Projenin Amacı
Biyoenformatik ve veri bilimi yaklaşımlarını birleştirerek, sağlık profesyonellerinin kullanabileceği pratik bir araç geliştirmektir. Laboratuvar ve muayene verilerini arka planda işleyen sistem, doktorlara saniyeler içinde evre tahmini sunarak ikinci bir görüş mekanizması oluşturur.

## 🛠️ Kullanılan Teknolojiler ve Kütüphaneler
* **Python:** Temel geliştirme dili
* **Scikit-Learn:** Karar Ağacı (Decision Tree) sınıflandırma algoritması ile modelin eğitilmesi
* **Pandas:** Veri manipülasyonu, temizleme ve One-Hot Encoding işlemleri
* **Streamlit:** Analitik modelin, son kullanıcıya (klinisyenlere) yönelik interaktif bir web paneline dönüştürülmesi

## 🚀 Sistem Nasıl Çalışır?
1. Sol menüdeki klinik giriş formundan hastaya ait yaş, patoloji tipi, tümör boyutu (T), lenf yayılımı (N) ve metastaz (M) gibi güncel parametreler seçilir.
2. Veriler, arka planda makine öğrenmesi modelinin anlayacağı sayısal matrislere dönüştürülür.
3. Eğitilmiş algoritma, hasta profiline en uygun klinik evreyi hesaplar ve anlık olarak ekrana yansıtır.
