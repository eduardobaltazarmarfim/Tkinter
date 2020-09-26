from tkinter import*
from tkinter import messagebox
from centralizarform import centralizando
from componentes import Objetos

class App10:

    def __init__(self):
        super().__init__()
        self.root=Tk()

        centralizando.posicionar(self,325,200,False)
        Objetos.tela(self,'App 10 - Python')
        
        Objetos.botoes(self,self.root,'Converter',lx=0.1,ly=0.65,largura=0.4,altura=0.22,comando=self.calcular)
        Objetos.botoes(self,self.root,'Limpar',lx=0.515,ly=0.65,largura=0.4,altura=0.22,comando=self.limpar)

        Objetos.labels(self,self.root,'Valor em Real',lx=0.1,ly=0.145,largura=0.22,altura=0.12)
        Objetos.labels(self,self.root,'Dolar',lx=0.1,ly=0.315,largura=0.22,altura=0.12,lz=E)
        Objetos.labels(self,self.root,'Valor Convertido',lx=0.035,ly=0.475,largura=0.65,altura=0.12,lz=W)

        self.textbox()

        self.root.mainloop()

        pass

    def textbox(self):

        self.txval1=Entry(self.root,bd=0.5,relief='solid')
        self.txval1.place(relx=0.335,rely=0.155,relwidth=0.5,relheight=0.085)

        self.txval2=Entry(self.root,bd=0.5,relief='solid')
        self.txval2.place(relx=0.335,rely=0.325,relwidth=0.5,relheight=0.085)

        self.txval3=Entry(self.root,bd=0.5,relief='solid',state='disabled')
        self.txval3.place(relx=0.335,rely=0.485,relwidth=0.5,relheight=0.085)

        self.txval1.focus()

        pass

    def limpar(self):

        self.txval1.delete(0,END)
        self.txval2.delete(0,END)
        self.txval3.delete(0,END)
        self.txval1.focus()
        self.txval3['state']='disabled'

        pass

    def calcular(self):

        try:

            if self.txval1.get().strip()=='' or self.txval2.get().strip()=='':

                messagebox.showwarning('Atenção','Favor preencher os campos!')
                self.txval1.focus()

            else:

                val1=float(self.txval1.get().replace(',','.'))
                val2=float(self.txval2.get().replace(',','.'))

                res=val1/val2

                self.txval3['state']='normal'
                self.txval3.insert(INSERT,f'US${res:.2f}')
                self.txval1.focus()
                

        except:

            messagebox.showerror('Erro','Dados inseridos são invalidos!')
            self.limpar()

        pass

    pass

App10()