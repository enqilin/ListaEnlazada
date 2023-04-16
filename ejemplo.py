from nodo_lista import Lista
from nodo_lista import Lista as insertar
from nodo_lista import Lista as buscar
from nodo_lista import Lista as eliminar
from nodo_lista import Lista as barrido


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
