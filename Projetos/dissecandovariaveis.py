from tkinter import*
from centralizarform import centralizando
from componentes import Objetos
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

class App04:

    def __init__(self):
        super().__init__()
        
        self.root=Tk()
 

        self.frame01= Frame(self.root,bd=0.5,relief='solid')
        self.frame01.place(relx=0.03,rely=0.03,relwidth=0.5,relheight=0.92)

        self.frame02= Frame(self.root,bd=0.5,relief='solid')
        self.frame02.place(relx=0.55,rely=0.03,relwidth=0.42,relheight=0.92)        
                
        centralizando.posicionar(self,650,300,False)
        Objetos.tela(self,'App 04 - Python')
        Objetos.labels(self,self.frame01,'Digite Algo:',lx=0.12,ly=0.25,largura=0.25,altura=0.07)

        Objetos.botoes(self,self.frame01,'Click',lx=0.15,ly=0.55,largura=0.65,altura=0.18,comando=self.analisar)
        Objetos.botoes(self,self.frame01,'Limpar',lx=0.15,ly=0.75,largura=0.65,altura=0.18,comando=self.limpar)

        self.textbox()
                
        self.root.mainloop()

        pass

    def textbox(self):

        self.valor=Entry(self.frame01,bd=0.5,relief='solid')
        self.valor.place(relx=0.15,rely=0.325,relwidth=0.65,relheight=0.07)

        self.texto=ScrolledText(self.frame02)
        self.texto.place(relx=0,rely=0,relwidth=1,relheight=1)

        self.valor.focus()

        pass

    def analisar(self):

        val=self.valor.get()

        if val.strip()=='':

            messagebox.showwarning('Atenção','Preencher o campo!')
            self.valor.focus()

        else:
            
            self.texto.insert(INSERT,'Analisando Dados:\n O tipo primitivo desse valor é {}.\nSó tem espaço {}\nÉ um número? {}\nEstá em maiúsculo: {}\nEstá em minúsculo: {}\nEstá capitalizada: {}\nÉ alfabético: {}\nÉ alfanumérico: {}'.format(type(val),val.isspace(),val.isnumeric(),val.isupper(),val.islower(),val.istitle(),val.isalpha(),val.isalnum()))

        pass

    def limpar(self):

        val=self.valor.get()

        if val.strip()=='':

            self.valor.delete(0,END)
            self.valor.focus()

        else:

            resp=messagebox.askquestion('Pergunta','Deseja limpar os campos!')

            if resp=='yes':

                self.valor.delete(0,END)
                self.texto.delete('1.0',END)
                self.valor.focus()

        pass

    pass


App04()