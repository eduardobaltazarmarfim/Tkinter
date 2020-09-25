from tkinter import*
from tkinter import messagebox
from centralizarform import centralizando
from componentes import Objetos

class App03:

    def __init__(self):
        super().__init__()

        self.root=Tk()

        centralizando.posicionar(self,350,220,False)
        Objetos.tela(self,'App 03 - Python')
        Objetos.labels(self,'Valor 01',lx=0.15,ly=0.15,largura=0.15,altura=0.1)
        Objetos.labels(self,'Valor 02',lx=0.15,ly=0.30,largura=0.15,altura=0.1)
        Objetos.labels(self,'Resultado',lx=0.15,ly=0.45,largura=0.15,altura=0.1)

        Objetos.botoes(self,'Calcular',lx=0.09,ly=0.65,largura=0.4,altura=0.18,comando=lambda:self.calcular(self.val1.get(),self.val2.get()))
        Objetos.botoes(self,'Limpar',lx=0.52,ly=0.65,largura=0.4,altura=0.18,comando=lambda:self.limpar(self.val1.get(),self.val2.get(),self.res.get()))

        self.textbox()

        self.root.mainloop()

        pass

    def textbox(self):

        self.val1=Entry(self.root,bd=0.5,relief='solid')
        self.val2=Entry(self.root,bd=0.5,relief='solid')
        self.res=Entry(self.root,bd=0.5,relief='solid')

        self.val1.place(relx=0.35,rely=0.15,relwidth=0.45,relheight=0.09)
        self.val2.place(relx=0.35,rely=0.30,relwidth=0.45,relheight=0.09)
        self.res.place(relx=0.35,rely=0.45,relwidth=0.45,relheight=0.09)

        self.res.config(state='disabled')

        self.val1.focus()    

        pass

    def calcular(self,val01,val02):
                        
        if val01=='' or val02=='':

            messagebox.showerror('Atenção','Favor preencher os campos informados!')
            self.val1.focus()

        else:

            if val01.isnumeric() and val02.isnumeric():

                self.res.config(state='normal')
                self.res.delete(0,END)

                val01=float(val01)
                val02=float(val02)

                res=val01+val02

                self.res.insert(END,f'{res:.2f}')

            else:

                messagebox.showwarning('Atenção','Dados inseridos são invalidos!')
                self.limpar(val01,val02,self.res,True)

        pass

    def limpar(self,val01,val02,res,corte=False):

        if corte==False:

            if val01=='' and val02=='' and res=='':

                self.val1.delete(0,END)
                self.val2.delete(0,END)
                self.res.delete(0,END)

            else:

                resp=messagebox.askyesno('Pergunta','Deseja limpar os campos!')

                if resp==True:

                    self.val1.delete(0,END)
                    self.val2.delete(0,END)
                    self.res.delete(0,END)

                    self.val1.focus()
                    self.res['state']='disabled'

        else:

            self.val1.delete(0,END)
            self.val2.delete(0,END)
            self.res.delete(0,END)

            self.val1.focus()
            self.res['state']='disabled'                

        pass

    pass

App03()