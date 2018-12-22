from tkinter import *
import os, os.path

if os.path.exists("~/Vídeos"):
    print("Verificando existencia da pasta videos")
else:
    print("pasta videos nao existe\n[Criando..]")
    os.system("mkdir ~/Vídeos")
if os.path.exists("~/musics"):
    print("Diretório existe")
else:
    os.system("mkdir ~/musics")

def vid():  
  a = l.get()
  if (a == ""):
    con['fg']= "red"
    con['text']= "O link está vazio!"
  else:
    os.system("youtube-dl {} -f mp4 -o \"~/Vídeos/%(title)s.%(ext)s\"".format(a))
    con['fg']= "green"
    con['text']= "Arquivo baixado!"
def mus():
  a = l.get()
  if (a == ""):
    con['fg']= "red"
    con['text'] = "O link está vazio!"
  else:
    os.system("youtube-dl {} --extract-audio --audio-format mp3 -o \"~/musics/%(title)s.%(ext)s\"".format(a))
    con['text']=" "
    con['fg']= "green"
    con['text']= "Arquivo baixado!"
j = Tk()
j.title("vdown(Beta) by: curing0")
j.geometry("500x250")

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
j.mainloop()
