#program untuk membuat suatu password yang valid
#jika password yang diunput valid maka akan muncul password valid
#jika tidak maka akan muncul password tidak valid
#panjang password minimal 8 karalter
#password harus terdiri dari minimal 1 huruf kecil,1 huruf kapital,dan 1 karakter khusus

print("          VALIDASI PASWORD ANDA          ")

while True : 
    password = input("masukkan password yang anda inginkan: ")

    panjang = False
    kecil = False
    besar = False
    angka = False
    khusus = False
    emoji = "!@$%^&*()_+=-\[]{}<>/?'"

    if len(password)>= 8:
        panjang = True
    else:
        print("karakter minimal 8!")

    for karakter in password :
        if"a"<= karakter <="z":
         kecil= True
        elif "A"<=karakter<="Z":
         besar = True
        elif"1"<=karakter<="9":
         angka = True
        elif karakter in emoji:
         khusus = True

    if panjang and kecil and besar and angka and besar :
       print("password valid dan kuat")
       print("sistem ditutup!")
       break
    else:
       if not kecil:
          print("minimal menggunakan  1 huruf kecil")
       if not besar:
          print("minimalmenggunkan 1 huruf besar ")
       if not angka:
          print("minimal menggunakan 1 angka ")
       if  not khusus:
          print("minimal menggunakan 1 karakter khusus")
       print("silahkan coba lagi!")