import pandas as pd

"""
--> pandas: Etiketli verilerle çalışmayı kolaylaştıran bir Python kütüphanesidir.
--> En temel veri yapısı olan DataFrame, satır-sütunlardan oluşur ve her satırın bir 'index'i (indeks) vardır.
--> Bu indeksler, verileri kolayca aramaya, sıralamaya ve güncellemeye olanak tanır.
--> NumPy yalnızca sayısal diziler (array) ile çalışırken, pandas hem sayısal hem metinsel verilerle
satır-sütun yapısında, etiketli olarak işlem yapmayı sağlar. Ayrıca eksik veri (NaN) gibi durumlarla da daha iyi başa çıkar.
"""


"""
pandas.Series: Tek boyutlu (1D), etiketli veri yapısıdır.
NumPy array'lerine benzer ama her elemanın bir index (etiket) ile tanımlandığı bir yapıdır.
Her elemanın bir veri tipi (int, float, str vb.) olabilir ve genellikle aynı tiptedir.
Series yapısı sayesinde verilere hem konum (örnek: s[0]) hem de etiket (örnek: s["ad"]) ile erişilebilir.
Boyutu, içerdiği eleman sayısı kadardır ve eksik değerler (NaN) desteklenir.

"""

s = pd.Series([10, 77, 12, 4, 5])

type(s)
s.dtype
s.size
s.ndim
s.values

"""
- type(s): Bu komut, s değişkeninin bir pandas Series (pandas.core.series.Series) 
nesnesi olduğunu gösterir.
- Series, etiketli tek boyutlu veri yapısıdır ve pandas'a özgüdür.
- type(s.values): Bu komut, Series içindeki ham verilerin bir NumPy 
ndarray (numpy.ndarray) olduğunu gösterir.
- Yani s.values, yalnızca verileri içerir ve etiket bilgisi (index) bu yapıda bulunmaz.

"""
type(s)        # pandas.core.series.Series
type(s.values) # numpy.ndarray

s.head()
s.head(3)
s.tail()
s.tail(3)

df = pd.read_csv("datasets/advertising.csv")
df.head()

#############################################
# Veriye Hızlı Bakış (Quick Look at Data)
#############################################
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.tail()
df.shape
df.info()
df.columns
df.index
df.describe().T
df.isnull().values.any()
df.isnull().sum()
df["sex"].head()
df["sex"].value_counts()

###################################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas) #
###################################################
import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
df.head()
df.index
df[0:13]
df.drop(0,axis=0).head()
delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes,axis=0).head(10)

# df = df.drop(delete_indexes, axis=0)
# df.drop(delete_indexes, axis=0, inplace=True)

#######################
# Değişkeni Indexe Çevirmek
#######################

df["age"].head()
df.age.head()

df.index = df["age"]

df.drop("age", axis=1).head()

df.drop("age", axis=1, inplace=True)
df.head()


# Indexi Değişkene Çevirmek
#######################

df.index

df["age"] = df.index

df.head()
df.drop("age", axis=1, inplace=True)

df.reset_index().head()
df = df.reset_index()
df.head()

#######################
# Değişkenler Üzerinde İşlemler
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

"age" in df

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head())


df[["age"]].head()
type(df[["age"]].head())

df[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df[col_names]

df["age2"] = df["age"]**2
df["age3"] = df["age"] / df["age2"]

df.drop("age3", axis=1).head()

df.drop(col_names, axis=1).head()

df.loc[:, ~df.columns.str.contains("age")].head()

#######################
# iloc & loc
#######################
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None )
df = sns.load_dataset("titanic")
df.head()


# iloc satır ve sütunlara indeks numaralarıyla erişmeyi sağlar.
df.iloc[0:3]
df.iloc[0,0]

##############################
# loc: label based selection #
##############################
# loc satır ve sütunlara etiketleriyle (isimleriyle) ulaşmanı sağlar.

"""
df.iloc[0:3, 0:3] indeks numaralarına göre ilk 3 satır ve 
ilk 3 sütunu seçerken, df.loc[0:3, "age"] indeks etiketi 0'dan 
3'e kadar olan satırların "age" adlı sütununu seçer.
"""
df.iloc[0:3, 0:3]
df.loc[0:3, "age"]

col_names = ["age", "embarked", "alive", "alone"]
df.loc[0:3, col_names]

#######################
# Koşullu Seçim (Conditional Selection)
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
# "age" sütunundaki 50 yaşından
# büyük olan kişilerin yaşlarının toplamını verir.
df[df["age"] > 50]["age"].sum()

#tüm sütunlar için ayrı ayrı kaç geçerli (NaN olmayan) değer olduğunu verir.
df[df["age"] > 50].count()

# 50 yaşından büyük kaç kişi olduğunu sayar (satır sayısı).
df[df["age"] > 50]["age"].count()


df.loc[df["age"] > 50, ["age", "class"]].head()

#birden fazla koşul olduğu için parantez kullanmak gerekir.
df[(df["age"] > 50) & (df["sex"] == "male")]["age"].count()

#loc, hem satır hem sütun filtresi yapabilmeyi sağlar.
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()

df["embark_town"].value_counts()

"""
Bu kod, 50 yaşından büyük erkek yolcular arasında Cherbourg veya Southampton 
limanlarından binenlerin hangi yolcu sınıfında (First, Second...) olduklarını sayar.
"""
df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

df_new["class"].value_counts()

"""
1. sınıfta yolculuk eden ve hayatta olmayan kadınları seçiyor
ve onların hangi sınıfta (class) olduklarının dağılımını gösteriyor."""
df_new2 = df.loc[(df["sex"] == "female")
                 & (df["alive"] == "no")
                 & (df["pclass"] == 1), ["age", "class"]]

df_new2["class"].value_counts()

#####################################################
# Toplulaştırma ve Gruplama (Aggregation & Grouping)#
#####################################################

# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean()

df.groupby("sex")["age"].mean()

df.groupby("sex").agg({"age": "mean"})
df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})


df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                       "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                       "survived": "mean"})


df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})



#######################
# Pivot table
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex", "embarked")
df.pivot_table("survived", "sex", "embarked", aggfunc="std")

df.pivot_table("survived", "sex", ["embarked", "class"])
df.pivot_table("survived", "sex", ["embarked", "class"], aggfunc="std")

df.pivot_table("survived", "sex", ["embarked", "class"])

df.head()

# Verileri eşit genişlikte aralıklara böler.
# Her grubun aralığı eşit, ama içindeki kişi sayısı farklı olabilir.
df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 30, 40, 50, 60, 70, 80, 90])

# Sayısal veriyi kategorik hale getirmek istediğinde.
# qcut() = Her grupta yaklaşık aynı kişi sayısı olur, ama aralık genişlikleri farklı olabilir.
# Verileri eşit sayıda gözleme sahip olacak şekilde böler.
df["new_age"] = pd.qcut(df["age"], q=7)

df.pivot_table("survived", "sex", "new_age")
df.pivot_table("survived", "sex", ["new_age", "class"])

pd.set_option('display.width', 500)
df.head()

#############################################
# Apply ve Lambda
#############################################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5
df.head()
(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()

df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

#df.loc[:, ["age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.head()

#############################################
# Birleştirme (Join) İşlemleri
#############################################
import numpy as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index=True)

#######################
# Merge ile Birleştirme İşlemleri
#######################

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
pd.merge(df1, df2, on="employees")

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)