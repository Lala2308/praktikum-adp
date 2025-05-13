
x = []
f = []
g = []
h = []
print ('\nOutput 1 :')
print('\tf(x) = 4x^3 + 7x - 5, x > 0 \n\t     = 3x^2 - 5x + 1 ,x < 0 \n\tg(x) = (f(x)) ^ 2 - f(x) \n\th(x) = f(x) * g(x)')
n = int(input('banyak data (n) = '))
while True :
    for i in range(n) :
        y = int(input(f'input x ke-{i+1} : '))
        x.append(y)
        
        if y >= 0 :
            fx= 4*y**3+7*y-5 
        else :
            fx = 3*y**2-5*y+1
    
        gx = fx**2-fx
        
        hx = fx*gx

        f.append(fx)
        g.append(gx)
        h.append(hx)
    print(f'Nilai x = {x}')
    print(f'Nilai f(x) = {f}')
    print(f'Nilai g(x) = {g}')
    print(f'Nilai h(x) = {h}')

    print('\nOutput 2 : ')
    print('No |\tx\t|\tf(x)\t|\tg(x)\t|\th(x)\t\t|')
    print('----'*18)
    for i in range (n):
        print(f'{i+1}  |\t{x[i]}\t|\t{f[i]}\t|\t{g[i]}\t|\t{h[i]:<10}\t|')
    ulang= input('\n input nilai x lagi Y/N?').strip().upper()
    if ulang!= 'Y':
        break