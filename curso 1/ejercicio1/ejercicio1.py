#funciones

#crear_dep: recibe la cantidad de variables dependientes e inserta cada una en una lista
def crear_dep(lst):
	n = int(input("\nVariables Dependientes\n\t-Cantidad de variables dependientes: "))
	for i in range(0 , n):
		variable = str(input("\t\t-Variable {}: ".format(i+1)))
		lst.insert(i, variable)

#crear_indep:
def crear_indep(lst):
	n = int(input("\nVariables Independientes\n\t-Cantidad de variables independientes: "))
	for i in range(0 , n):
		variable = str(input("\t\t-Variable {}: ".format(i+1)))
		lst.insert(i, variable)
#imprimir_lst: imprime una lista
def imprimir_ecuacion(lst):
	ecuacion = ""
	for it in lst:
		ecuacion+=it
	print(ecuacion)


def encontrar_soluciones(solucion, ecuacion, independientes, dependientes):
	i = 0
	while i < len(dependientes):
		posicion = 0
		j = 0
		while j < len(independientes):
			for termino in ecuacion:
				if termino == 'x' or termino == 'y':
					solucion.insert(posicion, dependientes[i])
				elif termino == 'a' or termino == 'b':
					solucion.insert(posicion, independientes[j])
				else:
					solucion.insert(posicion, termino)
				posicion+=1	
			imprimir_ecuacion(solucion)
			solucion.clear()	
			j+=1
		i+=1
	return True

"""............................................................"""

#programa principal
lst_solucion = []
lst_dependientes = []
lst_independientes = []
lst_ecuaciones = [["(", "x", "-", "y", ")", "*", "(", "a", "-", "b", ")"], ["x", "+", "*", "a", "-", "y"],["x", "*", "*", "2", "+", "2", "*", "*", "a", "-", "y", "*", "*", "2"]]

print("\t\tPrograma Ecuaciones\n")

crear_dep(lst_dependientes)
crear_indep(lst_independientes)

#imprimir_lst(lst_dependientes)
#imprimir_lst(lst_independientes)

for i in range(0, 3):
	encontrar_soluciones(lst_solucion, lst_ecuaciones[i], lst_independientes, lst_dependientes)

