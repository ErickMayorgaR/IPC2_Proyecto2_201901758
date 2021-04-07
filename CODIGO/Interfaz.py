import tkinter as ttk
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from ClaseLogica import Logica
import tkinter as tk


class InterfazP:
    reporte = []
    selectM1= None
    selectM2 = None

    nomMatriz1 = None
    nomMatriz2 = None

    entradaTexto = None

    listaMatrices = None
    
    ComboboxUno = None
    ComboboxDos = None
    ComboboxOp = None
    
    logicaMatrices = Logica()
    ventanaOp = None
    ventana = None
    panelV1 = None

    labelMatriz1 = None
    labelMatriz2 = None
    labelMatriz3 = None

    label1 = None
    label2 = None
    label3 = None
    
    carga = None

    def iniciar(self):
        self.ventana = ttk.Tk()
        self.ventana.title("Ventana Principal")


        self.ventana.resizable(True, True)
        self.ventana.geometry("1005x420")
        self.ventana.config(background ="Black")

        self.panelV1 = ttk.Frame()
        self.panelV1.config(background = 'Black')
        self.panelV1.pack()



        botonCarga = ttk.Button(self.panelV1, text = "CargarArchivo", command = lambda:self.cargaArchivo())
        botonCarga.grid(row = 0, column = 0,padx = 10, pady = 20)

        botonOperaciones = ttk.Button(self.panelV1, text= "Operaciones", command = lambda:self.VentanaOperaciones() )
        botonOperaciones.grid(row = 0, column = 1,padx = 10, pady = 20)

        botonReportes = ttk.Button(self.panelV1, text= "Reportes",command=lambda: self.generarReporte())
        botonReportes.grid(row = 0, column = 2,padx = 10, pady = 20)

        botonAyuda = ttk.Button(self.panelV1, text = "Ayuda")
        botonAyuda.grid(row= 0, column = 3,padx = 10, pady = 20)

        #imagen1 = PhotoImage(file= "P1.png")
        #imagen1 = imagen1.subsample(3,3)

        #imagen = PhotoImage(file= "Imagenes/A.png")

        #imagen = imagen.subsample(3, 3)


        self.labelMatriz1 = ttk.Label(self.panelV1)
        self.labelMatriz1.config(bg = "White",width = "40", height = "20")
        self.labelMatriz1.grid(row = 1, column = 0, padx = 10, pady = 20)

        self.labelMatriz2 = ttk.Label(self.panelV1)
        self.labelMatriz2.config(bg="White", width="40", height="20")
        self.labelMatriz2.grid(row=1, column=1, padx=10, pady=20)

        self.labelMatriz3 = ttk.Label(self.panelV1)
        self.labelMatriz3.config(bg="White", width="40", height="20")
        self.labelMatriz3.grid(row=1, column=2, padx=10, pady=20)




        print("algo")
        self.ventana.mainloop()

    def cambiaEstadoVentanaCarga(self):
        self.cargaArchivo()



    def cargaArchivo(self):
        ruta = ttk.Toplevel(self.ventana)
        ruta.filename = filedialog.askopenfilename(filetypes=(("XML files", "*.xml"), ("all files", "*.*")))
        file = open(ruta.filename, "r", encoding='utf-8')
        # file = 'C:/Users/emayo/OneDrive/Desktop/IPC2-Proyecto1-201901758/Matriz2.xml'
        print(file)
        ruta.destroy()
        self.logicaMatrices.almacenaDatos(file)

    def VentanaOperaciones(self):

        nombres = []
        self.listaMatrices = self.logicaMatrices.devolverMatrices()
        matrices = self.logicaMatrices.devolverMatrices()
        unaMatriz = matrices.primero

        if matrices.primero != None:
            while unaMatriz != None:
                nombres.append(unaMatriz.dato.nombre)
                unaMatriz = unaMatriz.siguiente

            self.ventanaOp = ttk.Tk()
            self.ventanaOp.config(bg= "Black")
            self.ventanaOp.geometry("500x300")

            self.selectM1 = ttk.StringVar(self.ventanaOp)
            self.selectM2 = ttk.StringVar(self.ventanaOp)

            vardf = ""
            self.selectM1.set(vardf)
            self.selectM2.set(vardf)



            self.ComboboxUno = ttk.OptionMenu (self.ventanaOp, self.selectM1, vardf, *nombres)
            self.ComboboxUno.config(width = 20, height = 1)
            self.ComboboxUno.grid(row = 0, column = 0 ,padx = 20 ,pady = 20)

            self.ComboboxDos = ttk.OptionMenu (self.ventanaOp, self.selectM2,vardf, *nombres)
            self.ComboboxDos.config(width = 20, height = 1)
            self.ComboboxDos.grid(row = 0, column = 1, padx = 20, pady = 20)


            botonseleccionar= ttk.Button(self.ventanaOp, text= "Seleccionar", command = lambda:self.selecionarMatrices())
            botonseleccionar.grid(row= 0, column = 2,padx = 10, pady = 20)
        else:
            messagebox.showerror("", "Cargue un Archivo")


    def selecionarMatrices(self):
        contadorMatrices = 0
        Image.MAX_IMAGE_PIXELS = None

        if self.selectM1.get() != "" or self.selectM2.get() != "":
            matrizaux = None
            nombres = None

            if self.selectM1.get() != "":
                self.nomMatriz1 = self.selectM1.get()

            if self.selectM2.get() != "":
                self.nomMatriz2 = self.selectM2.get()

            if self.listaMatrices.primero != None:
                matrizaux = self.listaMatrices.primero

            while matrizaux != None:
                if matrizaux.dato.nombre == self.nomMatriz1:
                    self.logicaMatrices.graficaMatriz(matrizaux)

                elif matrizaux.dato.nombre == self.nomMatriz2:
                    self.logicaMatrices.graficaMatriz(matrizaux)

                matrizaux = matrizaux.siguiente
            if self.nomMatriz1 != None:
                varimagen = 'Imagenes/' + self.nomMatriz1 + ".png"
                print(varimagen)
                self.labelMatriz1.destroy()
                imagen = Image.open(varimagen)
                imagen = imagen.resize((300, 300), Image.ANTIALIAS)
                imagenv2 = ImageTk.PhotoImage(imagen)

                self.labelMatriz1 = ttk.Label(self.panelV1, image=imagenv2)
                self.labelMatriz1.grid(row=1, column=0, padx=10, pady=20)
                self.labelMatriz1.image = imagenv2

                contadorMatrices += 1

            if self.nomMatriz2!= None:
                varimagen2 = 'Imagenes/' + self.nomMatriz2 + ".png"
                print(varimagen2)

                self.labelMatriz2.destroy()
                imagen2 = Image.open(varimagen2)
                imagen2 = imagen2.resize((300, 300), Image.ANTIALIAS)
                imagen2v2 = ImageTk.PhotoImage(imagen2)

                self.labelMatriz2 = ttk.Label(self.panelV1, image=imagen2v2)
                self.labelMatriz2.grid(row=1, column=1, padx=10, pady=20)
                self.labelMatriz2.image = imagen2v2

                contadorMatrices += 1


        else:
            messagebox.showerror("", "Seleccione una Matriz")

        if contadorMatrices == 1:
            self.labelMatriz2 = ttk.Label(self.panelV1)
            self.labelMatriz2.config(bg="White", width="40", height="20")
            self.labelMatriz2.grid(row=1, column=1, padx=10, pady=20)
            self.operacionesunaM()

        elif contadorMatrices == 2:
            self.operacionesdosM()


    def operacionesunaM(self):
        self.ventanaOp.destroy()

        self.ventanaOp = ttk.Tk()
        self.ventanaOp.config(bg="Black")
        self.ventanaOp.geometry("500x300")

        self.selectM1 = ttk.StringVar(self.ventanaOp)

        operaciones = ["Rotación Horizontal","Rotación Vertical","Matriz Transpuesta", "Limpiar Zona", "Agregar Linea Horizontal",
                       "Agregar Linea Vertical", "Agregar Rectangulo", "Agregar Triangulo Rectangulo "   ]
        self.selectM1.set(operaciones[0])

        operaciones.pop(0)


        self.ComboboxOp = ttk.OptionMenu(self.ventanaOp, self.selectM1, self.selectM1.get(), *operaciones)
        self.ComboboxOp.config(width=20, height=1)
        self.ComboboxOp.grid(row=0, column=0, padx=20, pady=20)

        self.entradaTexto = ttk.Entry(self.ventanaOp)
        self.entradaTexto.config(width = 40)
        self.entradaTexto.grid(row = 1, column = 0, padx = 20, pady = 20)

        botonseleccionar = ttk.Button(self.ventanaOp, text="Seleccionar", command=lambda: self.seleccionarOperaciones())
        botonseleccionar.grid(row=0, column=3, padx=10, pady=20)



    def operacionesdosM(self):
        self.ventanaOp.destroy()



        self.ventanaOp = ttk.Tk()
        self.ventanaOp.config(bg="Black")
        self.ventanaOp.geometry("500x300")

        self.selectM1 = tk.StringVar(self.ventanaOp)


        operaciones = ["Union", "Intersección", "Diferencia", "Diferencia Simetrica"

        ]
        self.selectM1.set(operaciones[0])
        operaciones.pop(0)

        self.ComboboxOp = ttk.OptionMenu(self.ventanaOp, self.selectM1, self.selectM1.get(), *operaciones)
        self.ComboboxOp.config(width=20, height=1)
        self.ComboboxOp.grid(row=0, column=0, padx=20, pady=20)

        botonseleccionar = ttk.Button(self.ventanaOp, text="Seleccionar", command=lambda: self.seleccionarOperaciones())
        botonseleccionar.grid(row=0, column=3, padx=10, pady=20)


    def seleccionarOperaciones(self):
        self.ventanaOp.destroy()
        if self.selectM1.get() == "Rotación Horizontal":
            nueva = self.logicaMatrices.rotacionH(self.nomMatriz1)
        elif self.selectM1.get() == "Rotación Vertical":
            nueva = self.logicaMatrices.rotacionV(self.nomMatriz1)
        elif self.selectM1.get() == "Matriz Transpuesta" :
            nueva = self.logicaMatrices.Transpuesta(self.nomMatriz1)
        elif self.selectM1.get() == "Limpiar Zona":
            nueva = self.logicaMatrices.Limpiar(self.nomMatriz1, self.entradaTexto.get())
        elif self.selectM1.get() == "Agregar Linea Horizontal":
            nueva = self.logicaMatrices.LineaH(self.nomMatriz1,self.entradaTexto.get())
        elif self.selectM1.get() == "Agregar Linea Vertical":
            nueva = self.logicaMatrices.LineaH(self.nomMatriz1, self.entradaTexto.get())
        elif self.selectM1.get() == "Agregar Rectangulo":
            nueva = self.logicaMatrices.Rectangulo(self.nomMatriz1, self.entradaTexto.get())
        elif self.selectM1.get() == "Agregar Triangulo Rectangulo ":
            nueva = self.logicaMatrices.Triagulo(self.nomMatriz1, self.entradaTexto.get())
        elif self.selectM1.get() == "Union":
            nueva = self.logicaMatrices.Union(self.nomMatriz1, self.nomMatriz2)
        elif self.selectM1.get() == "Intersección":
            nueva = self.logicaMatrices.Intereseccion(self.nomMatriz1, self.nomMatriz2)
        elif self.selectM1.get() ==  "Diferencia":
            nueva = self.logicaMatrices.Diferencia(self.nomMatriz1, self.nomMatriz2)
        elif self.selectM1.get() ==  "Diferencia Simetrica":
            nueva = self.logicaMatrices.DiferenciaSimetrica(self.nomMatriz1, self.nomMatriz2)

        self.colocarResultados(nueva)


    def colocarResultados(self,nombre_result):

        varimagen = 'Imagenes/' + nombre_result + ".png"
        print(varimagen)
        self.labelMatriz3.destroy()
        imagen = Image.open(varimagen)
        imagen = imagen.resize((300, 300), Image.ANTIALIAS)
        imagenv2 = ImageTk.PhotoImage(imagen)
        self.labelMatriz3 = ttk.Label(self.panelV1, image=imagenv2)
        self.labelMatriz3.grid(row=1, column=2, padx=10, pady=20)
        self.labelMatriz3.image = imagenv2

    def generarReporte(self):
        self.logicaMatrices.generarReporte()




