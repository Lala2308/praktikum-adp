M = float(input("masukkan modal awal : "))
r = float(input("masukkan suku bunga tahunan (%): "))
T = float(input("masukkan target investasi : "))

x = 0
M = M

while M < T :  
    x += 1
    M += M*r/100
    print(f"Tahun ke-{x} : Rp{M:}")

print(f"Target tercapai dalam : {x} tahun")