from tkinter import*
from tkinter import messagebox
from centralizando import Centralizar
from componentes import Objetos
from tkinter.scrolledtext import ScrolledText

class App04:

    def __init__(self):
        super().__init__()

        self.root=Tk()

        Centralizar.posicionar(self,self.root,650,300,False)
        Objetos.tela(self,self.root,'App 04 - Python')

        Objetos.labels(self,self.root,'Digite um texto',lx=0.045,ly=0.115,largura=0.22,altura=0.125)
        Objetos.botoes(self,self.root,'Analisar',lx=0.085,ly=0.45,largura=0.295,altura=0.165,comando=lambda:self.analisar(self.txfrase.get()))
        Objetos.botoes(self,self.root,'Limpar',lx=0.085,ly=0.653,largura=0.295,altura=0.165,comando=self.limpar)

        self.textbox()

        self.root.mainloop()


        pass

    def analisar(self,valor):

        if self.txfrase.get().strip()=='':

            messagebox.showwarning('Atenção','Favor preencher o campo!')
            self.txfrase.focus()

        else:

            resp=f'.Qual é o tipo {type(valor)}\n.É um número {valor.isnumeric()}\n.É alfabético {valor.isalpha()}\n.É alfanúmerico {valor.isalnum()}\n.Está em maisucula {valor.isupper()}\n.Está em minusculula {valor.islower()}\n.Está capitalizada {valor.istitle()}'

            self.txdados['state']='normal'
            self.txdados.insert(END,resp)
            self.txdados['state']='disabled'

        pass

    def limpar(self):

        if self.txfrase.get().strip()!='' or self.txdados.get().strip()!='':

            res=messagebox.askokcancel('Pergunta','Deseja limpar os campos!')
            
            if res==True:

                self.txfrase.delete(0,END)
                self.txdados['state']='normal'
                self.txdados.delete('1.0',END)
                self.txdados['state']='disabled'

        pass


    def textbox(self):

        self.txfrase=Entry(self.root,bd=1,relief='solid')
        self.txfrase.place(relx=0.085,rely=0.245,relwidth=0.295,relheight=0.065)

        self.txdados=ScrolledText(self.root,bd=1,relief='solid')
        self.txdados.place(relx=0.45,rely=0,relwidth=0.55,relheight=1)
        self.txdados['state']='disabled'
        self.txfrase.focus()

        pass


    pass


App04()