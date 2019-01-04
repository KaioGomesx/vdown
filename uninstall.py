from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage
import os
dir = os.path.expanduser('~/')
tinfo='''
O desinstalador removerá os seguintes arquivos:
vdown.py ( localizada na pasta /usr/bin )
vdown/ ( todo o conteudo dento do repositório baixado, provavelmente na pasta {} )
duck.ico ( localizado na pasta /usr/share/icons )
lang.conf ( localizado na pasta /usr/share/vdown )

'''.format(dir)

def remover():
	os.system('locate vdown.py vdown/ duck.ico lang.conf > {}temp.txt')
	a = open('{}temp.txt'.format(dir))
	b = a.readlines()
	for i in b:
		os.system('sudo rm '+i)
	a.close()
	messagebox.showinfo('Aviso', 'Desinstalado com Sucesso!')
	os.system('rm {}temp.txt'.format(dir))
	j.destroy()
	
def info():
	i = Tk()
	i.title("Info")
	li = Label(i,text=tinfo)
	li.pack()
	i.mainloop()
j = Tk()
j.title('Desinstalar Vdown by:@Curing0')
j.geometry("380x130")
img= PhotoImage(file="/usr/share/icons/vdowninfo.png")
l = Label(j, text="Você deseja desinstalar Vdown(Beta)?", font=("Arial", "14"))
l.grid(column=1)
b = Button(j,image=img,command=info)
b.grid(column=2)
d = Button(j,text="Desinstalar",command=remover)
d.grid(column=1)
j.mainloop()
