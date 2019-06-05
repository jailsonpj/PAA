num_esferas = int(input())

pl = []
for i in range(num_esferas):
    lados = list([int(x) for x in input().split(' ')])
    l1 = max(lados)
    lados.remove(l1)
    l2 = max(lados)
    pl.append((l1, l2))
    
cont = 0
for l1, l2 in pl:
    raio = int(input())
    cont += (1 if l1**2 + l2**2 <= 4*raio**2 else 0)

print(cont)