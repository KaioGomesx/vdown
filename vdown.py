from tkinter import *
from tkinter import messagebox
import os
#Detectar diretório do usuário
dir = os.path.expanduser("~/")
#Verificar existencia dos diretórios
if (os.path.isdir("{}Vídeos".format(dir)) == True):
    print("OK")
else:
    os.system("mkdir {}Vídeos".format(dir))
if (os.path.isdir("{}musics".format(dir)) == True):
    print("OK")
else:
    os.system("mkdir ~/musics")

#checar conexão com a internet
def check():
	checknetwork = os.system("ping www.youtube.com -c 1")
	if (checknetwork != 0):
		aviso = messagebox.askretrycancel("AVISO", "Não foi possível conectar com a internet")
		if(aviso == True):
			check()
		else:
			j.destroy()
#Baixar como vídeo    
def vid():
	check()
	a = l.get()
	a = a.replace(" ","")
	l.delete(0,"end")
	if (a == ""):
		messagebox.showerror("ERRO","O link está vazio!")
	else:
		video = os.system("youtube-dl {} -f mp4 -o \"~/Vídeos/%(title)s.%(ext)s\"".format(a))
		if(video == 256):
			messagebox.showerror("ERROR","Link inválido!")
		else:
			messagebox.showinfo("Aviso","Arquivo baixado!")
#Baixar como música
def mus():
	check()
	a = l.get()
	a = a.replace(" ","")
	l.delete(0,"end")
	if (a == ""):
		messagebox.showerror("ERROR", "O link está vazio!")
	else:
		musc = os.system("youtube-dl {} --extract-audio --audio-format mp3 -o \"~/musics/%(title)s.%(ext)s\"".format(a))
		if (musc == 256):
			messagebox.showerror("ERROR", "Link inválido")
		else:
			messagebox.showinfo("Aviso", "Arquivo Baixado!")
#Criar janela			
j = Tk()
j.title("vdown(Beta) by: curing0")
j.geometry("500x250")
ig = PhotoImage(file='/usr/share/icons/duck.gif')
j.tk.call('wm', 'iconphoto',j._w, ig)
tp = Label(j, text="Video Downloader", font="Verdana 20")
tp.pack()
tl = Label(j, text="Insira o link do video abaixo:")
tl.pack()
l = Entry()
l.pack()
bv = Button(j, text="Download Video", command = vid)
bv.pack()
bm = Button(j, text="Download Music", command = mus)
bm.pack()
lem = Label(j, text="OBS: Os arquivos são salvos automaticamente em ~/Vídeos/ ou ~/musics")
lem.pack()
con = Label(j, text="")
con.pack()
by = Label(j, text="My Telegram: @Curing0", fg="blue")
git = Label(j, text="My Github: https://github.com/curing0")
don = Label(j, text="Donate: 3H5jubwe2HraBz5LmLyUtWE1QuUL4VJSJi", fg="yellow")
by.pack()
git.pack()
don.pack()
#Mostrar mensagem de erro caso esteja sem conexão com a internet
check()
j.mainloop()
