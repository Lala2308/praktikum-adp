huruf = ['A','A-','B+','B','B-','C+','C','D','E']
angka = [4.00,3.75,3.50,3.00,2.75,2.50,2.00,1.00,0.00]
a = int(input('jumlah mahasiswa : '))
b = int(input('jumlah mata kuliah : '))

data = []
for i in range (a):
    print(f'\nMahasiswa ke-{i+1} : ')
    nama = input('Nama : ')
    nilai =[]
    total = 0
    for j in range (b):
        n = input(f'Nilai: ').upper()
        nilai.append(n)
        total+= angka[huruf.index(n)]
    ip = total/b
    data.append([nama,nilai,ip])
for i in range(len(data)):
    for j in range (i+1,len(data)):
        if data[i][2]<data[j][2]:
           m=data[i]
           data[i]=data[j]
           data[j]=m
print('\nTABEL IP MAHASISWA')
print('---'*20)
print(f'{'NAMA':<20}{'NILAI':<30}{'IP':>5}')
print('---'*20)
for x in data :
    nama = x[0]
    n_str=','.join(x[1])
    IP = x[2]
    print(f'{nama:<20}{n_str:<30}{IP:5}')
print('---'*20)