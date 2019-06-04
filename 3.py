import math

def quicksort(l):
	#print("entrou")
	if l:
		left = [x for x in l if x < l[0]]
		right = [x for x in l if x > l[0]]
		if len(left) > 1:
			left = quicksort(left)
		if len(right) > 1:
			right = quicksort(right)
		return left + [l[0]] * l.count(l[0]) + right

	return []



def volume_p(vet):
	p = []
	for i in range(0,len(vet)):
		exp = 1
		for j in range(0,3):
			exp = exp * vet[i][j]
		p.append(exp)
	return p

#calcula raio da esfera
def cubo_e(vet):
	e = [math.pow(vet[x],3) for x in range(0,len(vet))]
	return e

#calcula diagonal de um paralelepipedo
def diagonal_p(vet):
	p = []
	#print("entrou")
	for i in range(0,len(vet)):
		exp = 0
		for j in range(0,3):
			exp = exp + pow(vet[i][j],2)
		
		p.append(int(math.sqrt(exp)))
	return p

#calcula raio da esfera
def raio_e(vet):
	e = [2*vet[x] for x in range(0,len(vet))]
	return e



def busca_binaria(k,vet,e,d):
	if e <= d:
		m = int((e+d)/2)
		if k <= vet[m]:
			vet.pop(m)
			return 1
		else:
			return busca_binaria(k,vet,m+1,d)
	else:
		return 0


def total_e(p,e):
	total = [1 for i in range(0,len(p)) if p[i] <= e[i]]
	return len(total)


def total(v,r):
	total = []
	for i in range(0,len(v)):
		total.append(busca_binaria(v[i],r,0,len(r)-1))

	total = sum(total)
	#print(total)
	return total


#processa entradas
def processa():
	global raio
	n = int(input())
	p = []
	#e = []
	#entrada paralelepipedo
	for x in range(0,n):
		entrada = input().split()
		entrada = [int(x) for x in entrada]
		p.append(entrada)

	
	#vol_p = diagonal_p(p)
	vol_p = volume_p(p)
	e = [int(input()) for x in range(0,n)]
	
	#raio = raio_e(e)
	raio = cubo_e(e)

	vol_p =  quicksort(vol_p)
	raio = quicksort(raio)

	print(vol_p)
	print(raio)

	print(total(vol_p,raio))
	

processa()

