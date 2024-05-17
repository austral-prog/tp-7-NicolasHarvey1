def enumerate_list(lista):
	index = 0
	while index < len(lista):
		if lista[index]:
			word = lista[index]
			lista[index] = f"{index}. {word}"
			index += 1
		else:
			del lista[index]		
	return lista


def enumerate_backwards(lista2):
	index = 0
	while index < len(lista2):
		if lista2[index]:
			word = lista2[index][::-1]
			lista2[index] = f"{index}. {word}"
			index += 1
		else:
			del lista2[index]		
	return lista2
