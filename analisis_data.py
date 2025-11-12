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

#analisis data
var = []
p_value = []
def analisis_korelasi(variabel):    
    # supaya datanya full gak kepotong
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    #pd.set_option('display.width', 1000)

    # bikin tabel ringkasan antara 2 kolom
    tabel_ringkasan = pd.crosstab(variabel[1:], penyakit[1:])
    print("="*100)
    print("TABEL RINGKASAN")
    print("="*100)

    print(tabel_ringkasan)
    print("="*100)

    # hitung korelasinya (pake p_value)
    chi2, p_value, dof, expected = chi2_contingency(tabel_ringkasan)

    print (f"Nilai P-Value adalah : {p_value}")
    print("="*100)

    if p_value < 0.05:
        print(f"Ada hubungan antara variabel {variabel[0]} dengan {penyakit[0]}")
    else:
        print(f"Tidak Ada hubungan antara variabel {variabel[0]} dengan {penyakit[0]}")
    print("="*100)


    p_valueTable(tabel_ringkasan, variabel[0])


    return (variabel[0], p_value)

#visualisasi data
def p_valueTable(tabel_ringkasan, judul):

    
    tab = plt.table(
    cellText=tabel_ringkasan.values,      # -> Isi datanya
    colLabels=tabel_ringkasan.columns,    # -> Judul kolom
    rowLabels=tabel_ringkasan.index,      # -> Judul baris
    loc='center',                         # -> Posisikan di tengah
    cellLoc='center',                     # -> Teks di dalam sel di tengah
    )
    tab.scale(1.2, 1.2) # Skalakan ukuran sel


# Simpan sebagai gambar
    nama_file_gambar = f"tabel {judul}.png"
    plt.savefig(nama_file_gambar, dpi=200, bbox_inches='tight')
    plt.clf()

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
    data = analisis_korelasi(item)
    var.append(data[0])
    p_value.append(data[1])

dat = (var, p_value)
#visualisasiP_Value(dat)
print("RINGKASAN P_VALUE")
for t, p in zip(var, p_value):
    kesimpulan = "Ada Korelasi" if p <0.05 else "Tidak Ada Korelasi"
    print(f"{t} : {p} -> {kesimpulan}")