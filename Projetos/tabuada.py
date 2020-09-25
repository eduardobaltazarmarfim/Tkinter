from tkinter import*
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from centralizarform import centralizando
from componentes import Objetos

class App09:

    def __init__(self):
        super().__init__()

        self.root=Tk()

        centralizando.posicionar(self,600,300,False)
        Objetos.tela(self,'App 09 - Python')

        self.frame1=Frame(self.root,bd=0.5,relief='solid')
        self.frame1.place(relx=0.02,rely=0.02,relwidth=0.5,relheight=0.97)

        self.frame2=Frame(self.root,bd=0.5,relief='solid')
        self.frame2.place(relx=0.525,rely=0.02,relwidth=0.465,relheight=0.97)

        Objetos.botoes(self,self.frame1,'Tabuada',lx=0.295,ly=0.575,largura=0.5,altura=0.165,comando=self.tabuada)
        Objetos.botoes(self,self.frame1,'Cancelar',lx=0.295,ly=0.75,largura=0.5,altura=0.165,comando=self.limpar)

        Objetos.labels(self,self.frame1,'Digite um valor',lx=0.265,ly=0.255,largura=0.4,altura=0.12)

        self.textbox()   

        self.root.mainloop()

        pass

    def textbox(self):

        self.multexto=ScrolledText(self.frame2,font='Tahoma 12')
        self.multexto.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.multexto['state']='disabled'

        self.txvalor=Entry(self.frame1,bd=0.5,relief='solid')
        self.txvalor.place(relx=0.325,rely=0.358,relwidth=0.45,relheight=0.065)

        pass

    def tabuada(self):

        try:

            if self.txvalor.get().strip()=='':

                messagebox.showwarning('Atenção','Favor preencher o campo!')
                self.limpar()

            else:

                num=int(self.txvalor.get())

                self.multexto['state']='normal'
                            
                for i in range(0,11):

                    res=i*num
                    self.multexto.insert(END,f'{i:^2}{" x ":<2}{num:^2}{" = ":^2}{res:^2}\n')                 

        except:

            messagebox.showerror('Erro','Dados inseridos são invalidos!')
            self.limpar()
          

        pass

    def limpar(self):

        self.txvalor.delete(0,END)
        self.multexto.delete('1.0',END)
        self.multexto['state']='disabled'
        self.txvalor.focus()

        pass

    pass

App09()