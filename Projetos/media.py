from tkinter import*
from tkinter import messagebox
from centralizando import Centralizar
from componentes import Objetos

class App07:

    def __init__(self):
        super().__init__()

        self.root=Tk()

        Centralizar.posicionar(self,self.root,325,250)
        Objetos.tela(self,self.root,'App 07 - Python')
        
        Objetos.labels(self,self.root,'Valor 01',lx=0.215,ly=0.095,largura=0.125,altura=0.04)
        Objetos.labels(self,self.root,'Valor 02',lx=0.215,ly=0.245,largura=0.125,altura=0.04)
        Objetos.labels(self,self.root,'Média',lx=0.215,ly=0.405,largura=0.125,altura=0.04)
       

        Objetos.botoes(self,self.root,'Calcular',lx=0.215,ly=0.525,largura=0.62,altura=0.21,comando=self.calcular)
        Objetos.botoes(self,self.root,'Limpar',lx=0.215,ly=0.75,largura=0.62,altura=0.21,comando=self.limpar)

        self.textbox()

        self.root.mainloop()


        pass

    def textbox(self):

        self.txvalor01=Entry(self.root,bd=1,relief='solid')
        self.txvalor01.place(relx=0.365,rely=0.075,relwidth=0.4,relheight=0.075)

        self.txvalor02=Entry(self.root,bd=1,relief='solid')
        self.txvalor02.place(relx=0.365,rely=0.235,relwidth=0.4,relheight=0.075)

        self.txresultado=Entry(self.root,bd=1,relief='solid',state='disabled')
        self.txresultado.place(relx=0.365,rely=0.375,relwidth=0.4,relheight=0.075) 
        self.txvalor01.focus()               

        pass

    def calcular(self):
        
        if self.txvalor01.get().strip()=='' or self.txvalor02.get().strip()=='':

            messagebox.showwarning('Atenção','Favor preencher os campos!')
            self.txvalor01.focus()

        else:

            try:

                valor1=float(self.txvalor01.get())
                valor2=float(self.txvalor02.get())

                res=(valor1+valor2)/2

                self.txresultado['state']='normal'
                self.txresultado.insert(END,f'{res:.2f}')

                self.txresultado['state']='disabled'
                self.txvalor01.focus()

            except:

                messagebox.showerror('Erro','Dados inseridos são invalidos!')
                self.limpar(True)


        pass


    def limpar(self,status=False):

        if status==True:

            self.txresultado['state']='normal'

            self.txvalor01.delete(0,END)
            self.txvalor02.delete(0,END)
            self.txresultado.delete(0,END)

            self.txresultado['state']='disabled'
            self.txvalor01.focus()

        else:

            if self.txvalor01.get().strip()!='' or self.txvalor02.get().strip()!='' or self.txresultado.get().strip()!='':

                res=messagebox.askyesno('Pergunta','Deseja limpar os campos!')

                if res==True:

                    self.txresultado['state']='normal'

                    self.txvalor01.delete(0,END)
                    self.txvalor02.delete(0,END)
                    self.txresultado.delete(0,END)

                    self.txresultado['state']='disabled'
                    self.txvalor01.focus()                    


        pass


    pass


App07()