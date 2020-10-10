from tkinter import*
from tkinter import messagebox
from Modulos.centralizando import Centralizar
from Modulos.componentes import Objetos


class App06:

    def __init__(self):
        super().__init__()

        self.root=Tk()

        Centralizar.posicionar(self,self.root,300,200,False)

        self.root.mainloop()


        pass



    pass


App06()