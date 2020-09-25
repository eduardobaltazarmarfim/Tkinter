from tkinter import*

root=Tk()

def mensagem():

    print(valores.get())

valores=IntVar()

ra1=Radiobutton(root,text='Opção 01',variable=valores,value=1)
ra1.pack()

ra2=Radiobutton(root,text='Opção 02',variable=valores,value=2)
ra2.pack()

ra3=Radiobutton(root,text='Opção 03',variable=valores,value=3)
ra3.pack()

Button(root,text='Click',command=mensagem).pack()


root.mainloop()