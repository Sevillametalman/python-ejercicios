#funciones

#obtener_compra: llena la lista de compras ingresada por el usuario
def obtener_compra(n, lst):
	i = 0
	while i < n:
		producto = str(input("producto {}: ".format(i+1)))
		cantidad = int(input("\tcantidad: "))
		registro = producto, cantidad
		lst.insert(i, registro)
		i+=1

#crear_total: crea la lista de elementos que se pueden comprar, es decir, los que estan en el inventario y fueron solicitados
#el campo registro[3] esta conformado por el total de la cantidad pedida por el precio en inventario
def crear_total(total, compra, inventario):
	i = 0
	for buscado in compra:
		for actual in inventario:
			if buscado[0] == actual[0]:
				registro = buscado[1], actual[0], actual[1], actual[2], buscado[1]*actual[3] 
				total.insert(i, registro)
				i+=1

#obtener_total: obtiene el resultado de sumar cada elemento comprado. 
def obtener_total(lst):
	total = 0
	for actual in lst:
		total+=actual[4]
	return total

#imprimir_lst: imprime los valores de una lista de tuplas
def imprimir_lst(lst):
	for it in lst:
		print("\t{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}".format(it[0], it[1], it[2], it[3], it[4]))

#inicializar_inventario: introduce los valores arbitrarios de inventario en una lista
def inicializar_inventario(lst):
	lst.insert(0, ("leche","en polvo","los andes",200))
	lst.insert(1, ("queso","en crema","kraft",325))
	lst.insert(2, ("avena","en hojuelas","Quaker",145))
	lst.insert(3, ("azucar","pulverizada","splenda",458))
	lst.insert(4, ("aceite","vegetal","mazeite",253))
	lst.insert(5, ("arroz","blanco","mary",214))
	lst.insert(6, ("pasta","tornillo","sindoni",129))
	lst.insert(7, ("caraotas","negras","pantera",342))
	lst.insert(8, ("yogurt","firme","yoka",412))
	lst.insert(9, ("atun","enlatado","margarita",143))
	lst.insert(10, ("jamon","endiablado","plumrose",114))
	lst.insert(11, ("harina","de trigo","robin hood",874))
	lst.insert(12, ("agua","mineral","nevada",127))
	lst.insert(13, ("jabon","en polvo","las llaves",427))
	lst.insert(14, ("papel","higienico","scott",742))
	lst.insert(15, ("crema","dental","colgate",958))

"""....................................................................."""

#programa principal

lst_productos = []
lst_compra = []
lst_total = []

inicializar_inventario(lst_productos)

cantidad_productos = int(input("\t\tCompra Supermercado\n\nIngrese cantidad de productos a comprar: "))
obtener_compra(cantidad_productos, lst_compra)

crear_total(lst_total, lst_compra, lst_productos)
total = obtener_total(lst_total)

print("\n\t\t\tResumen de Compra\n\tCant\t\tNombre\t\tPresentacion\t\tMarca\t\tSubtotal")
imprimir_lst(lst_total)
print("\n\tTotal: {}".format(total))