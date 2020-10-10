from tkinter import *
from tkinter import messagebox
from centralizando import Centralizar
from componentes import Objetos


class App02:


    def __init__(self):
        super().__init__()

        self.root=Tk()

        Centralizar.posicionar(self,self.root,300,400,False)
        Objetos.tela(self,self.root,'App 02 - Python')

        Objetos.botoes(self,self.root,'Mensagem',lx=0.285,ly=0.6,largura=0.5,altura=0.15,comando=lambda:self.mensagem(self.txnome.get()))
        Objetos.botoes(self,self.root,'Limpar',lx=0.285,ly=0.785,largura=0.5,altura=0.15,comando=lambda:self.limpar(self.txnome.get()))

        Objetos.labels(self,self.root,'Digite seu Nome',lx=0.285,ly=0.15,largura=0.35,altura=0.12)

        self.textbox()

        self.root.mainloop()


        pass

    def textbox(self):

        self.txnome=Entry(self.root,bd=1,relief='solid')
        self.txnome.place(relx=0.295,rely=0.235,relwidth=0.5,relheight=0.05)
        self.txnome.focus()

        pass

    def mensagem(self,nome):

        if nome.strip()=='':

            messagebox.showwarning('Atenção','Favor preencher o campo!')
            self.txnome.focus()

        else:

            messagebox.showinfo('OK',f'Seja bem vindo {nome.title()}!')

        pass


    def limpar(self,nome):

        if nome.strip()=='':

            self.txnome.delete(0,END)
            self.txnome.focus()

        else:

            resp=messagebox.askquestion('Pergunta','Deseja limpar os campos!')

            if resp=='yes':

                self.txnome.delete(0,END)
                self.txnome.focus()
            
        pass


    pass


App02()