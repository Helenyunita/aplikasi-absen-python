import sqlite3
import datetime

# Fungsi untuk membuat tabel absensi jika belum ada
def create_table():
    conn = sqlite3.connect("absensi.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS absensi
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  nama TEXT,
                  tanggal DATE,
                  jam TIME)''')
    conn.commit()
    conn.close()

# Fungsi untuk menambahkan data absensi
def absen():
    nama = input("Masukkan nama Anda: ")
    waktu_absen = datetime.datetime.now()
    tanggal = waktu_absen.strftime("%Y-%m-%d")
    jam = waktu_absen.strftime("%H:%M:%S")
    
    conn = sqlite3.connect("absensi.db")
    c = conn.cursor()
    c.execute("INSERT INTO absensi (nama, tanggal, jam) VALUES (?, ?, ?)", (nama, tanggal, jam))
    conn.commit()
    conn.close()
    
    print("Absensi berhasil!")
    print("Nama:", nama)
    print("Tanggal:", tanggal)
    print("Jam:", jam)

# Fungsi untuk melihat semua data absensi
def lihat_absensi():
    conn = sqlite3.connect("absensi.db")
    c = conn.cursor()
    c.execute("SELECT * FROM absensi")
    rows = c.fetchall()
    
    print("Data Absensi:")
    for row in rows:
        print("ID:", row[0])
        print("Nama:", row[1])
        print("Tanggal:", row[2])
        print("Jam:", row[3])
        print("---------------")
    
    conn.close()

# Membuat tabel absensi (jika belum ada)
create_table()

# Menampilkan menu
while True:
    print("=== APLIKASI ABSENSI ===")
    print("1. Absen")
    print("2. Lihat Absensi")
    print("0. Keluar")
    choice = input("Pilih menu: ")

    if choice == "1":
        absen()
    elif choice == "2":
        lihat_absensi()
    elif choice == "0":
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
 