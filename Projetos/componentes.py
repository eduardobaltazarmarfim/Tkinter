from tkinter import*

class Objetos:

    def __init__(self):
        super().__init__()

        self.root=Tk()

        self.tela()
        self.botoes()
        self.labels()

        pass
        
    def tela(self,tela,titulo=None,imagem='Aplicações/Imagem/bussola.ico',cor=None,fonte=None,linha=None,borda=None):

        self.root=tela

        self.root.title(titulo)
        self.root.iconbitmap(imagem)
        self.root['bg']=cor
        self.root['font']=fonte
        self.root['bd']=linha
        self.root['relief']=borda

        pass

    def labels(self,tela,texto=None,cor=None,lx=None,ly=None,largura=None,altura=None):
        
        self.root=tela

        self.labels=Label(self.root,text=texto)
        self.labels['bg']=cor

        self.labels.place(relx=lx,rely=ly,relwidth=largura,relheight=altura)

        pass

    def botoes(self,tela,texto=None,comando=None,cor=None,lx=None,ly=None,largura=None,altura=None,status='normal'):

        self.root=tela

        self.botao=Button(self.root,text=texto,command=comando)
        self.botao['bg']=cor

        self.botao.place(relx=lx,rely=ly,relwidth=largura,relheight=altura)

        self.botao['state']=status

        pass

    pass