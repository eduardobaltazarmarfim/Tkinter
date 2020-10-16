from tkinter import*
from tkinter import messagebox
from centralizando import Centralizar
from componentes import Objetos
from tkinter.scrolledtext import ScrolledText


class App09:

    def __init__(self):
        super().__init__()
                        
        self.root=Tk()

        Centralizar.posicionar(self,self.root,600,300,False)
        Objetos.tela(self,self.root,'App 09 - Python')

        self.frame01=Frame(self.root,bd=1,relief='solid')
        self.frame01.place(relx=0.03,rely=0.05,relwidth=0.35,relheight=0.90)

        self.textbox()

        Objetos.labels(self,self.frame01,'Digite um Valor',lx=0.105,ly=0.295,largura=0.55,altura=0.1)

        Objetos.botoes(self,self.frame01,'Calcular',lx=0.185,ly=0.63,largura=0.65,altura=0.15,comando=self.tabuada)
        Objetos.botoes(self,self.frame01,'Limpar',lx=0.185,ly=0.795,largura=0.65,altura=0.15,comando=self.limpar)

        
        self.root.mainloop()


        pass

    
    def textbox(self):

        self.txvalor=Entry(self.frame01,bd=1,relief='solid')
        self.txtabuada=ScrolledText(self.root,bd=1,relief='solid',font='2')

        self.txvalor.place(relx=0.185,rely=0.395,relwidth=0.65,relheight=0.075)
        self.txtabuada.place(relx=0.405,rely=0.05,relwidth=0.575,relheight=0.9)

        self.txtabuada['state']='disabled'
        self.txvalor.focus()
        
        pass


    def tabuada(self):

        if self.txvalor.get().strip()=='':

            messagebox.showwarning('Atenção','Favor preencher o campo!')
            self.txvalor.focus()

        else:

            try:

                num=int(self.txvalor.get())
                
            except:

                messagebox.showerror('Erro','Dados inseridos são invalidos!')
                self.limpar(True)

            finally:
                
                self.txtabuada['state']='normal'
                
                for i in range(0,11):
                    
                    res=num*i

                    if i<10:
                    
                        self.txtabuada.insert(END,f'{i}x{num}={res}\n')

                    else:

                        self.txtabuada.insert(END,f'{i}x{num}={res}\nFIM')


                self.txtabuada['state']='disabled'
                          

        pass


    def limpar(self,status=False):

        if status==True:

            self.txtabuada['state']='normal'
            self.txtabuada.delete('1.0',END)
            self.txtabuada['state']='disabled'
            self.txvalor.delete(0,END)
            self.txvalor.focus()

        else:

            if self.txvalor.get().strip()!='' or self.txtabuada.get().strip()!='':

                resp=messagebox.askquestion('Pergunta','Deseja limpar os campos!')

                if resp=='yes':

                    self.txtabuada['state']='normal'
                    self.txtabuada.delete('1.0',END)
                    self.txtabuada['state']='disabled'

                    self.txvalor.delete(0,END)

                    self.txvalor.focus()


    pass


App09()