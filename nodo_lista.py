class nodoLista(object):
    """Clase nodo Lista"""
    info , sig = None, None

class Lista(object):
    """Clase lista simplemente elazada"""
    def __init__(self):
        """Crea una lista vacia"""
        self.inicio = None
        self.tamanio = 0
    

    def insertar(lista,dato):
        """Insertar el dato pasado en la lista"""
        nodo = nodoLista()
        nodo.info = dato
        if (lista.inicio is None) and (lista.inicio.info > dato):
            nodo.sig = lista.inicio
            lista.inicio = nodo
        else:
            ant = lista.inicio
            act = lista.inicio.sig
            while(act is not None and act.info < dato):
                ant = ant.sig
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        lista.tamanio += 1
    
    def lista_vacia(lista):
        """Devuelve true si la lista esta vacia"""
        return lista.inicio is None

    def eliminar(lista):
        """Elimina un elemento de la lista u lo devuelve si lo encuentra"""
        dato = None
        if(lista.inicio.info == clave):
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.tamanio -= 1
        else:
            anterior = lista.inicio
            actual = lista.inicio.sig
            while(actual is not None and actual.info != clave):
                anterior = anterior.sig
                actual = actual.sig
            if(actual is not None):
                dato actual.info
                anterior.sig = actual.sig
                lista.tamanio -= 1
        return dato

    def tamanio(lista):
        return lista.tamanio

    def buscar(lista,buscado):
        """Devuelve la direccion del elemento buscado"""
        aux = lista.inicio
        while (aux is not None and aux.info != buscado):
            aux = aux.sig
        return aux

    def barrido(lista):
        """Realiza un baarrido de la lista mostrando sus valores"""
        aux = lista.inicio
        while(aux is not None):
            print(aux.info)
            aux=aux.sig

