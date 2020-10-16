from tkinter import*
from tkinter import messagebox

root=Tk()

valor1=IntVar()
valor2=IntVar()

def Mensagem():

    if valor1.get()==1 and valor2.get()==1:

        messagebox.showwarning('Atenção','Os dois valores estão selecionados!')

    elif valor1.get()==1:

        messagebox.showinfo('Mensagem 01','Seja bem vindo!')

    elif valor2.get()==1:

        messagebox.showinfo('Mensagem 02','Hello World!')

    pass

root.geometry('300x200+0+0')
root.resizable(False,False)

c1=Checkbutton(root,text='Mensagem 01',variable=valor1,onvalue=1,offvalue=0)
c1.pack()

c2=Checkbutton(root,text='Mensagem 02',variable=valor2,onvalue=1,offvalue=0)
c2.pack()

btn=Button(root,text='Click',width=25,height=3,command=Mensagem).pack()


root.mainloop()