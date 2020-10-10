from tkinter import *
from tkinter import messagebox
from centralizando import Centralizar
from componentes import Objetos

class App01:

    def __init__(self):
        super().__init__()

        self.root=Tk()

        Centralizar.posicionar(self,self.root,300,200,False)
        Objetos.tela(self,self.root,'App 01 - Python')
        Objetos.botoes(self,self.root,'Mensagem',lx=0.30,ly=0.35,largura=0.45,altura=0.25,comando=self.mensagem)

        self.root.mainloop()


        pass


    def mensagem(self):

        messagebox.showinfo('Mensagem','Hello World!')

        pass


    pass


App01()