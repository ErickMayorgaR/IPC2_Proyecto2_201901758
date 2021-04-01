from MatrizOrtogonal.UnaMatriz import UnaMatriz

from MatrizOrtogonal import *
from ListaSimple.ListaSimple import ListaS
import xml.etree.ElementTree as ET

class Logica:
    listaMatrices = ListaS()

    def almacenaDatos(self, UnXML):
        arbol = ET.parse(UnXML)
        raiz = arbol.getroot()

        for matriz in raiz:
            unaMatriz = UnaMatriz()
            for elemento in matriz:
                print(elemento.tag.lower())






