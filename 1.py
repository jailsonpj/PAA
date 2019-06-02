import sys

'''
A solução da questão 1 :
	-  como visto , as combinações sempre irá pegar os dois maiores números do conjunto , não import se seja maior que dois,
	o resultdao irá pegar os dois maiores número do conjunto .
	- a solução se baseio em pegar as entradas e ordenar de forma decrescente os dois valores da tupla e depois pegar os dois primeiros 
	e imprimir o segundo item da tupla. 
'''



def quicksort(l):
	if l:
		left = [x for x in l if x > l[0]]
		right = [x for x in l if x < l[0]]
		if len(left) > 1:
			left = quicksort(left)
		if len(right) > 1:
			right = quicksort(right)
		return left + [l[0]] * l.count(l[0]) + right

	return []

def input_str():
	size = int(input())
	numbers = input()	
	numbers = numbers.split()
	cont = 0
	numbers = [(int(numbers[x]),x+1) for x in range(size)]
	print("ordenado")
	numbers = quicksort(numbers)
	print(numbers)
	v1,v2 = numbers[0],numbers[1]
	#Falta arrumar a saída

	if v1[1] > v2[1]:
		print(str(v2[1])+" "+str(v1[1]))
	else:
		print(str(v1[1])+" "+str(v2[1]))


input_str()
