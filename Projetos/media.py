from tkinter import*
from centralizarform import centralizando
from componentes import Objetos
from tkinter import messagebox

class App07:

    def __init__(self):
        super().__init__()

        self.root=Tk()

        centralizando.posicionar(self,400,250,False)
        Objetos.tela(self,'App 07 - Python')
        Objetos.botoes(self,self.root,'Calcular',lx=0.125,ly=0.7,largura=0.35,altura=0.18,comando=self.calcular)
        Objetos.botoes(self,self.root,'Limpar',lx=0.525,ly=0.7,largura=0.35,altura=0.18,comando=self.limpar)

        Objetos.labels(self,self.root,'Digite o valor 1',lx=0.15,ly=0.03,largura=0.4,altura=0.12)
        Objetos.labels(self,self.root,'Digite o valor 2',lx=0.15,ly=0.215,largura=0.4,altura=0.12)
        Objetos.labels(self,self.root,'Média das Notas',lx=0.15,ly=0.425,largura=0.425,altura=0.12)

        self.textbox()

        self.root.mainloop()

        pass

    def textbox(self):

        self.val1=Entry(self.root,bd=0.5,relief='solid')
        self.val1.place(relx=0.25,rely=0.145,relwidth=0.5,relheight=0.07)

        self.val2=Entry(self.root,bd=0.5,relief='solid')
        self.val2.place(relx=0.25,rely=0.325,relwidth=0.5,relheight=0.07)

        self.val3=Entry(self.root,bd=0.5,relief='solid')
        self.val3.place(relx=0.25,rely=0.525,relwidth=0.5,relheight=0.07)

        self.val3['state']='disabled'
        self.val1.focus()

        pass

    def limpar(self):

        self.val1.delete(0,END)
        self.val2.delete(0,END)
        self.val3.delete(0,END)
        self.val3['state']='disabled'
        self.val1.focus()

        pass

    def calcular(self):

        try:

            if self.val1.get().strip()=='' or self.val2.get().strip()=='':

                messagebox.showwarning('Atenção','Favor preencher todos os campos!')
                self.val1.focus()

            else:
                               

                val01=float(self.val1.get())
                val02=float(self.val2.get())
                media=(val01+val02)/2
                
                self.val3['state']='normal'
                self.val3.delete(0,END)
                self.val3.insert(0,f'{media:.2f}')
                self.val1.focus()

        except:

            messagebox.showerro('Erro','Valor digitado é invalido!')

        pass

    pass

App07()