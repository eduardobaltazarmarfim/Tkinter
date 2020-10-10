from tkinter import*
from tkinter import messagebox
from centralizando import Centralizar
from componentes import Objetos


class App06:

    def __init__(self):
        super().__init__()

        self.root=Tk()

        Centralizar.posicionar(self,self.root,325,420,False)
        Objetos.tela(self,self.root,'App 06 - Python')

        Objetos.botoes(self,self.root,'Calcular',lx=0.215,ly=0.6,largura=0.56,altura=0.125,comando=self.calcular)
        Objetos.botoes(self,self.root,'Limpar',lx=0.215,ly=0.75,largura=0.56,altura=0.125,comando=self.limpar)

        Objetos.labels(self,self.root,'Valor',lx=0.175,ly=0.035,largura=0.125,altura=0.125)
        Objetos.labels(self,self.root,'Dobro',lx=0.175,ly=0.155,largura=0.125,altura=0.125)
        Objetos.labels(self,self.root,'Triplo',lx=0.175,ly=0.295,largura=0.125,altura=0.125)
        Objetos.labels(self,self.root,'Raiz',lx=0.175,ly=0.435,largura=0.125,altura=0.125)
        
        self.textbox()

        self.root.mainloop()


        pass

    def textbox(self):

        self.txvalor=Entry(self.root,bd=1,relief='solid')
        self.txvalor.place(relx=0.295,rely=0.075,relwidth=0.425,relheight=0.045)

        self.txdobro=Entry(self.root,bd=1,relief='solid')
        self.txdobro.place(relx=0.295,rely=0.195,relwidth=0.425,relheight=0.045)

        self.txtriplo=Entry(self.root,bd=1,relief='solid')
        self.txtriplo.place(relx=0.295,rely=0.33,relwidth=0.425,relheight=0.045)  

        self.txraiz=Entry(self.root,bd=1,relief='solid')
        self.txraiz.place(relx=0.295,rely=0.472,relwidth=0.425,relheight=0.045)

        self.txdobro['state']='disabled'
        self.txraiz['state']='disabled'
        self.txtriplo['state']='disabled'
        self.txvalor.focus()            

        pass

    def calcular(self):

        if self.txvalor.get()=='':

            messagebox.showwarning('Atenção','Favor preencher o campo em questão!')
            self.txvalor.focus()

        else:

            try:

                valor=int(self.txvalor.get())
                
                dobro=valor*2
                triplo=valor*3
                raiz=valor**(1/2)

                self.txraiz['state']='normal'
                self.txdobro['state']='normal'
                self.txtriplo['state']='normal'

                self.txdobro.insert(END,f'{dobro}')
                self.txtriplo.insert(END,f'{triplo}')
                self.txraiz.insert(END,f'{raiz:.2f}')

                self.txraiz['state']='disabled'
                self.txdobro['state']='disabled'
                self.txtriplo['state']='disabled'
                self.txvalor.focus()              

            except:

                messagebox.showerror('Erro','Dados inseridos são invalidos!')
                self.limpar(True)

        pass

    def limpar(self,status=False):

        if status==True:
            
            self.txdobro['state']='normal'
            self.txraiz['state']='normal'
            self.txtriplo['state']='normal'
            
            self.txvalor.delete(0,END)
            self.txtriplo.delete(0,END)
            self.txraiz.delete(0,END)
            self.txdobro.delete(0,END)

            self.txdobro['state']='disabled'
            self.txraiz['state']='disabled'
            self.txtriplo['state']='disabled'
            self.txvalor.focus()

        else:

            if self.txdobro.get().strip()!='' or self.txraiz.get().strip()!='' or self.txtriplo.get().strip()!='' or self.txvalor.get().strip()!='':

                res=messagebox.askquestion('Pergunta','Deseja limpar os campos!')

                if res=='yes':

                    self.txdobro['state']='normal'
                    self.txraiz['state']='normal'
                    self.txtriplo['state']='normal'
                    
                    self.txvalor.delete(0,END)
                    self.txtriplo.delete(0,END)
                    self.txraiz.delete(0,END)
                    self.txdobro.delete(0,END)

                    self.txdobro['state']='disabled'
                    self.txraiz['state']='disabled'
                    self.txtriplo['state']='disabled'
                    self.txvalor.focus()

        pass


    pass


App06()