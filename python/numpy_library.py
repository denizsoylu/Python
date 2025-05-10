import veri_analizi_numpy as np

"""
--> numpy, "Numerical Python" (Sayısal Python) ifadesinin kısaltmasıdır.
--> bilimsel hesaplamalar için kullanılır.
--> En önemli özelliği: N boyutlu diziler (array) ile hızlı ve verimli işlem yapabilmesidir.
--> Bilimsel ve istatistiksel hesaplamalar desteklenir.
--> Verimli veri saklama ve vektörel operasyonlardır.
--> Numpy'ı listelerden ayıran iki önemli nokta vardır. 
    1- Verimli veri saklama.
    2- Yüksek seviyeden işlemlerdir, vektörel işlemlerdir.
--> Numpy sabit tipte veri tutar. Bu da verimli veri saklama imkanı sağlar.
--> Sabit tipte veri sakladığı için hızlı çalışır.
--> Her verinin ayrı ayrı tipini tutmaz, tek bir tip tutar ve 
    o tipteki verileri içinde saklar ve daha hızlıdır.
"""

#iki tane listeyi çarpmak istiyoruz

#numpy kullanılmadan bu şekilde yapılır.

a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])




#numpy kullanılarak bu şekilde yapılır.

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b



#####################################################
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
#####################################################
import veri_analizi_numpy as np

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))

#sıfırlardan oluşan bir array oluşturma
np.zeros(10, dtype=int)

#verilen aralıkta random array oluşturma
np.random.randint(0, 10, size=10)

#bu yukarıdakiyle aynı şey başlangıç girilmezse kabul eder
np.random.randint(0, 10, size=10)

#istatistiksel dağılıma göre array oluşturma
#ortalama 10, standart sapma 4, boyut (3,4)
np.random.normal(10, 4, (3, 4))


#############################################
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
#############################################
import veri_analizi_numpy as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)
a.ndim
a.shape
a.size
a.dtype


#############################################
# Yeniden Şekillendirme (Reshaping)
#############################################
import numpy as np

np.random.randint(1, 10, size=9)

#boyutunu reshape ile değiştiriyoruz
np.random.randint(1, 10, size=9).reshape(3,3)
ar = np.random.randint(1, 10, size=9)
ar.reshape(3,3)
#mesela 10 elemanlı bir arrayi 3,3 lük yapıya çeviremeyiz hata verir
ar = np.random.randint(1, 10, size=10)
ar.reshape(3,3)


#############################################
# Index Seçimi (Index Selection)
#############################################

import veri_analizi_numpy as np

a = np.random.randint(10, size=10)
a[0]
a[0:5] #sol taraftaki dahil sağ taraftaki hariç [dahil, hariç]
a[0] = 999

#iki boyutlu olursa ne olur?
m = np.random.randint(10, size=(3,5))
m[0, 0]
m[1, 1]
m[2, 3] = 88   # [satır, sütun]
m[2, 3] = 999.1 #sadece 999 kısmını alır

m[:, 0] #bütün satırları seç ve 0.sütunu seç
m[:, 1] #bütün satırları seç ve 1.sütunu seç
m[:, 2] #bütün satırları seç ve 2.sütunu seç
m[:, 3] #bütün satırları seç ve 3.sütunu seç
m[:, 4] #bütün satırları seç ve 4.sütunu seç

m[0, :] #bütün sütunları seç ve 0.satırı seç
m[1, :] #bütün sütunları seç ve 1.satırı seç
m[2, :] #bütün sütunları seç ve 2.satırı seç


#seçilecek satır ve sütun aralıklarını seçme
m[0:2 , 0:3]



#############################################
# Fancy Index
#############################################
"""Fancy Indexing (Süslü İndeksleme), 
NumPy'de bir dizi (array) içerisinden birden fazla öğeyi liste, 
dizi veya boolean maske kullanarak seçme işlemidir. 
Normal indekslemeden farklı olarak, tek bir değer yerine 
birden çok değeri aynı anda seçmeye yarar."""
import numpy as np

#0'dan 30'a kadar 3er 3er artsın
v = np.arange(0, 30, 3)
v[1]
v[4]
v[5]

catch = [1, 2, 3]
v[catch]


#############################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
#############################################
import numpy as np

v = np.array([1, 2, 3, 4, 5])

ab = []

# Klasik yöntem ile

for i in v:
    if i < 3:
        ab.append(i)


#Numpy ile

v < 3
v[v < 3]
v[v > 3]
v[v != 3]
v[v == 3]
v[v >= 3]



#############################################
# Matematiksel İşlemler (Mathematical Operations)
#############################################

import numpy as np

v = np.array([1, 2, 3, 4, 5])
v / 5
v * 5 / 10
v ** 2
v - 1


np.subtract(v, 1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)
v = np.subtract(v, 1)


# NumPy ile İki Bilinmeyenli Denklem Çözümü

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]]) #katsayılar
b = np.array([12, 10]) #sonuçlar

np.linalg.solve(a, b)