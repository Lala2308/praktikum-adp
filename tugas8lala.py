# Fungsi untuk menghitung jumlah pengalaman dari string
def hitung_jumlah_pengalaman(pengalaman_str):
    jumlah = 1 if len(pengalaman_str) > 0 else 0
    for c in pengalaman_str:
        if c == ';':
            jumlah += 1
    return jumlah

# Fungsi untuk mengecek apakah bidang ada dalam pengalaman
def bidang_ada_dalam_pengalaman(bidang, pengalaman_str):
    kata = ''
    for c in pengalaman_str + ';':  # tambahan ';' agar kata terakhir ikut dicek
        if c == ';':
            if kata.lower() == bidang.lower():
                return True
            kata = ''
        else:
            kata += c
    return False

# Fungsi untuk menghitung nilai total
def hitung_nilai(wawancara, pengalaman_str, bidang, ketua):
    nilai = hitung_jumlah_pengalaman(pengalaman_str)
    if ketua:
        nilai += 2
    if bidang_ada_dalam_pengalaman(bidang, pengalaman_str):
        nilai += 3
    return wawancara + nilai

# Fungsi seleksi dan pengelompokan koordinator berdasarkan bidang
def seleksi_koordinator(data):
    bidang_dict = {
        'Acara': [],
        'Pubdok': [],
        'Perlengkapan': [],
        'Danus': []
    }

    for cakoor in data:
        nama = cakoor[0]
        nim = cakoor[1]
        kelas = cakoor[2]
        pengalaman = cakoor[3]
        wawancara = cakoor[4]
        bidang = cakoor[5]
        ketua = cakoor[6]

        nilai = hitung_nilai(wawancara, pengalaman, bidang, ketua)

        bidang_dict[bidang].append({
            'nama': nama,
            'nim': nim,
            'kelas': kelas,
            'nilai': nilai,
            'wawancara': wawancara,
            'pengalaman': pengalaman,
            'ketua': ketua
        })

    # Urutkan berdasarkan nilai tertinggi
    for bidang in bidang_dict:
        daftar = bidang_dict[bidang]
        for i in range(len(daftar)):
            for j in range(i + 1, len(daftar)):
                if daftar[j]['nilai'] > daftar[i]['nilai']:
                    daftar[i], daftar[j] = daftar[j], daftar[i]

    return bidang_dict

# Menampilkan semua data cakoor
def tampilkan_data(data):
    print("======= SEMUA DATA CAKOOR =======")
    for d in data:
        print(f"\nNama      : {d[0]}")
        print(f"NIM       : {d[1]}")
        print(f"Kelas     : {d[2]}")
        print(f"Pengalaman: {d[3]}")
        print(f"Wawancara : {d[4]}")
        print(f"Bidang    : {d[5]}")
        print(f"Ketua     : {'Ya' if d[6] else 'Tidak'}")

# Menampilkan hasil seleksi
def tampilkan_hasil(hasil):
    print("\n======= KOORDINATOR TERPILIH =======")
    for bidang in hasil:
        print(f"\nBidang: {bidang}")
        top2 = hasil[bidang][:2]
        for i in range(len(top2)):
            cakoor = top2[i]
            print(f"{i+1}. {cakoor['nama']} (NIM: {cakoor['nim']}, Kelas: {cakoor['kelas']}) - Nilai: {cakoor['nilai']}")

# Simpan hasil ke file teks
def simpan_ke_file(hasil, nama_file):
    f = open(nama_file, 'w')
    f.write("======= HASIL SELEKSI KOORDINATOR =======\n")
    for bidang in hasil:
        f.write(f"\nBidang: {bidang}\n")
        top2 = hasil[bidang][:2]
        for i in range(len(top2)):
            c = top2[i]
            f.write(f"{i+1}. {c['nama']} | NIM: {c['nim']} | Kelas: {c['kelas']} | Nilai: {c['nilai']}\n")
    f.close()
    print(f"\nHasil telah disimpan di file: {nama_file}")

# Main program
def main():
    # Array 2D data cakoor
    data = [
        ["Lala Abdillah Batubara", "2410431031", "A", "Acara;perlengkapan", 85, "Acara", True],
        ["Anggya Fadhilla", "2410431028", "B", "Acara;Danus", 90, "Danus", True],
        ["Bima Niskala Lisyanda", "2410433015", "C", "Acara;Pubdok", 83, "Acara", True],
        ["Dinda Rahma Mulyana", "2410431034", "B", "Pubdok", 88, "Pubdok", True],
        ["Shusan Berliana Putri", "2410431025", "C", "Perlengkapan;Danus", 85, "Perlengkapan", True],
        ["Nur Azizah", "2410432011", "A", "Acara;Pubdok;Danus", 80, "Pubdok", False],
        ["Raditya Irawan", "2410432003", "A", "Acara;Perlengkapan", 75, "Perlengkapan", False],
        ["Aysi Fitria Ramadhani","2410431013","A","Danus",80,"Danus",True],
        ["Wahyu Andani","2410432004","B","Pubdok;Danus",80,"Danus",False],
        ["Gibran Rmadhan","2410431032","B","Pubdok;Danus",84,"Pubdok",False],
        ["Naila Farizka Azzahra","2410431016","C","Pubdok;Acara",85,"Pubdok",True],
        ["Lexania Nazila","2410431019","A","Acara;Perlengkapan",80,"Acara",False],
        ["Azhari Fauzi","2410433008","B","Danus;Perlengkapan",78,"Perlengkapan",False],
        ["Zazkia Avris Yaumi","2410431039","A","Danus;Pubdok",79,"Danus",False],
        ["Yazid Riyanda Putra","2410431005","C","Acara",83,"Acara",False],
        ["Sari Ramadahani","2420431029","A","Perlengkapan;Acara",83,"Perlengkapan",True]
]

    tampilkan_data(data)
    hasil = seleksi_koordinator(data)
    tampilkan_hasil(hasil)
    simpan_ke_file(hasil, "hasil_koordinator.txt")

main()