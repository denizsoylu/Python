###############################################
# Python Alıştırmalar
###############################################







###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################
x = 8
type(x)  #int

y = 3.2
type(y)  #float

z = 8j + 18
type(z)  #complex

a = "Hello World"
type(a)  #string

b = True
type(b)  #boolean

c = 23 < 22
type(c)  #boolean

l = [1, 2, 3, 4]
type(l)  #list

d = {"Name" : "Jake",
     "Age" : 27,
     "Adress" : "Downtown"}
type(d)  #dictionary

"""
Sıralıdır - elemanların bir sırası vardır ve t[0] ile erişilebilir
Değiştirilemez -> Bir kez oluşturulduktan sonra içeriği değiştirilemez.
Aynı elemendan birden fazla kez olabilir.
"""
t = ("Machine Learning", "Data Science")
type(t)  #tuple
t[0]

"""
Sırasızdır - Elemanlara erişilemez
Değiştirilebilir - Eleman eklenip silinebilir
Aynı eleman bir kez olabilir
"""
s = {"Python", "Machine Learning", "Data Science"}
type(s)   #set
"""
Bu kod hata vermez, çünkü Python set tanımlandığında yinelenen 
(duplicate) elemanları otomatik olarak kaldırır."""
k = {"Python", "Python", "Machine Learning", "Data Science"}
print(k)










###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
# Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################


text = "The goal is to turn data into information, and information into insight."

# Bütün harfleri büyüğe çevirmek için .upper() metodu kullanılır.
textupper = text.upper()

# Belirli karakterleri başka bir karakterle veya yazıyla değiştirmek için .replace() metodu kullanılır.
textreplace = textupper.replace(",", " ")
textreplace2 = textreplace.replace(".", " ")

# Metni kelime kelime ayırmak için .split() metodu kullanılır.
output = textreplace2.split()
#['THE', 'GOAL', 'IS', 'TO', 'TURN', 'DATA', 'INTO', 'INFORMATION', 'AND', 'INFORMATION', 'INTO', 'INSIGHT']













###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################


lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
"""
remove(x)    --> Değeri x olan ilk elemanı siler.
pop(i)       --> i. indeksteki elemanı siler
pop()	     --> Son elemanı siler
del liste[i] --> i. indeksteki elemanı siler
clear()	     --> Listenin tüm elemanlarını siler
"""
len(lst)           # eleman sayısını söyler
lst[0]             # 0. elemanı çağırır
lst[10]            # 1. elemanını çağırır
list2 = lst[0:4]   # ['D', 'A', 'T', 'A' ] listesi oluşturulur
lst.pop(8)         # 8. indeksteki eleman silimir
lst.append("DATA") # Yeni eleman eklendi
lst.insert(8,"N")






###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################

dict = {'Christian' : ["America", 18],
        'Daisy' : ["England", 12],
        'Antonio' : ["Spain", 22],
        'Dante' : ["Italy", 25]}


# Adım 1: Key değerlerine erişiniz.

dict.keys()


# Adım 2: Value'lara erişiniz.

dict.values()

# Adım 3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.

dict["Daisy"][1] = 13
dict.update({"Daisy": ["England", 13]})

# Adım 4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.

dict.update({"Ahmet": ["Turkey", 24]})
dict["Ahmet"] = ["Turkey", 24]

# Adım 5: Antonio'yu dictionary'den siliniz.

del dict["Antonio"]






###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

l = [2,13,18,93,22]


def ayir (liste):
    c = []  # c ve k'yı fonksiyonun içine tanımlamamızın sebebi
    t = []  #her çağrıda listeler temiz başlasın ve eski veriler kalmasın.
    for i in liste:
        if i % 2 == 0:
         c.append(i)
        else:
            t.append(i)

    return c , t

ayir(l)
type(ayir(l))







###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde
# dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını
# temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]



def basariSirala(ogrenciListesi):
    print("Mühendislik başarı sırası")
    for index, ogrenci in enumerate(ogrenciler[:3], start=1):
        print(index, ogrenci)

    print("Tıp başarı sırası")
    for index, ogrenci in enumerate(ogrenciler[3:], start=1):
        print(index, ogrenci)

basariSirala(ogrenciler)







###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir.
# Listelerde sırası ile bir dersin kodu, kredisi ve
# kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]

list(zip(ders_kodu, kredi, kontenjan))









###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor
# ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin
# 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

def kontrol(kume1, kume2):
    if kume1.issuperset(kume2):
        print(kume1.intersection(kume2))
    else:
        print(kume2.difference(kume1))

kontrol(kume1, kume2)

# 1. add --> Kümenin içine bir eleman ekler.
# 2. remove --> Belirtilen elemanı siler. Eleman yoksa hata verir.
# 3. discard --> Belirtilen elemanı siler. Eleman yoksa hata vermez.
# 4. clear --> Kümenin tüm elemanlarını siler. Küme boş hale gelir.
# 5. intersection --> Kesişim. İki kümenin ortak elemanlarını döner.
# 6. union --> Birleşim. İki kümenin tüm elemanlarını (tekrarsız) döner.
# 7. difference --> Fark. İlk kümede olup ikinci kümede olmayanları döner.
# 8. symmetric_difference --> Sadece birinde olanları döner, ortakları çıkarır.
# 9. issubset --> Alt küme. İlk küme, ikinci kümenin alt kümesi mi? (True/False)
# 10. issuperset --> Kapsayıcı mı? İlk küme, ikinci kümeyi kapsıyor mu? (True/False)
# 11. isdisjoint --> Ortak eleman yok mu? Küme kesişimi boş mu? (True/False)



kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

# 1. add --> Kümenin içine bir eleman ekler.
kume1.add("ai")
kume1.add("ml")
kume1.add("dp")
kume1.add("mp")

kume2.add("deep learning")
kume2.add("numpy")
kume2.add("mp")

# 2. remove --> Belirtilen elemanı siler. Eleman yoksa hata verir.
kume1.remove("dp")
kume2.remove("mp")
# 3. discard --> Belirtilen elemanı siler. Eleman yoksa hata vermez.
kume1.discard("mp")
kume2.discard("mp")
# 4. clear --> Kümenin tüm elemanlarını siler. Küme boş hale gelir.
kume1.clear()
kume2.clear()
# 5. intersection --> Kesişim. İki kümenin ortak elemanlarını döner.
kume1.intersection(kume2)
kume2.intersection(kume1)
# 6. union --> Birleşim. İki kümenin tüm elemanlarını (tekrarsız) döner.
kume1.union(kume2)
kume2.union(kume1)
# 7. difference --> Fark. İlk kümede olup ikinci kümede olmayanları döner.
kume1.difference(kume2)  # 1'in 2'den farkı → kume1'de olup kume2'de olmayanlar
kume2.difference(kume1)  # 2'nin 1'den farkı → kume2'de olup kume1'de olmayanlar
# 8. symmetric_difference --> Sadece birinde olanları döner, ortakları çıkarır.
kume1.symmetric_difference(kume2)
kume2.symmetric_difference(kume1)
# 9. issubset --> Alt küme. İlk küme, ikinci kümenin alt kümesi mi? (True/False)
kume1.issubset(kume2)
kume2.issubset(kume1)
# 10. issuperset --> Kapsayıcı mı? İlk küme, ikinci kümeyi kapsıyor mu? (True/False)
kume1.issuperset(kume2)
kume2.issuperset(kume1)
# 11. isdisjoint --> Ortak eleman yok mu? Küme kesişimi boş mu? (True/False)
kume1.isdisjoint(kume2)
kume2.isdisjoint(kume1)








##################################################
# List Comprehensions
##################################################

# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak
#  car_crashes verisindeki numeric değişkenlerin isimlerini
#  büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.


import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()

[col.upper() if not pd.api.types.is_numeric_dtype(df[col]) else "NUM_" + col.upper() for col in df.columns]

["NUM_" + col.upper()  if pd.api.types.is_numeric_dtype(df[col]) else col.upper() for col in df.columns]


# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak
#  car_crashes verisindeki isminde "no" barındırmayan
#   değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################
#
# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']


df.columns2 = [col.upper() if "no" in col else col.upper() + "_FLAG" for col in df.columns]
df.columns2







# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak
#  aşağıda verilen değişken isimlerinden FARKLI
#   olan değişkenlerin isimlerini seçiniz ve
#   yeni bir dataframe oluşturunuz.
# ###############################################

og_list = ["abbrev", "no_previous"]

############[eklenecek_değer for döngü if filtre]
new_cols = [col for col in df.columns if col not in og_list ]
new_df = df[new_cols]
new_df.head()


# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension
#  kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek
#  yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#







