from tkinter import *
from tkinter import filedialog
from time import sleep
from ClaseLogica import Logica




class InterfazP:
    logicaMatrices = Logica()
    ventana = None
    carga = None
    def iniciar(self):
        self.ventana = Tk()
        self.ventana.title("Ventana Principal")
        self.ventana.resizable(True, True)

        panel = Frame()
        panel.pack()



        botonCarga = Button(panel, text = "CargarArchivo", command = lambda:self.cargaArchivo())
        botonCarga.grid(row = 0, column = 0)

        botonOperaciones = Button(panel, text= "Operaciones")
        botonOperaciones.grid(row = 0, column = 1)

        botonReportes = Button(panel, text= "Reportes")
        botonReportes.grid(row = 0, column = 2)

        botonAyuda = Button(panel, text = "Ayuda")
        botonAyuda.grid(row= 0, column = 3)

        #imagen1 = PhotoImage(file= "P1.png")

        #imagen1 = imagen1.subsample(3,3)
        labelMatriz1 = Label(panel, )
        labelMatriz1.config(bg = "Black",width = "20", height = "10")
        labelMatriz1.grid(row = 1, column = 0, padx = 10, pady = 20)

        labelMatriz2 = Label(panel)


        print("algo")
        self.ventana.mainloop()

    def cambiaEstadoVentanaCarga(self):
        self.cargaArchivo()



    def cargaArchivo(self):
        ruta = Toplevel(self.ventana)
        ruta.filename = filedialog.askopenfilename(filetypes=(("XML files", "*.xml"), ("all files", "*.*")))
        file = open(ruta.filename, "r", encoding='utf-8')

        # file = 'C:/Users/emayo/OneDrive/Desktop/IPC2-Proyecto1-201901758/Matriz2.xml'

        print(file)
        ruta.destroy()
        self.logicaMatrices.almacenaDatos(file)




