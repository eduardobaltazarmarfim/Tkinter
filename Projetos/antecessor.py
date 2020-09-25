from tkinter import *
from centralizarform import centralizando
from componentes import Objetos
from tkinter import messagebox

class App05:

    def __init__(self):
        super().__init__()
        self.root=Tk()

        centralizando.posicionar(self,350,450,False)

        Objetos.tela(self,'App 05 - Python')
        Objetos.botoes(self,self.root,'Click',lx=0.29,ly=0.55,largura=0.45,altura=0.12,comando=self.analisar)
        Objetos.botoes(self,self.root,'Limpar',lx=0.29,ly=0.70,largura=0.45,altura=0.12,comando=self.limpar)
        Objetos.labels(self,self.root,'Digite um número:',lx=0.165,ly=0.12,largura=0.35,altura=0.07)
        Objetos.labels(self,self.root,'Antecessor:',lx=0.165,ly=0.22,largura=0.25,altura=0.07)
        Objetos.labels(self,self.root,'Sucessor:',lx=0.155,ly=0.32,largura=0.25,altura=0.07)

        self.textbox()

        self.root.mainloop()

        pass

    def textbox(self):

        self.valor=Entry(self.root,bd=0.5,relief='solid')
        self.valor.place(relx=0.2,rely=0.175,relwidth=0.65,relheight=0.05)

        self.valor1=Entry(self.root,bd=0.5,relief='solid',state='disabled')
        self.valor1.place(relx=0.2,rely=0.275,relwidth=0.65,relheight=0.05)

        self.valor2=Entry(self.root,bd=0.5,relief='solid',state='disabled')
        self.valor2.place(relx=0.2,rely=0.375,relwidth=0.65,relheight=0.05)

        self.valor.focus()

        pass

    
    def analisar(self):

        try:
            
            num=int(self.valor.get())
                       

            if num<=0:

                messagebox.showwarning('Atenção','Você não pode digitar valor menor ou igual à 0.')
                self.valor.delete(0,END)
                self.valor.focus()

            else:

                antecessor=num-1
                Sucessor=num+1

                self.valor1['state']='normal'
                self.valor2['state']='normal'

                self.valor1.insert(INSERT,f'{antecessor}')
                self.valor2.insert(INSERT,f'{Sucessor}')

        except:

            messagebox.showerror('Erro','Dados inseridos são invalidos')
            self.valor.delete(0,END)
            self.valor.focus()

        pass

    def limpar(self):

        self.valor.delete(0,END)
        self.valor1.delete(0,END)
        self.valor2.delete(0,END)

        self.valor1['state']='disabled'
        self.valor2['state']='disabled'

        pass


    pass

App05()