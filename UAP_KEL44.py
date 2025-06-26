import random
import time
import threading
import os
import datetime
import sys
from termcolor import colored

def bersihkan_layar():
    """Membersihkan layar konsol untuk tampilan yang rapi."""
    os.system('cls')

def soal_mudah():
    """Membuat 5 soal matematika level Mudah (penjumlahan & pengurangan)."""
    daftar_soal = []
    for i in range(5):
        angka1 = random.randint(10, 30)
        angka2 = random.randint(10, 30)
        operator = random.choice(['a','b'])
        if operator == 'a':
            teks_soal = f"Berapakah {angka1} + {angka2}? "
            jawaban_benar = angka1 + angka2
        else:
            teks_soal = f"Berapakah {max(angka1, angka2)} - {min(angka1, angka2)}? "
            jawaban_benar = max(angka1, angka2) - min(angka1, angka2)
        daftar_soal.append((teks_soal, jawaban_benar))
    return daftar_soal

def soal_sedang():
    """Membuat 5 soal matematika level Sedang (penjumlahan, pengurangan, perkalian)."""
    daftar_soal = []
    for i in range(5):
        angka1 = random.randint(30, 100)
        angka2 = random.randint(10, 50)
        angka3 = random.randint(2, 15)
        operator = random.choice(['a','b','c'])
        if operator == 'a':
            teks_soal = f"Berapakah {angka1} + {angka2}? "
            jawaban_benar = angka1 + angka2
        elif operator == 'b':
            teks_soal = f"Berapakah {angka1} - {angka2}? "
            jawaban_benar = angka1 - angka2
        else:
            teks_soal = f"Berapakah {angka2} * {angka3}? "
            jawaban_benar = angka2 * angka3
        daftar_soal.append((teks_soal, jawaban_benar))
    return daftar_soal

def soal_sulit():
    """Membuat 5 soal matematika level Sulit (operasi campuran, pembagian bulat)."""
    daftar_soal = []
    for i in range(5):
        angka1 = random.randint(20, 100)
        angka2 = random.randint(5, 20)
        angka3 = random.randint(3, 10)
        operator = random.choice(['+', '-', '*', '/'])
        if operator == '+':
            teks_soal = f"Berapakah {angka1} + {angka2} * {angka3}? "
            jawaban_benar = angka1 + angka2 * angka3
        elif operator == '-':
            angka4 = random.randint(5, 15) * angka2
            teks_soal = f"Berapakah {angka4} // {angka2} - {angka3}? (pembagian bilangan bulat) "
            jawaban_benar = angka1 // angka2 - angka3
        elif operator == '*':
            teks_soal = f"Berapakah {angka2} * {angka3} + {angka1}? "
            jawaban_benar = angka2 * angka3 + angka1
        else: # Pembagian bulat
            angka4 = random.randint(5, 15) * angka2
            teks_soal = f"Berapakah {angka1} + {angka4} // {angka2}? (Pembagian bilangan bulat) "
            jawaban_benar = angka1 + angka4 // angka2
        daftar_soal.append((teks_soal, jawaban_benar))
    return daftar_soal

def input_jawaban():
    """Fungsi pembantu untuk mengambil input secara blocking.
    Mengatur JAWABAN_PEMAIN menjadi angka (jika valid), "EMPTY_ENTER_FLAG" (jika kosong),
    atau None (jika tidak valid dan bukan kosong).
    """
    global JAWABAN_PEMAIN
    try:
        raw_input_str = input("Jawaban : ") # Ambil input sebagai string terlebih dahulu
        if raw_input_str == "":
            JAWABAN_PEMAIN = "jawaban kosong" # Gunakan flag khusus untuk input kosong
        else:
            JAWABAN_PEMAIN = int(raw_input_str) # Coba konversi ke integer
    except ValueError:
        # Ini akan menangkap input non-numerik (misal "abc")
        JAWABAN_PEMAIN = None # Menandakan input tidak valid (bukan kosong atau angka)
    except Exception:
        JAWABAN_PEMAIN = None # Tangani error lain yang tidak terduga

def batas_waktu_input(batas_waktu):
    """Mengambil input dari pemain dengan batas waktu, tanpa menampilkan hitungan mundur."""
    global JAWABAN_PEMAIN 
    JAWABAN_PEMAIN = None # Reset jawaban pemain
    
    thread_input = threading.Thread(target=input_jawaban)
    thread_input.start()
    thread_input.join(timeout=batas_waktu) # Memblokir thread utama hingga input diterima atau waktu habis
    thread_input.is_alive()

def mulai_sesi_kuis():
    """Menjalankan satu sesi kuis lengkap untuk seorang pemain."""
    global SKOR_SAAT_INI, INFO_LEVEL, JAWABAN_PEMAIN
    bersihkan_layar()
    nama_pemain = input("Masukkan nama Anda: ")
    bersihkan_layar()
    print(colored("\n🎯 Pilih tingkat kesulitan:","blue"))
    nama_level_list = list(INFO_LEVEL.keys())
    for i, nama_level in enumerate(nama_level_list):
        print(f"{i+1}. {nama_level}")

    while True:
        try: # Menambahkan try-except untuk penanganan input pilihan level
            pilihan_angka = int(input("Masukkan nomor pilihan Anda: "))
            
            if 1 <= pilihan_angka <= len(nama_level_list):
                nama_level_terpilih = nama_level_list[pilihan_angka - 1]
                break
            else:
                print(colored("❌ Pilihan tidak valid. Silakan coba lagi.","red"))
        except ValueError:
            print(colored("Input tidak valid. Masukkan angka.","red"))


    fungsi_pembuat_soal, batas_waktu = INFO_LEVEL[nama_level_terpilih]
    bersihkan_layar()
    print(f"\nAnda memilih level: {colored(nama_level_terpilih, 'cyan')} 👍 (Batas waktu: {batas_waktu} detik per soal)")
    input("Tekan Enter jika anda siap... ")
    daftar_soal = fungsi_pembuat_soal()
    bersihkan_layar()

    SKOR_SAAT_INI = 0
    for i, (teks_soal, jawaban_benar) in enumerate(daftar_soal):
        print(f"\nSoal ke-{i+1}:")
        print(teks_soal) # Menggunakan end='' agar input ada di baris yang sama

        batas_waktu_input(batas_waktu)

        if JAWABAN_PEMAIN is not None and JAWABAN_PEMAIN == jawaban_benar:
            print(colored("Benar! ✅ Jawaban Anda tepat!", "green"))
            SKOR_SAAT_INI += 1
        elif JAWABAN_PEMAIN == "jawaban kosong": # Kasus baru: pemain mengosongkan jawaban
            print(colored("Anda mengosongkan jawaban. 🤷", "red"))
            print(colored(f"Jawaban yang benar adalah {jawaban_benar}.", "yellow"))
        elif JAWABAN_PEMAIN is not None: # Berarti JAWABAN_PEMAIN adalah angka, tapi salah
            print(colored("Salah! ❌", "red"), end='')
            print(colored(f" Jawaban yang benar adalah {jawaban_benar}.", "yellow"))
        else: # JAWABAN_PEMAIN adalah None (waktu habis atau input non-numerik)
            print(colored("\nWaktu habis atau input tidak valid! ⏰", "red")) # Pesan gabungan
            print(colored(f"Jawaban yang benar adalah {jawaban_benar}.", "yellow"))
        time.sleep(2) # Memberi waktu untuk melihat feedback
        bersihkan_layar() # Membersihkan layar setelah setiap soal

    print(colored("\n🎉 -------------- Kuis Selesai -------------- 🎉","blue"))
    print(f"Skor akhir Anda: {colored(SKOR_SAAT_INI, 'magenta')} dari {len(daftar_soal)} soal.")
    simpan_skor(nama_pemain, nama_level_terpilih, SKOR_SAAT_INI)
    input("Tekan Enter untuk kembali ke menu... ")

def simpan_skor(nama_pemain, level, skor):
    """Menyimpan skor pemain ke dalam file riwayat_skor_kuis.txt."""
    global NAMA_FILE_SKOR
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(NAMA_FILE_SKOR, "a") as f:
        f.write(f"[{timestamp}] Nama: {nama_pemain}, Level: {level}, Skor: {skor}\n")
    print(colored(f"Skor Anda telah disimpan ke {NAMA_FILE_SKOR} 💾", "cyan"))

def tampilkan_riwayat_skor():
    """Menampilkan semua skor yang telah tersimpan."""
    global NAMA_FILE_SKOR
    bersihkan_layar()
    if not os.path.exists(NAMA_FILE_SKOR):
        print(colored("\nBelum ada skor yang tersimpan. Ayo main dulu! 💪", "yellow"))
        input("Tekan Enter untuk kembali ke menu... ")
        return
        
    print(colored("\n📜 --------------------- Riwayat Skor --------------------- 📜","blue"))
    with open(NAMA_FILE_SKOR, "r") as f:
        daftar_skor = f.readlines()
        if not daftar_skor:
            print(colored("Belum ada skor yang tersimpan.","red"))
        for baris_skor in daftar_skor:
            print(baris_skor.strip())
    print(colored("-----------------------------------------------------------","blue"))
    input("Tekan Enter untuk kembali ke menu... ")

def reset_semua_skor():
    """Mengatur ulang (menghapus) semua skor yang tersimpan."""
    global NAMA_FILE_SKOR
    bersihkan_layar()
    if os.path.exists(NAMA_FILE_SKOR):
        konfirmasi = input(colored("Apakah Anda yakin ingin mereset semua skor? (ya/tidak): ", "red")).lower()
        bersihkan_layar()
        if konfirmasi == 'ya':
            os.remove(NAMA_FILE_SKOR)
            print(colored("Semua skor telah direset. Siap untuk rekor baru! ✨", "green"))
        else:
            print(colored("Reset skor dibatalkan. 👍", "yellow"))
    else:
        print(colored("Tidak ada skor untuk direset. File belum ada. 🤷", "yellow"))
    input("Tekan Enter untuk kembali ke menu... ")

def tampilkan_menu_utama():
    """Menampilkan opsi menu utama kepada pemain."""
    
    print(colored("\n---------- Menu Utama Kuis Hitung Cepat ----------","blue"))
    print("1️⃣   Mulai Kuis 🚀         ")
    print("2️⃣   Tampilkan Riwayat Skor 📜")
    print("3️⃣   Reset Skor 🔄         ")
    print("4️⃣   Keluar 🚪           ")
    print(colored("--------------------------------------------------","blue"))

def jalankan_aplikasi_kuis():
    """Metode utama untuk menjalankan aplikasi kuis."""
    bersihkan_layar()
    print(colored("🧠 Selamat datang di Kuis Menghitung Cepat! 🧠", "yellow", attrs=['bold']))
    while True:
        tampilkan_menu_utama()
        pilihan_menu = input("Pilih opsi (1-4): ")
        if pilihan_menu == '1':
            mulai_sesi_kuis()
            bersihkan_layar()
        elif pilihan_menu == '2':
            tampilkan_riwayat_skor()
            bersihkan_layar()
        elif pilihan_menu == '3':
            reset_semua_skor()
            bersihkan_layar()
        elif pilihan_menu == '4':
            bersihkan_layar()
            print(colored("Terima kasih telah bermain! Sampai jumpa lagi! 👋😊", "green", attrs=['bold']))
            break
        else:
            print(colored("Pilihan tidak valid. Silakan coba lagi. 🤷‍♂️", "red"))
            input("Tekan Enter untuk melanjutkan... ")
            bersihkan_layar()

# --- Variabel Global ---
INFO_LEVEL = {
    "Mudah": (soal_mudah, 5),
    "Sedang": (soal_sedang, 10),
    "Sulit": (soal_sulit, 15),
}
SKOR_SAAT_INI = 0
NAMA_FILE_SKOR = "riwayat_skor_kuis.txt"
JAWABAN_PEMAIN = None # Nilai awal, akan disetel oleh _input_blocking
# -----------------------------------------------------------

# Panggil fungsi utama secara langsung
jalankan_aplikasi_kuis()