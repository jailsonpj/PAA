
def diagonal(l):
	saida = [l1**2 + l2**2 + l3**2 for l1,l2,l3 in l]
	return saida

def diametro(r):
	saida = [4*i**2 for i in r]
	return saida


def total(v,r):
	total = 0
	i,j=0,0
	while i<len(v) and j<len(v):
		if v[i]<=r[j]:
			#print(v[i])
			i+=1
			j+=1
			total+=1
		else:
			j+=1
	return total


#processa entradas
def processa():
	n = int(input())
	p = []

	#entrada paralelepipedo
	for x in range(0,n):
		lado = tuple([int(x) for x in input().split(' ')])
		p.append(lado)

	vol_p = diagonal(p)

	#entrada raio
	e = [int(input()) for x in range(0,n)]
	raio = diametro(e)

	#Ordenação
	vol_p = sorted(vol_p)
	raio = sorted(raio)


	print(total(vol_p,raio))


processa()
