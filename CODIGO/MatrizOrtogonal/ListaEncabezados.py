

class ListaEncabezado:

    def __init__(self):
        self.primero = None

    def insertaEncabezado(self,EncabezadoNuevo):
        if self.primero == None:
            self.primero = EncabezadoNuevo
        elif EncabezadoNuevo.id < self.primero.id:
            EncabezadoNuevo.siguiente = self.primero
            self.primero.anterior = EncabezadoNuevo
            self.primero = EncabezadoNuevo
        else:
            actual = self.primero
            while actual.siguiente != None:
                if EncabezadoNuevo.id < actual.siguiente.id:
                    EncabezadoNuevo.siguiente = actual.siguiente
                    actual.siguiente.anterior = EncabezadoNuevo
                    EncabezadoNuevo.anterior = actual
                    actual.siguiente = EncabezadoNuevo
                    break
                actual = actual.siguiente

            if actual.siguiente == None:
                actual.siguiente = EncabezadoNuevo
                EncabezadoNuevo.anterior = actual

    def ObtenerEncabezado(self, id):
        actual = self.primero
        while actual != None:
            if actual.id == id:
                return actual
            actual = actual.siguiente
        return None













