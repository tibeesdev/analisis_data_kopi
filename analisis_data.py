import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import chi2_contingency

list_data = []
file =  "hasil_form.csv"

# buka filenya dan masukkan ke dalam list data
with open(file, "r") as f:
    for i in f:
        list_data.append(i.split(","))

# list data row
header =  list_data[0]
timestamp = []
email = []
nama = []
fakultas = []
usia = []
jenis_kopi = []
frekuensi_konsumsi = []
riwayat_penyakit = []
waktu_tidur = []
penyakit = []

main_data = [fakultas, usia, jenis_kopi, frekuensi_konsumsi, riwayat_penyakit, waktu_tidur, penyakit]

# proses data buat dapatin row
def proses_data():
    # masukkan data ke dalam list masing masing
    for i in range(len(list_data)):
        timestamp.append(list_data[i][0])
        email.append(list_data[i][1])
        nama.append(list_data[i][2])
        fakultas.append(list_data[i][3])
        usia.append(list_data[i][4])
        jenis_kopi.append(list_data[i][5])
        frekuensi_konsumsi.append(list_data[i][6])
        riwayat_penyakit.append(list_data[i][7])
        waktu_tidur.append(list_data[i][8])
        penyakit.append(list_data[i][9])

# ngitung berapa banyak responden memilih suatu pilihan
#returnnya (list pilihan dan list jumlah responden yang memilih suatu pilihan)
def count(list_data):
    data_type =[] # tipe data yang ada dalam sebuah list(contohnya dari fakultas apa aja)
    header = list_data[0]# header buat judul
    data_map = {}
    for i in range(1, len(list_data)): # buat ngambil jenis datanya (biar kalo ada banyak fakultas di list maka gak perlu dimasukkan)
        if i not in data_type:
            data_type.append(list_data[i])

    for x in data_type: # buat ngitung jumlah tiap datanya (ngitung berapa orang di tiap fakultas)
        data_map[x] = list_data.count(x)

    # mengurutkan data map biar value paling tinggi berada lebih dulu
    data_sorted = sorted(data_map.items(), key=lambda item: item[1]) # bentuk datanya jadi list array

    header_sorted = []
    value_sorted = []
    for item in data_sorted:
        header_sorted.append(item[0]) # masukkan header
        value_sorted.append(item[1])# masukkan valuenya

    print (data_sorted)

    return (header_sorted, value_sorted, header)
    
def horizontal_bar(data):
    nama, value, title = data
    xlable = "Jumlah Responden"
    ylable = ''
    # list warna buat balok
    warna = [
        '#9BBE3B',  
        '#7EB443',  
        '#5AAE5C',  
        '#3B9C7C',  
        '#307D87',  
        '#356E8A',  
        '#435E83',  
        '#4F4D7D',  
        '#4A356A'   
]
    plt.title(title) # nampilin judul di atas
    plt.xlabel(xlable) #nampilin label x (di bawah)
    plt.ylabel(ylable) #nampilin label y (di samping)
    plt.grid(axis='x', zorder=1) # nampilin garis
    plt.barh(nama, value, color=warna,  zorder=2) # bikin bar horizontal

    for x, y in zip(nama, value): # nampilin angka di ujung bar
        plt.text(y + 0.5, x, str(y), verticalalignment = 'center', zorder = 2)

    plt.yticks(fontsize=8)
    plt.tight_layout()
    
    plt.savefig(f"{title}.png")
    plt.clf()

def pie_chart(data):
    nama, value, title = data
    xlable = "Jumlah Responden"
    ylable = ''
    # list warna buat balok
    warna = [
        '#9BBE3B',  
        '#7EB443',  
        '#5AAE5C',  
        '#3B9C7C',  
        '#307D87',  
        '#356E8A',  
        '#435E83',  
        '#4F4D7D',  
        '#4A356A'   
        ]
    plt.title(title) # nampilin judul di atas
    plt.xlabel(xlable) #nampilin label x (di bawah)
    plt.ylabel(ylable) #nampilin label y (di samping)
    plt.pie(value, labels=nama, autopct='%1.1f%%')
    plt.savefig(f"{title} pie.png")
    plt.clf()

# visualisasi data
proses_data()
for item in main_data[:-1]: # iterasi buat bikin plot untuk setiap listnya
    data = count(item)
    horizontal_bar(data)
    pie_chart(data)
