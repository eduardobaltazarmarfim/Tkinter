from os import system
from tkinter import*

system('cls')

class Objetos:

    def __init__(self):
     
        self.root=Tk()

        pass

    def tela(self,titulo,imagemico='Tkinter/Aplicações/Imagem/bussola.ico',cores=None,borda=None,tipoborda=None):

        self.root.title(titulo)
        self.root.iconbitmap(imagemico)

        self.root['bg']=cores
        self.root['bd']=borda
        self.root['relief']=tipoborda

        pass

    def botoes(self,master,titulo,lx=0,ly=0,largura=0,altura=0,comando=None,cores=None):

        self.root=master

        self.botao=Button(self.root,text=titulo,command=comando,bd=cores)
        self.botao.place(relx=lx,rely=ly,relwidth=largura,relheight=altura)

        pass

    def labels(self,master,titulo,lx=0,ly=0,largura=0,altura=0,cores=None,posicao=None):

        self.root=master

        self.nome=Label(self.root,text=titulo,bg=cores,justify=posicao)
        self.nome.place(relx=lx,rely=ly,relwidth=largura,relheight=altura)

        pass


    def caixaOpcao(self,master,titulo,variavel,valor,lx=0,ly=0,largura=0,altura=0,cores=None,selecionar=None):

        self.root=master
        
        self.opcoes=Radiobutton(self.root,text=titulo,variable=variavel,value=valor)
        self.opcoes.place(relx=lx,rely=ly,relwidth=largura,relheight=altura)

        if selecionar!=None:

            self.opcoes.select()

        pass
