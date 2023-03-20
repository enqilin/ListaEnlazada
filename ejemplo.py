from nodo_lista import Lista, insertar, buscar, eliminar, barrido


lista = Lista()
dato =  input("Ingrese una palabra ")

while(dato !=''):
    insertar(lista, dato)
    dato = input('Ingrese una palabra')

buscado = input("Ingrese la palabra a buscar ")
posicion = buscar(lista,buscado)

if(posicion is not None):
    dato = eliminar(lista, posicion.info)
    print("Elemento elimondo: ", dato)
else:
    print("No se encontro el elemento a eliminar")

barrido(lista)
