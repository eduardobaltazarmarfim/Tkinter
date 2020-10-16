from tkinter import*
from centralizando import Centralizar
from componentes import Objetos
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText


class App08:

    def __init__(self):
        super().__init__()

        self.root=Tk()

        Centralizar.posicionar(self,self.root,600,300,False)
        Objetos.tela(self,self.root,'App 08 - Python')
        
        Objetos.botoes(self,self.root,'Analisar',lx=0.05,ly=0.585,largura=0.25,altura=0.15,comando=self.analisar)
        Objetos.botoes(self,self.root,'Limpar',lx=0.05,ly=0.765,largura=0.25,altura=0.15,comando=self.limpar)

        Objetos.labels(self,self.root,'Digite um Valor',lx=0.045,ly=0.225,largura=0.15,altura=0.15)
        

        self.textbox()

        self.root.mainloop()


        pass


    def textbox(self):

        self.txvalor=Entry(self.root,bd=1,relief='solid')
        self.txvalor.place(relx=0.05,rely=0.335,relwidth=0.25,relheight=0.065)

        self.txdados=ScrolledText(self.root,bd=1,relief='solid')
        self.txdados.place(relx=0.45,rely=0,relwidth=0.535,relheight=1)

        self.txdados['state']='disabled'
        self.txvalor.focus()       

        pass


    def analisar(self):

        if self.txvalor.get().strip()=='':

            messagebox.showwarning('Atenção','Favor preencher o campo!')
            self.txvalor.focus()

        else:

            try:
                
                num=float(self.txvalor.get().replace(',','.'))
                
                mm=num*10
                km=num/1000000
                dam=num/1000
                m=num/100
                dm=num/10


                self.txdados['state']='normal'
                self.txdados.insert(END,f'O valor de {num} convertido em:\n.Milímetro: {mm}\n.Quilômetro: {km}\n.Decametro: {dam}\n.Metro: {m}\n.Decimetro: {dm:.2f}')

            except:

                messagebox.showerror('Erro','Dados inseridos são invalidos')
                self.limpar(True)

        pass


    def limpar(self,status=False):

        if status==True:
            
            self.txdados['state']='normal'

            self.txvalor.delete(0,END)
            self.txdados.delete('1.0',END)
            self.txvalor.focus()

            self.txdados['state']='disabled'

        else:

            if self.txvalor.get().strip()!='' or self.txdados.get().strip()!='':

                resp=messagebox.askquestion('Pergunta','Deseja limpar os campos!')

                if resp=='yes':

                    self.txdados['state']='normal'

                    self.txvalor.delete(0,END)
                    self.txdados.delete('1.0',END)

                    self.txdados['state']='disabled'

                    self.txvalor.focus()

        pass


    pass


App08()