from ListaSimple.Nodo import Nodo

class ListaS:
    def __init__(self):
        self.primero = None


    def insertar(self,dato):
        unNodo = Nodo(dato)
        if self.primero == None:
            self.primero= unNodo
        else:
            temp = self.primero
            while temp.siguiente != None:
                temp = temp.siguiente
            temp.siguiente = unNodo
            unNodo.anterior = temp