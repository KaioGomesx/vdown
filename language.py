from tkinter import *
import os

dir = os.path.expanduser("~/")
def en():
	a = os.path.isdir("{}Videos".format(dir))
	b = os.path.isdir("{}Music".format(dir))
	
	c = open("/usr/share/vdown/lang.conf","w")
	c.write("en")
	c.close()
	
	if (a == False) and (b == False):
		os.system("mkdir {}Videos".format(dir))
		os.system("mkdir {}Music".format(dir))
		
	else:
		
		print("OK")
	j.destroy()
		
def pt():
	a = os.path.isdir("{}Vídeos".format(dir))
	b = os.path.isdir("{}Música".format(dir))
	
	c = open("/usr/share/vdown/lang.conf","w")
	c.write("pt")
	c.close()
	
	if(a == False) and (b == False):
		os.system("mkdir {}Vídeos/".format(dir))
		os.system("mkdir {}Música".format(dir))
	else:
		print("OK")
	j.destroy()
	
j = Tk()
j.title("Configuração do idioma")
j.geometry("200x100")

t = Label(j, text = "Escolha um Idioma:")
t.pack()

b1 = Button(j, text="en", width=7, command=en)
b1.pack(side="left")
b2 = Button(j, text="pt", width=7, command=pt)
b2.pack(side="right")


j.mainloop()
