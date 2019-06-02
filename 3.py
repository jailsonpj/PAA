import math

#calcula volume de um paralelepipedo
def volume_p(vet):
	p = []
	for i in range(0,len(vet)):
		exp = 1
		for j in range(0,3):
			exp = exp * vet[i][j]
		p.append(exp)
	return p

#calcula raio da esfera
def raio_e(vet):
	e = [math.pow(vet[x],3) for x in range(0,len(vet))]
	return e

#calcula total de paralepipedos que cabem nas esferas
def total_e(p,e):
	total = [1 for i in range(0,len(p)) if p[i] < e[i]]
	return len(total)

#processa entradas
def processa():
	n = int(input())
	p = []
	#e = []
	#entrada paralelepipedo
	for x in range(0,n):
		entrada = input().split()
		entrada = [int(x) for x in entrada]
		p.append(entrada)

	#print(p)
	vol_p = volume_p(p)
	#print(vol_p)

	# entrada esfera
	e = [int(input()) for x in range(0,n)]
	#print(e)
	raio = raio_e(e)
	#print(raio)

	print(total_e(vol_p,raio))

processa()

