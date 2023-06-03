from bs4 import BeautifulSoup as bs
import requests
from tabulate import tabulate
import time

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

URL = 'https://bigpara.hurriyet.com.tr/doviz/'


content = requests.get(URL, headers = header)

sayfa = bs(content.text, "html.parser")

fiyatlar = sayfa.find_all("li", class_ = "cell015")

isimler_liste = ["Dolar","Euro","Sterlin","İsviçre Frankı","Japon Yeni","Suudi Arabistan Riyali",
                    "Norveç Kronu","Danimarka Kronu","Avustralya Doları","Kanada Doları","İsveç Kronu",
                    "Ruble"
                ] 

fiyatlar_liste = []
alis = []
satis = []
degisim = []

le = int(len(fiyatlar)/2)
for i in range(3,le):
    fiyatlar[i] = (fiyatlar[i].text).strip("\n").strip()
    if i%3 == 0:
        alis.append(fiyatlar[i])
    elif i%3 == 1:
        satis.append(fiyatlar[i])
    elif i%3 == 2:
        degisim.append(fiyatlar[i])

headerss = ["Kur Adı","Alış Fiyatı","Satış Fiyatı","Değişim Miktarı"]

table = zip(isimler_liste,alis,satis,degisim)
t = time.localtime()
cur_time = time.strftime("%H:%M:%S",t)
print("Saat " f"{cur_time}" " itibariyle döviz kurları")
print(tabulate(table,headers=headerss,floatfmt=".4f",tablefmt="fancy_grid"))




