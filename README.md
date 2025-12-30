# Kod Açıklaması – Brookshear Makinesi Simülasyonu

---

## Öğrenci bigileri

- **Ad Soyad:** Antsaniaina Zinha Tatiana Tanteliharisoa
- **Öğrenci numarası:** 24360859223

---

## Proje konusu

**Makine Dili ve Brookshear Mimarisi**

---

## Youtube linki

Sunum videosu aşağıdaki bağlantı üzerinden izlenebilir:
  https://youtu.be/VoVzWy8mhII

---

## Proje Açiklamasi

### I. Proje Tanımı

Bu proje, Python programlama dili kullanılarak Brookshear makinesini simüle eden
bir algoritma geliştirmek amacıyla gerçekleştirilmiştir.

Bu projenin amacı, makine komutlarının nasıl çalıştığını anlamak ve algoritmik
düşünme becerisini geliştirmektir.

---

### II. Kullanılan Dil ve Kütüphaneler

Proje, Python programlama dili kullanılarak geliştirilmiştir.  
Bu projede herhangi bir harici (external) kütüphane kullanılmamıştır.

Program yalnızca Python’un gömülü (built-in) fonksiyonlarını ve karakter dizileri
üzerinde çalışan temel metotları kullanmaktadır.

Kullanılan gömülü fonksiyonlar ve metotlar şunlardır:
- `.upper()`
- `.isalnum()`
- `any()`

---

### III. Programın Genel Çalışma Mantığı

Programın çalışma adımları aşağıdaki gibidir:

1. Kullanıcıdan bir hexadecimal kod alınır.
2. Kodun hanelerinin geçerli olup olmadığı kontrol edilir.
3. Kod, komut parçalarına ayrılır.
4. Algoritma tarafından kod analiz edilir ve hangi işlemi yaptığı açıklanır.
5. Uygun açıklama ekrana yazdırılır.

---

### IV. Algoritmanın Mantığı

Algoritma aşağıdaki adımları izler:

1. Kullanıcıdan alınan hexadecimal kod büyük harfe dönüştürülür.
2. Kodun uzunluğunun 4 haneli olup olmadığı kontrol edilir.
3. Kod içinde harf ve sayı dışında bir karakter olup olmadığı kontrol edilir.
4. Kod içinde A–F aralığı dışında bir harf olup olmadığı kontrol edilir.
5. Kod komut parçalarına ayrılarak opcode değeri belirlenir.
6. Opcode’a göre uygun açıklama seçilir.
7. Sonuç ekrana yazdırılır.

---

### V. Kodun Önemli Bölümlerinin Açıklanması

- `Harf=[...]` diziyi, geçerli haneleri belirtiyor.
- `kod=kod.upper()` metodu, kod içindeki harfleri büyük harfe çevirmek için kullanılır.
- `any(not element.isalnum() for element in kod)` ifadesi, kod içindeki tüm
  karakterlerin harf veya sayı olup olmadığını kontrol etmek için kullanılır.  
  Örneğin `*` karakteri geçersiz bir elemandır.
- `match ... case` yapısı, opcode değerine göre uygun açıklamayı seçmek için
  kullanılır.

---

### VI. Özet

Bu proje sayesinde Brookshear makinesinin temel çalışma prensipleri öğrenilmiştir.  
Ayrıca Python programlama dilinde string işlemleri, koşul yapıları ve algoritma
kurma becerileri geliştirilmiştir.

Gelecekte bu proje, birden fazla komutu işleyebilecek şekilde geliştirilebilir
veya görsel bir arayüz eklenebilir.
