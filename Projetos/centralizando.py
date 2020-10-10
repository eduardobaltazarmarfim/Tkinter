from tkinter import*
from os import system

system('cls')

class Centralizar:


    def __init__(self):
        super().__init__()

        self.root=Tk()

        self.posicionar()

        pass


    def posicionar(self,tela,largura=None,altura=None,responsivo=True):
        
        self.root=tela

        largura_tela=self.root.winfo_screenwidth()
        altura_tela=self.root.winfo_screenheight()

        posx=(largura_tela/2)-(largura/2)
        posy=(altura_tela/2)-(altura/2)


        self.root.geometry('%dx%d+%d+%d'%(largura,altura,posx,posy))
        self.root.resizable(responsivo,responsivo)

        pass


    pass
