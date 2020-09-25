from tkinter import*

class centralizando:

    def __init__(self):

        self.root=Tk()

        pass

    def posicionar(self,largura,altura,responsivo=True):

        largura_tela=self.root.winfo_screenwidth()
        altura_tela=self.root.winfo_screenheight()

        posx=(largura_tela/2)-(largura/2)
        posy=(altura_tela/2)-(altura/2)

        self.root.geometry('%dx%d+%d+%d' %(largura,altura,posx,posy))

        self.root.resizable(responsivo,responsivo)

        pass


    pass