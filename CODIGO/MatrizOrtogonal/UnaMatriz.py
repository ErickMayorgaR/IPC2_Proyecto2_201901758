
from MatrizOrtogonal.NodoDato import NodoDato
from MatrizOrtogonal.NodoEncabezado import NodoEncabezado
from MatrizOrtogonal.ListaEncabezados import ListaEncabezado

class UnaMatriz:
    def __init__(self, nombre):
        self.nombre = nombre
        self.UnaFila = ListaEncabezado()
        self.UnaColumna = ListaEncabezado()

    def insertarDato(self, fila, columna, dato):
        unNodo = NodoDato(fila, columna, dato)
        auxFila = self.UnaFila.ObtenerEncabezado(fila)

        if auxFila == None:
            auxFila = NodoEncabezado(fila)
            auxFila.accesoNodo = unNodo
            self.UnaFila.insertaEncabezado(auxFila)
        else:
            if unNodo.columna < auxFila.accesoNodo.columna:
                unNodo.derecha = auxFila.accesoNodo
                auxFila.accesoNodo.izquierda = unNodo
                auxFila.accesoNodo = unNodo
            else:
                #aqui recorro las columnas en una fila en especifico para saber si existe
                #si existe, se inserta
                actual = auxFila.accesoNodo
                while actual.derecha !=None:
                    if unNodo.columna < actual.derecha.columna:
                        unNodo.derecha = actual.derecha
                        actual.derecha.izquierda = unNodo
                        unNodo.izquierda = actual
                        actual.derecha = unNodo
                        break
                    actual = actual.derecha
                #Si no existe una columna en donde se pueda colocar el encabezado en la fila en la cal
                if actual.derecha == None:
                    actual.derecha = unNodo
                    unNodo.izquierda = actual


        auxColumna = self.UnaColumna.ObtenerEncabezado(columna)

        if auxColumna == None:
            auxColumna = NodoEncabezado(columna)
            auxColumna.accesoNodo = unNodo
            self.UnaColumna.insertaEncabezado(auxColumna)
        else:
            if unNodo.fila < auxColumna.accesoNodo.Fila:
                unNodo.abajo = auxFila.accesoNodo
                auxFila.accesoNodo.arriba = unNodo
                auxFila.accesoNodo = unNodo
            else:
                actual = auxColumna.accesoNodo
                while actual.abajo != None:
                    if unNodo.fila < actual.abajo.fila:
                        unNodo.abajo = actual.abajo
                        actual.abajo.arriba = unNodo
                        unNodo.arriba = actual
                        actual.abajo = unNodo
                        break
                    actual = actual.abajo

                if actual.abajo == None:
                    actual.abajo = unNodo
                    unNodo.arriba = actual







