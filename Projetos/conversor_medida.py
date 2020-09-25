from tkinter import*
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from centralizarform import centralizando
from componentes import Objetos

class App08:

    def __init__(self):
        super().__init__()

        self.root=Tk()

        self.fram01=Frame(self.root,bd=0.5,relief='solid')
        self.fram01.place(relx=0.02,rely=0.02,relwidth=0.495,relheight=0.955)

        self.fram02=Frame(self.root,bd=0.5,relief='solid')
        self.fram02.place(relx=0.525,rely=0.02,relwidth=0.45,relheight=0.955)    

        centralizando.posicionar(self,600,350,False)
        Objetos.tela(self,'App 08 - Python')

        Objetos.botoes(self,self.fram01,'Analisar',lx=0.295,ly=0.525,largura=0.5,altura=0.165,comando=self.analisar)
        Objetos.botoes(self,self.fram01,'Cancelar',lx=0.295,ly=0.725,largura=0.5,altura=0.165,comando=self.limpar)
        
        Objetos.labels(self,self.fram01,'Digite um valor',lx=0.295,ly=0.225,largura=0.32,altura=0.09)
        

        self.textbox()

        self.root.mainloop()

        pass

    def textbox(self):

        self.multitexto=ScrolledText(self.fram02,state='disabled')
        self.multitexto.place(relx=0,rely=0,relwidth=1,relheight=1)

        self.txvalor=Entry(self.fram01,bd=0.5,relief='solid')
        self.txvalor.place(relx=0.325,rely=0.32,relwidth=0.45,relheight=0.065)

        self.txvalor.focus()

        pass

    def limpar(self):

        self.txvalor.delete(0,END)
        self.multitexto.delete('1.0',END)
        self.multitexto['state']='disabled'
        self.txvalor.focus()

        pass

    def analisar(self):

        try:

                        
            if self.txvalor.get().strip()=='':

                messagebox.showwarning('Atenção','Preencher o campo em questão!')
                self.txvalor.focus()

            else:
                
                num=float(self.txvalor.get())
                cm=num*100
                mm=num*1000
                km=num/1000
                hm=num/100
                dam=num/10
                dm=num*10


                resposta='A medida em {}m corresponde a {}cm, {}mm, {}km, {}hm, {}dam e {}dm'.format(num,cm,mm,km,hm,dam,dm)

                self.multitexto['state']='normal'
                self.multitexto.delete('1.0',END)
                self.multitexto.insert(END,resposta)

        except:

            messagebox.showerror('Erro','Dados inseridos são invalidos!')
            self.limpar()

        pass

    pass

App08()