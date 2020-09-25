from tkinter import*
from tkinter import messagebox
from centralizarform import centralizando
from componentes import Objetos


class App06:

    def __init__(self):
        super().__init__()
        self.root=Tk()

        centralizando.posicionar(self,450,250,False)
        Objetos.tela(self,'App 06 - Python')
        
        self.textbox()

        self.fram01=Frame(self.root,bd=0.5,relief='solid')
        self.fram01.place(relx=0.02,rely=0.09,relwidth=0.3,relheight=0.8)

        Objetos.botoes(self,self.root,'Calcular',lx=0.35,ly=0.7,largura=0.295,altura=0.18,comando=lambda:self.calcular(valOpcao.get()))
        Objetos.botoes(self,self.root,'Limpar',lx=0.665,ly=0.7,largura=0.295,altura=0.18,comando=self.limpar)

        Objetos.labels(self,self.root,'Digite um Valor:',lx=0.345,ly=0.17,largura=0.2,altura=0.06)
        Objetos.labels(self,self.root,'Resultado:',lx=0.32,ly=0.39,largura=0.2,altura=0.06)

        valOpcao=IntVar()
    
        Objetos.caixaOpcao(self,self.fram01,titulo='Dobro',variavel=valOpcao,valor=1,lx=0.02,ly=0.1,largura=0.5,altura=0.25,selecionar=1)
        Objetos.caixaOpcao(self,self.fram01,titulo='Triplo',variavel=valOpcao,valor=2,lx=0.02,ly=0.25,largura=0.5,altura=0.25)
        Objetos.caixaOpcao(self,self.fram01,titulo='Raiz Quadrada',variavel=valOpcao,valor=3,lx=0.05,ly=0.4,largura=0.78,altura=0.25)

                    
        self.root.mainloop()

        pass


    def textbox(self):

        self.txvalor=Entry(self.root,bd=0.5,relief='solid')
        self.txvalor.place(relx=0.35,rely=0.25,relwidth=0.6,relheight=0.07)

        self.txres=Entry(self.root,bd=0.5,relief='solid')
        self.txres.place(relx=0.35,rely=0.45,relwidth=0.6,relheight=0.07)

        self.txres['state']='disabled'
        self.txvalor.focus()

        pass

    def calcular(self,val):

        try:
                   
            if val==0 or self.txvalor.get().strip()=='':

                messagebox.showwarning('Atenção','Informar os dados para calculo!')
                self.txvalor.focus()

            else:

                num=float(self.txvalor.get())

                if val==1:

                    calc=num*2

                elif val==2:

                    calc=num*3

                elif val==3:

                    calc=num**(1/2)


                self.txres['state']='normal'
                self.txres.delete(0,END)
                self.txres.insert(INSERT,f'{calc:.2f}')

        except:

            messagebox.showerror('Erro','Dados inseridos são invalidos!')
            self.txvalor.focus()

                
        pass

    def limpar(self):

        self.txvalor.delete(0,END)
        self.txres.delete(0,END)
        self.txres['state']='disabled'
        
        pass

    pass


App06()