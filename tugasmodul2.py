
DAFTAR = "DAFTAR JUDUL FILM"
a = "antara aku dan kamu"
b = "penantian tanpa ujung"
c = "ngeri ngeri sedap" 
d = "keluarga cemara"
e = "beri aku waktu"

J1 = a
J2 = b
J3 = c 
J4 = d 
J5 = e 

kode_film = (f" (J1){a}    = RP 45000\n (J2){b}  = RP 48000\n (J3){c}      = RP 47000\n (J4){d}        = RP 50000\n (J5){e}         = RP 55000")
print(DAFTAR)
print(kode_film)
nama =str (input("masukkan nama pelanggan = "))
kode_film =str(input("masukkan kode film yang ingin dibeli (J1-J5) = "))
jumlah_tiket =int(input("masukkan jumlah tiket = "))
judul = input("Masukkan judul film = ")

if judul == "antara aku dan dia" :
   harga_satuan = 45000
   print(f'harga ={harga_satuan}')
elif judul == "penantian tanpa ujung" :
   harga_satuan = 48000
   print(f'harga ={harga_satuan}')
elif judul == "ngeri ngeri sedap" :
   harga_satuan = 47000
   print(f'harga ={harga_satuan}')
elif judul == "keluarga cemara" :
   harga_satuan = 47000
   print(f'harga ={harga_satuan}')
elif judul == "beri aku waktu":
   harga_satuan = 47000
   print(f'harga ={harga_satuan} ')
else :
   print('tiket tidak tersedia')
   

harga_total = harga_satuan*jumlah_tiket

print("Harga total= ", harga_total)

if harga_total>100000 :
   diskon = harga_total*15/100
   print(f'potongan harga = {diskon}')
   total_bayar = harga_total-diskon
   print(f'total bayar = {total_bayar}')

elif harga_total>350000 :
   diskon = harga_total*35/100
   print(f'potongan harga = {diskon}')
   total_bayar = harga_total-diskon
   print(f'total bayar = {total_bayar}')
else :
   print(f'total bayar = {harga_total}')

struk = "Struk Pemesanan"
print(struk)
print(f'  Nama Pembeli :{nama}\n  Judul Film :{judul}\n  Jumlah Tiket :{jumlah_tiket}\n')
print(f'   Harga Satuan :{harga_satuan}\n   Potongan Harga :{diskon}\n   Total Harga :{total_bayar}  ')




 
   