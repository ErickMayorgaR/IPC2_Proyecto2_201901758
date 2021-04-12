from MatrizOrtogonal.UnaMatriz import unamatriz
import os
from MatrizOrtogonal import *
import time
from ListaSimple.ListaSimple import ListaS
import xml.etree.ElementTree as ET

class Logica:
    listaMatrices = ListaS()
    reporte = []

    def almacenaDatos(self, UnXML):
        contlleno = 0
        contvacio = 0

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
                            if dato == "*":
                                contlleno += 1
                            else:
                                contvacio +=1

            self.listaMatrices.insertar(unaMatriz)

            fecha = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
            self.reporte.append(fecha + unaMatriz.nombre + "-Espacios Llenos "+ str(contlleno)+
                                "-Espacios Vacios"+ str(contvacio))

            contlleno = 0
            contvacio = 0

        ver= 0

    def graficaMatriz(self, Matriz):
        nombre = Matriz.dato.nombre
#################
        imagen = ""
        encabezadoGraphviz = 'digraph G {' + '\n' + ' TABLA [shape = plaintext label =< ' + '\n' + ' <TABLE border="0" cellspacing="1" cellborder = "1" cellpadding = "2">'
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



        nueva_matriz.nombre = (matriz.dato.nombre + "Transpuesta")
#####################################
        nueva_matriz.nColumnas = matriz.dato.nFilas
        nueva_matriz.nFilas = matriz.dato.nColumnas
################################################################3
        self.listaMatrices.insertar(nueva_matriz)
        graficar = self.encontrarMatriz(nueva_matriz.nombre)
        self.graficaMatriz(graficar)

        return nueva_matriz.nombre



    def Limpiar(self, M1, coordenadas):
        coordenada = coordenadas.split(",")
        x1 = int(coordenada[0])
        y1 = int(coordenada[1])
        x2 = int(coordenada[2])
        y2 = int(coordenada[3])

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
                    nueva_matriz.insertarDato(contadorF, contadorC, "*")
                else:
                    nueva_matriz.insertarDato(contadorF, contadorC, "_")
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        nueva_matriz.nombre = (matriz.dato.nombre + "Limpiar")
        nueva_matriz.nColumnas = matriz.dato.nColumnas
        nueva_matriz.nFilas = matriz.dato.nFilas

        contadorF = 1
        contadorC = 1
        matriz = nueva_matriz


        fila = matriz.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                if y1 <= casilla.columna <= y2 and x1 <= casilla.fila <= x2:
                    casilla.dato = "-"
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        self.listaMatrices.insertar(nueva_matriz)
        graficar = self.encontrarMatriz(nueva_matriz.nombre)
        self.graficaMatriz(graficar)

        return nueva_matriz.nombre
        var = ''

    def LineaH(self, M1, coordenadas):
        coordenada = coordenadas.split(",")
        x1 = int(coordenada[0])
        y1 =int(coordenada[1])
        largo = int(coordenada[2])

        contadorF = 1
        contadorC = 1
        matriz = self.encontrarMatriz(M1)
        nueva_matriz = unamatriz()

        fila = matriz.dato.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                if casilla.dato == "*":
                    nueva_matriz.insertarDato(contadorF, contadorC, "*")
                else:
                    nueva_matriz.insertarDato(contadorF, contadorC, "_")
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        nueva_matriz.nombre = (matriz.dato.nombre + "LineaH")
        nueva_matriz.nColumnas = matriz.dato.nColumnas
        nueva_matriz.nFilas = matriz.dato.nFilas

        contadorF = 1
        contadorC = 1
        matriz = nueva_matriz

        fila = nueva_matriz.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                if y1 <= casilla.columna <= (y1+largo-1) and casilla.fila ==x1 :
                    casilla.dato = "*"
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente


        self.listaMatrices.insertar(nueva_matriz)
        graficar = self.encontrarMatriz(nueva_matriz.nombre)
        self.graficaMatriz(graficar)

        return nueva_matriz.nombre

    def LineaV(self, M1, coordenadas):
        coordenada = coordenadas.split(",")
        x1 = int(coordenada[0])
        y1 = int(coordenada[1])
        largo = int(coordenada[2])

        contadorF = 1
        contadorC = 1
        matriz = self.encontrarMatriz(M1)
        nueva_matriz = unamatriz()

        fila = matriz.dato.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                if casilla.dato == "*":
                    nueva_matriz.insertarDato(contadorF, contadorC, "*")
                else:
                    nueva_matriz.insertarDato(contadorF, contadorC, "_")
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        nueva_matriz.nombre = (matriz.dato.nombre + "LineaV")
        nueva_matriz.nColumnas = matriz.dato.nColumnas
        nueva_matriz.nFilas = matriz.dato.nFilas

        contadorF = 1
        contadorC = 1
        matriz = nueva_matriz

        fila = nueva_matriz.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                if casilla.columna == y1 and x1 <= casilla.fila <= (x1+largo -1):
                    casilla.dato = "*"
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        self.listaMatrices.insertar(nueva_matriz)
        graficar = self.encontrarMatriz(nueva_matriz.nombre)
        self.graficaMatriz(graficar)

        return nueva_matriz.nombre

    def Rectangulo(self, M1, coordenadas):
        coordenada = coordenadas.split(",")
        x1 = int(coordenada[0])
        y1 = int(coordenada[1])
        tamF= int(coordenada[2])
        tamC = int(coordenada[3])

        contadorF = 1
        contadorC = 1
        matriz = self.encontrarMatriz(M1)
        nueva_matriz = unamatriz()

        fila = matriz.dato.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                if casilla.dato == "*":
                    nueva_matriz.insertarDato(contadorF, contadorC, "*")
                else:
                    nueva_matriz.insertarDato(contadorF, contadorC, "_")
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        nueva_matriz.nombre = (matriz.dato.nombre + "Rectangulo")
        nueva_matriz.nColumnas = matriz.dato.nColumnas
        nueva_matriz.nFilas = matriz.dato.nFilas

        contadorF = 1
        contadorC = 1
        matriz = nueva_matriz

        fila = nueva_matriz.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                if y1 <= casilla.columna < (y1+ tamC) and x1 <= casilla.fila < (x1+ tamF):
                    casilla.dato = "*"
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        self.listaMatrices.insertar(nueva_matriz)
        graficar = self.encontrarMatriz(nueva_matriz.nombre)
        self.graficaMatriz(graficar)

        return nueva_matriz.nombre


    def Triagulo(self, M1, coordenadas):
        coordenada = coordenadas.split(",")
        x1 = int(coordenada[0])
        y1 = int(coordenada[1])
        tam = int(coordenada[2])


        contadorF = 1
        contadorC = 1
        matriz = self.encontrarMatriz(M1)
        nueva_matriz = unamatriz()

        fila = matriz.dato.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                if casilla.dato == "*":
                    nueva_matriz.insertarDato(contadorF, contadorC, "*")
                else:
                    nueva_matriz.insertarDato(contadorF, contadorC, "_")
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        nueva_matriz.nombre = (matriz.dato.nombre + "Triangulo")
        nueva_matriz.nColumnas = matriz.dato.nColumnas
        nueva_matriz.nFilas = matriz.dato.nFilas

        opero = False
        contadorF = 1
        contadorC = 1
        contadortamF = tam
        contadortamC = 0
        matriz = nueva_matriz

        fila = nueva_matriz.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                if contadortamC < tam:
                    if casilla.columna == y1 and casilla.fila == (x1- contadortamF+ 1):
                        opero = True
                        casilla.dato = "*"
                    if y1 <= casilla.columna <=(y1 + contadortamC) and casilla.fila == (x1 - contadortamF + 1):
                        opero = True
                        casilla.dato = "*"
                contadorC += 1
                casilla = casilla.derecha
            if opero == True:
                opero = False
                contadortamC +=1
                contadortamF -= 1

            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        self.listaMatrices.insertar(nueva_matriz)
        graficar = self.encontrarMatriz(nueva_matriz.nombre)
        self.graficaMatriz(graficar)

        return nueva_matriz.nombre


    def Union(self, M1, M2):
        matriz1 = self.encontrarMatriz(M1)
        matriz2 = self.encontrarMatriz(M2)
        matriz = self.encontrarMatriz(M1)
        contadorF = 1
        contadorC = 1

        nueva_matriz = unamatriz()

        fila = matriz.dato.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                nueva_matriz.insertarDato(contadorF, contadorC, "_")
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        nueva_matriz.nombre = (matriz1.dato.nombre + "Union" + matriz2.dato.nombre)
        nueva_matriz.nColumnas = matriz.dato.nColumnas
        nueva_matriz.nFilas = matriz.dato.nFilas

        fila1 = matriz1.dato.UnaFila.primero
        fila2 = matriz2.dato.UnaFila.primero
        fila = nueva_matriz.UnaFila.primero
        while fila != None:
            casilla1 = fila1.accesoNodo
            casilla2 = fila2.accesoNodo
            casilla = fila.accesoNodo
            while casilla != None:
                if casilla1.dato == "*" or casilla2.dato == "*":
                    casilla.dato = "*"
                contadorC += 1
                casilla = casilla.derecha
                casilla1 = casilla1.derecha
                casilla2 = casilla2.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente
            fila1 = fila1.siguiente
            fila2 = fila2.siguiente

        self.listaMatrices.insertar(nueva_matriz)
        graficar = self.encontrarMatriz(nueva_matriz.nombre)
        self.graficaMatriz(graficar)
        return nueva_matriz.nombre




    def Intereseccion(self, M1, M2):
        matriz1 = self.encontrarMatriz(M1)
        matriz2 = self.encontrarMatriz(M2)
        matriz = self.encontrarMatriz(M1)
        contadorF = 1
        contadorC = 1

        nueva_matriz = unamatriz()

        fila = matriz.dato.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                nueva_matriz.insertarDato(contadorF, contadorC, "_")
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        nueva_matriz.nombre = (matriz1.dato.nombre + "Interseccion" + matriz2.dato.nombre)
        nueva_matriz.nColumnas = matriz.dato.nColumnas
        nueva_matriz.nFilas = matriz.dato.nFilas

        fila1 = matriz1.dato.UnaFila.primero
        fila2 = matriz2.dato.UnaFila.primero
        fila = nueva_matriz.UnaFila.primero
        while fila != None:
            casilla1 = fila1.accesoNodo
            casilla2 = fila2.accesoNodo
            casilla = fila.accesoNodo
            while casilla != None:
                if casilla1.dato == "*"and casilla2.dato== "*":
                    casilla.dato = "*"
                contadorC += 1
                casilla = casilla.derecha
                casilla1 = casilla1.derecha
                casilla2 = casilla2.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente
            fila1 = fila1.siguiente
            fila2 = fila2.siguiente

        self.listaMatrices.insertar(nueva_matriz)
        graficar = self.encontrarMatriz(nueva_matriz.nombre)
        self.graficaMatriz(graficar)

        return nueva_matriz.nombre


    def Diferencia(self,M1, M2):
        matriz1 = self.encontrarMatriz(M1)
        matriz2 = self.encontrarMatriz(M2)
        matriz = self.encontrarMatriz(M1)
        contadorF = 1
        contadorC = 1

        nueva_matriz = unamatriz()

        fila = matriz.dato.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                nueva_matriz.insertarDato(contadorF, contadorC, "_")
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        nueva_matriz.nombre = (matriz1.dato.nombre + "Diferencia" + matriz2.dato.nombre)
        nueva_matriz.nColumnas = matriz.dato.nColumnas
        nueva_matriz.nFilas = matriz.dato.nFilas

        fila1 = matriz1.dato.UnaFila.primero
        fila2 = matriz2.dato.UnaFila.primero
        fila = nueva_matriz.UnaFila.primero
        while fila != None:
            casilla1 = fila1.accesoNodo
            casilla2 = fila2.accesoNodo
            casilla = fila.accesoNodo
            while casilla != None:
                if casilla1.dato == "*" and casilla2.dato != "*":
                    casilla.dato = "*"
                contadorC += 1
                casilla = casilla.derecha
                casilla1 = casilla1.derecha
                casilla2 = casilla2.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente
            fila1 = fila1.siguiente
            fila2 = fila2.siguiente

        self.listaMatrices.insertar(nueva_matriz)
        graficar = self.encontrarMatriz(nueva_matriz.nombre)
        self.graficaMatriz(graficar)

        return nueva_matriz.nombre

    def DiferenciaSimetrica(self, M1, M2):
        matriz1 = self.encontrarMatriz(M1)
        matriz2 = self.encontrarMatriz(M2)
        matriz = self.encontrarMatriz(M1)
        contadorF = 1
        contadorC = 1

        nueva_matriz = unamatriz()

        fila = matriz.dato.UnaFila.primero
        while fila != None:
            casilla = fila.accesoNodo
            while casilla != None:
                nueva_matriz.insertarDato(contadorF, contadorC, "_")
                contadorC += 1
                casilla = casilla.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente

        nueva_matriz.nombre = (matriz1.dato.nombre + "DiferenciaSimetrica" + matriz2.dato.nombre)
        nueva_matriz.nColumnas = matriz.dato.nColumnas
        nueva_matriz.nFilas = matriz.dato.nFilas

        fila1 = matriz1.dato.UnaFila.primero
        fila2 = matriz2.dato.UnaFila.primero
        fila = nueva_matriz.UnaFila.primero
        while fila != None:
            casilla1 = fila1.accesoNodo
            casilla2 = fila2.accesoNodo
            casilla = fila.accesoNodo
            while casilla != None:
                if casilla1.dato == "*" and casilla2.dato != "*":
                    casilla.dato = "*"
                if casilla1.dato != "*" and casilla2.dato == "*":
                    casilla.dato = "*"
                contadorC += 1
                casilla = casilla.derecha
                casilla1 = casilla1.derecha
                casilla2 = casilla2.derecha
            contadorC = 1
            contadorF += 1
            fila = fila.siguiente
            fila1 = fila1.siguiente
            fila2 = fila2.siguiente

        self.listaMatrices.insertar(nueva_matriz)
        graficar = self.encontrarMatriz(nueva_matriz.nombre)
        self.graficaMatriz(graficar)

        return nueva_matriz.nombre

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

    def generarReporte(self):
        tam = len(self.reporte)
        auxtam = tam + 1
        saltoL = "\n"
        reporte = ""
        reporte += '<!DOCTYPE html>' + "\n"+ '<html lang="en">' + '\n' +  '<head>' + '\n' + '<meta charset="UTF-8">'+ \
                     '\n' + '<meta name="viewport" content="width=device-width, initial-scale=1.0">' + '\n' + \
                   '<title>Formulario</title>' + '\n' + '<link rel="stylesheet" type="text/css"  media="">' + '\n' +\
              '</head>' + '\n' + '<center>' + '\n' + '<body>' + '\n' + '<header>' + '\n' + '<h1>Reporte</h1>' + '\n' + '</header>'
        reporte += saltoL
        for i in range(tam):
            reporte += '<p>' + self.reporte[i] +'</p>'
            reporte += saltoL

        reporte += '</body> \n </center> \n </html>'

        with open("Reporte.html", 'w', encoding='utf-8') as file:
            file.write(reporte)
            file.close()


        os.system("Reporte.html")








