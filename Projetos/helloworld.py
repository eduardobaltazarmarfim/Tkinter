from tkinter import*
from centralizarform import centralizando
from componentes import Objetos
from tkinter import messagebox

class App01:

    def __init__(self):
        super().__init__()
        self.root=Tk()
        
        caminho='Aplicações/Imagem/bussola.ico'

        centralizando.posicionar(self,300,200,False)
        Objetos.tela(self,'App 01 - Python',imagemico=caminho)
        Objetos.botoes(self,'Mensagem',lx=0.325,ly=0.35,largura=0.4,altura=0.22,comando=self.Mensagem)

        self.root.mainloop()

        pass

    def Mensagem(self):

        messagebox.showinfo('Mensagem','Hello World!')

        pass

    pass


App01()