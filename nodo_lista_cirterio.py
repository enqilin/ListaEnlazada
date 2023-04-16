
class nodoLista(object):
    """Clase nodo Lista"""
    info , sig = None, None

class Lista(object):
    """Clase lista simplemente elazada"""
    def __init__(self):
        """Crea una lista vacia"""
        self.inicio = None
        self.tamanio = 0

    def criterio(dato , campo = None):
        dic = {}
        if (hasattr(dato, "__dict__")):
            dic = dato.__dict__
        if campo is None or campo not in dic:
            return dato
        else:
            return dic[campo]
        
    def insetar(lista, dato,campo = None):
        nodo =nodoLista()
        nodo.info =dato
        if lista.inicio is None or Lista.criterio(lista.inicio.info , campo) > Lista.criterio(dato,campo):
            nodo.sig = lista.inicio
            lista.inicio = nodo
        else:
            ant = lista.inicio
            act = lista.inicio.sig
            while act is not None and Lista.criterio(act.info ,campo) < Lista.criterio(dato,campo):
                ant = ant.sig
                act = act.sig
            nodo.sig = act
            ant.sig = nodo
        lista.tamanio += 1

    def buscar(lista, buscando,campo =None):
        aux = lista.inicio
        while aux is not None and Lista.criterio(aux.info , campo) != Lista.criterio(buscando,campo):
            aux = aux.sig
        return aux

    def eliminar(lista , clave, campo =None):
        dato = None
        if Lista.criterio(lista.inicio.info,campo) == Lista.criterio(clave,campo):
            dato = lista.inicio.info
            lista.inicio = lista.inicio.sig
            lista.tamanio -= 1
        else:
            anterior = lista.inicio
            actual = lista.inicio.sig
            while actual is not None and Lista.criterio(actual.info,campo) !=Lista.criterio(clave,campo):
                anterior = anterior.sig
                actual = actual.sig
            if actual is not None:
                dato = actual.info
                anterior.sig = actual.sig
                lista.tamanio -= 1
        return dato