from tkinter import*
from tkinter import messagebox
from centralizando import Centralizar
from componentes import Objetos

class App05:

    def __init__(self):
        super().__init__()

        self.root=Tk()

        Centralizar.posicionar(self,self.root,300,375,False)
        Objetos.tela(self,self.root,'App 05 - Python')

        Objetos.botoes(self,self.root,'Analisar',lx=0.235,ly=0.65,largura=0.535,altura=0.135,comando=lambda:self.analisar(self.txvalor.get()))
        Objetos.botoes(self,self.root,'Limpar',lx=0.235,ly=0.825,largura=0.535,altura=0.135,comando=self.limpar)

        Objetos.labels(self,self.root,'Valor',lx=0.165,ly=0.125,largura=0.225,altura=0.135)
        Objetos.labels(self,self.root,'Antecessor',lx=0.225,ly=0.265,largura=0.225,altura=0.135)
        Objetos.labels(self,self.root,'Sucessor',lx=0.205,ly=0.395,largura=0.225,altura=0.135)

        self.textbox()

        self.root.mainloop()


        pass

    def textbox(self):

        self.txvalor=Entry(self.root,bd=1,relief='solid')
        self.txvalor.place(relx=0.235,rely=0.225,relwidth=0.525,relheight=0.056)

        self.txantecessor=Entry(self.root,bd=1,relief='solid',state='disabled')
        self.txantecessor.place(relx=0.235,rely=0.365,relwidth=0.525,relheight=0.056)

        self.txsucessor=Entry(self.root,bd=1,relief='solid',state='disabled')
        self.txsucessor.place(relx=0.235,rely=0.495,relwidth=0.525,relheight=0.056)

        self.txvalor.focus()               

        pass


    def analisar(self,Valor):

        if self.txvalor.get().strip()=='':

            messagebox.showwarning('Atenção','Favor preencher o campo!')
            self.limpar()

        else:

            try:

                Valor=int(Valor)

                antecessor=Valor-1
                sucessor=Valor+1

                self.txantecessor['state']='normal'
                self.txsucessor['state']='normal'

                self.txantecessor.insert(END,f'{antecessor}')
                self.txsucessor.insert(END,f'{sucessor}')

                self.txantecessor['state']='disabled'
                self.txsucessor['state']='disabled'

            except:

                messagebox.showerror('Erro','Dados inseridos são invalidos!')
                self.limpar(True)

        pass


    def limpar(self,pular=False):

        if pular==True:

            self.txvalor.delete(0,END)
            self.txantecessor['state']='normal'
            self.txsucessor['state']='normal'

            self.txantecessor.delete(0,END)
            self.txsucessor.delete(0,END)

            self.txantecessor['state']='disabled'
            self.txsucessor['state']='disabled'

            self.txvalor.focus()

        else:       

            if self.txvalor.get().strip()!='':

                res=messagebox.askyesno('Pergunta','Deseja limpar os campos!')

                if res==True:

                    self.txvalor.delete(0,END)
                    self.txantecessor['state']='normal'
                    self.txsucessor['state']='normal'

                    self.txantecessor.delete(0,END)
                    self.txsucessor.delete(0,END)

                    self.txantecessor['state']='disabled'
                    self.txsucessor['state']='disabled'

                    self.txvalor.focus()
        pass


    pass


App05()