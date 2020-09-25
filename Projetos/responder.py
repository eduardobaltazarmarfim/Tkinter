from tkinter import*
from centralizarform import centralizando
from componentes import Objetos
from tkinter import messagebox

class App02:

    def __init__(self):
        super().__init__()

        caminho='Aplicações/Imagem/bussola.ico'

        self.root=Tk()
        
        centralizando.posicionar(self,300,200,False)
        Objetos.tela(self,'App 02 - Python',imagemico=caminho)
        Objetos.labels(self,'Nome',lx=0.1,ly=0.25,largura=0.15,altura=0.1)

        Objetos.botoes(self,'Mensagem',lx=0.09,ly=0.6,largura=0.4,altura=0.22,comando=lambda:self.mensagem(self.nome.get()))
        Objetos.botoes(self,'Limpar',lx=0.525,ly=0.6,largura=0.4,altura=0.22,comando=lambda:self.limpar(self.nome.get()))

        self.textbox()
        
        self.root.mainloop()

        pass

    def textbox(self):

        self.nome=Entry(self.root,bd=0.5,relief='solid')
        self.nome.place(relx=0.25,rely=0.25,relwidth=0.65,relheight=0.1)

        self.nome.focus()

        pass
    
    def mensagem(self,nome=None):

        if nome.strip()=='':

            messagebox.showerror('Atenção','Favor preencher o campo em questão!')

        else:

            messagebox.showinfo('Informação',f'Seja bem vindo {nome.title()}')

        pass

    def limpar(self,nome=None):

        if nome.strip()=='':

            self.nome.delete(0,END)
            self.nome.focus()
            
        else:

            resp=messagebox.askquestion('Informação','Deseja limpar os campos!')

            if resp=='yes':

                self.nome.delete(0,END)
                self.nome.focus()
                

        pass

    pass

App02()