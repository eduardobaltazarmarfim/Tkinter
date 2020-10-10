from tkinter import *
from tkinter import messagebox
from Modulos.centralizando import Centralizar
from Modulos.componentes import Objetos

class App03:

    def __init__(self):
        super().__init__()

        self.root=Tk()

        Centralizar.posicionar(self,self.root,350,400,False)
        Objetos.tela(self,self.root,'App 03 - Python')

        self.frame01=Frame(self.root,bd=1,relief='solid')
        self.frame01.place(relx=0.145,rely=0.025,relwidth=0.75,relheight=0.55)

        Objetos.botoes(self,self.root,'Calcular',lx=0.255,ly=0.65,largura=0.45,altura=0.125,comando=lambda:self.calcular(self,self.txval01.get(),self.txval02.get()))
        Objetos.botoes(self,self.root,'Limpar',lx=0.255,ly=0.825,largura=0.45,altura=0.125,comando=self.limpar)

        Objetos.labels(self,self.frame01,'Digite Valor 01',lx=0.01,ly=0.195,largura=0.45,altura=0.12)
        Objetos.labels(self,self.frame01,'Digite Valor 02',lx=0.01,ly=0.425,largura=0.45,altura=0.12)
        Objetos.labels(self,self.frame01,'Resultado',lx=0.015,ly=0.65,largura=0.365,altura=0.12)
        
        self.textbox()
                
        self.root.mainloop()


        pass


    def textbox(self):

        self.txval01=Entry(self.frame01,bd=1,relief='solid')
        self.txval02=Entry(self.frame01,bd=1,relief='solid')
        self.txresultado=Entry(self.frame01,bd=1,relief='solid')

        self.txval01.place(relx=0.1,rely=0.335,relwidth=0.75,relheight=0.085)
        self.txval02.place(relx=0.1,rely=0.555,relwidth=0.75,relheight=0.085)
        self.txresultado.place(relx=0.1,rely=0.77,relwidth=0.75,relheight=0.085)
        self.txresultado['state']='disabled'

        self.txval01.focus()

        pass

    def calcular(self,valor1,valor2,res=None,status=False):

        if self.txval01.get().strip()=='' or self.txval02.get().strip()=='':

            messagebox.showwarning('Atenção','Favor preencher todos os campos!')

        else:

            try:

                valor1=float(self.txval01.get().replace(',','.'))
                valor2=float(self.txval02.get().replace(',','.'))

                res=valor1+valor2

                self.txresultado['state']='normal'
                self.txresultado.insert(END,f'{res:.2f}')
                self.txresultado['state']='disabled'

            except:

                messagebox.showerror('Erro','Dados inseridos são invalidos')
                self.limpar()            

        pass


    def limpar(self):

        self.txval01.delete(0,END)
        self.txval02.delete(0,END)
        self.txresultado['state']='normal'
        self.txresultado.delete(0,END)
        self.txresultado['state']='disabled'
        self.txval01.focus()

        pass


    pass


App03()