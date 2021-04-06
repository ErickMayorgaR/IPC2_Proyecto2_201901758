from MatrizOrtogonal.UnaMatriz import unamatriz
import os
from MatrizOrtogonal import *
from ListaSimple.ListaSimple import ListaS
import xml.etree.ElementTree as ET

class Logica:
    listaMatrices = ListaS()

    def almacenaDatos(self, UnXML):

        arbol = ET.parse(UnXML)
        raiz = arbol.getroot()

        for matriz in raiz:

            unaMatriz = unamatriz()
            for elemento in matriz:
                if elemento.tag.lower() == "nombre":
                    unaMatriz.nombre = elemento.text
                if elemento.tag.lower() == "filas":
                    unaMatriz.nFilas = int(elemento.text)
                if elemento.tag.lower() == "columnas":
                    unaMatriz.nColumnas = int(elemento.text)
                if elemento.tag.lower() == "imagen":
                    contadorFila = 0
                    contadorColumna = 0
                    for dato in elemento.text:
                        if dato == " ":
                            continue
                        elif dato == "\t":

                            continue
                        elif dato == "\n":
                            contadorColumna = 0
                            contadorFila +=1
                            continue
                        else:

                            contadorColumna +=1
                            unaMatriz.insertarDato(contadorFila,contadorColumna,dato)

            self.listaMatrices.insertar(unaMatriz)
        ver= 0

    def graficaMatriz(self, Matriz):
        nombre = Matriz.dato.nombre

        imagen = ""
        encabezadoGraphviz = 'digraph G {' + '\n' + ' TABLA [shape = plaintext label =< ' + '\n' + ' <TABLE border="0" cellspacing="1" cellborder = "1" cellpadding = "250">'
        saltoLinea = '\n'
        casillaNegro = '<TD bgcolor="black"></TD>'
        casillaBlanco = '<TD></TD>'
        imagen += encabezadoGraphviz
        imagen += saltoLinea

        fila = Matriz.dato.UnaFila.primero
        while fila != None:
            imagen += '<TR>'
            imagen += saltoLinea
            casilla = fila.accesoNodo
            while casilla != None:
                if casilla.dato == "*":
                    imagen += casillaNegro

                else:
                    imagen += casillaBlanco
                imagen += saltoLinea
                casilla = casilla.derecha

            imagen += '</TR>'

            fila = fila.siguiente

        imagen += '</TABLE>>];' +'\n' + '}'

        directorio = 'Imagenes/'
        directorio += nombre
        directoriodot = directorio  + ".dot"
        directorioPng = directorio + ".png"
        with open(directoriodot, 'w', encoding='utf-8') as file:
            file.write(imagen)
            file.close()

        varos = 'dot -Tpng ' + directoriodot + ' -o ' + directorioPng
        print(varos)
        var = "dot -Tpng Prueba.dot -o P1.png'"
        os.system(varos)

    def devolverMatrices(self):
        return self.listaMatrices

    def rotacionH(self, M1):
        contadorF = 1
        contadorC = 1
        matriz = self.encontrarMatriz(M1)
        nueva_matriz = unamatriz()
        filas = int(matriz.dato.nFilas)

        fila = matriz.dato.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                if casilla.dato == "*":
                    nueva_matriz.insertarDato((filas-(contadorF-1)), contadorC,"*")
                else:
                    nueva_matriz.insertarDato((filas - (contadorF - 1)), contadorC, "_")
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente


        nueva_matriz.nombre = (matriz.dato.nombre + "Horizontal")
        nueva_matriz.nColumnas = matriz.dato.nColumnas
        nueva_matriz.nFilas = matriz.dato.nFilas

        self.listaMatrices.insertar(nueva_matriz)
        graficar = self.encontrarMatriz(nueva_matriz.nombre)
        self.graficaMatriz(graficar)

        return nueva_matriz.nombre



    def rotacionV(self, M1):
        contadorF = 1
        contadorC = 1
        matriz = self.encontrarMatriz(M1)
        nueva_matriz = unamatriz()
        columnas = int(matriz.dato.nColumnas)

        fila = matriz.dato.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                if casilla.dato == "*":
                    nueva_matriz.insertarDato(contadorF, (columnas -(contadorC- 1)), "*")
                else:
                    nueva_matriz.insertarDato(contadorF,(columnas -(contadorC- 1)), "_")
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        nueva_matriz.nombre = (matriz.dato.nombre + "Vertical")
        nueva_matriz.nColumnas = matriz.dato.nColumnas
        nueva_matriz.nFilas = matriz.dato.nFilas

        self.listaMatrices.insertar(nueva_matriz)
        graficar = self.encontrarMatriz(nueva_matriz.nombre)
        self.graficaMatriz(graficar)

        return nueva_matriz.nombre


    def Transpuesta(self, M1):
        contadorF = 1
        contadorC = 1
        matriz = self.encontrarMatriz(M1)
        nueva_matriz = unamatriz()
        filas = int(matriz.dato.nFilas)

        fila = matriz.dato.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                if casilla.dato == "*":
                    nueva_matriz.insertarDato(contadorC, contadorF, "*")
                else:
                    nueva_matriz.insertarDato(contadorC, contadorF, "_")
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente



        nueva_matriz.nombre = (matriz.dato.nombre + "Transpuesta    ")
        nueva_matriz.nColumnas = matriz.dato.nColumnas
        nueva_matriz.nFilas = matriz.dato.nFilas

        self.listaMatrices.insertar(nueva_matriz)
        graficar = self.encontrarMatriz(nueva_matriz.nombre)
        self.graficaMatriz(graficar)

        return nueva_matriz.nombre



    def Limpiar(self, M1, coordenadas):
        matriz = self.encontrarMatriz(M1)

    def LineaH(self, M1, coordenadas):
        matriz = self.encontrarMatriz(M1)

    def LineaV(self, M1, coordenadas):
        matriz = self.encontrarMatriz(M1)

    def Rectangulo(self, M1, coordenadas):
        matriz = self.encontrarMatriz(M1)

    def Triagulo(self, M1, coordenadas):
        matriz = self.encontrarMatriz(M1)

    def Union(self, M1, M2):
        matriz1 = self.encontrarMatriz(M1)
        matriz2 = self.encontrarMatriz(M2)

    def Intereseccion(self, M1, M2):
        matriz1 = self.encontrarMatriz(M1)
        matriz2 = self.encontrarMatriz(M2)

    def Diferencia(self,M1, M2):
        matriz1 = self.encontrarMatriz(M1)
        matriz2 = self.encontrarMatriz(M2)

    def DiferenciaSimetrica(self, M1, M2):
        matriz1 = self.encontrarMatriz(M1)
        matriz2 = self.encontrarMatriz(M2)

    def encontrarMatriz(self, nombre):
        matrizaux = None
        matrizEncontrada = None
        if self.listaMatrices.primero != None:
            matrizaux = self.listaMatrices.primero

        while matrizaux != None:
            if matrizaux.dato.nombre == nombre:
                matrizEncontrada = matrizaux
                break
            matrizaux = matrizaux.siguiente

        return  matrizEncontrada








