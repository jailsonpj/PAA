
def prod_max(vet,k):
    f = [0 for i in range(0,len(vet)+k)]
    f[0] = vet[0]
    #print(f)
    for i in range(1,len(vet)):
        #print(f[i-k])
        f[i] = max(vet[i] + f[i-k],f[i-1])

    #print(f)
    return f[len(vet)-1]

def processa():
    #lote = [0]
    lote = []
    n = int(input())
    entrada = input().split(" ")
    #lote = [0]
    for i in range(0,n):
        lote.append(int(entrada[i]))

    k = int(input())

    print(prod_max(lote,k))


processa()
