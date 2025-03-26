baris = int(input("masukkan jumlah baris : "))
kolom = int(input("masukkan jumlah kolom : "))
#loop untuk mencetak pola X dan O
for i in range (baris):
    for j in range (kolom):
        if (i+j)%2 == 0:
           print("X", end= " ")
        else:
           print("O", end=" ")
    print()