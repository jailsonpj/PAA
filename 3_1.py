
#processa entradas
def processa():
	n = int(input())
	lados = []
	raios = []

	#entrada paralelepipedo
	for i in range(0,n):
		l1, l2, l3 = [int(x) for x in input().split(' ')]
		lados.append(l1**2 + l2**2 + l3**2)

	for i in range(n):
		raio = int(input())
		raios.append(4 * (raio**2))

	#Ordenação
	lados = sorted(lados)
	raio = sorted(raios)

	#verififa 
	total = 0
	i,j=0,0
	while i<len(lados) and j<len(lados):
		if lados[i]<=raio[j]:
			#print(v[i])
			i+=1
			j+=1
			total+=1
		else:
			j+=1

	print(total)


processa()
