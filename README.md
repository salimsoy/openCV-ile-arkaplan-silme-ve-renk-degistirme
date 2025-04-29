Projenin Amacı:
İlgili görseldeki gülün arka planını siyah yapıp, detayları kaybetmeden gülü mor hale çevirmek.

Nasıl Çalışır?
Kullanılacak olan input.jpg görseli okunur
Görsel HSV formatına çevrilir.
Trackbar kullanarak inRange metodundaki lower değerleri belirlenir ve maske oluşturulur.
Maske üzerindeki gürültüler morfolojik işlemlerle (kapama ve açma) temizlenir.
Sadece maskelenmiş bölgedeki (gül) renk tonu mor renge çevrilir.
Sonuç görselleştirilir ve output.jpg olarak kaydedilir.
