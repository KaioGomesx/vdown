# instalar o figlet e mostrar o "install" bem grandão na tela pq é estiloso
sudo dnf install figlet
figlet -c install
sleep 0.5

echo "         ====== Esse setup é recomendado apenas para o Fedora 29 ======"
echo "         Aguarde enquanto faremos a instalação das dependências necessárias "

# adicionar o repositorio pra instalação do FFmpeg (somente pro Fedora 29)
sudo yum install http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-29.noarch.rpm

# instalar o python e as libs necessárias
sudo dnf install python3
sudo dnf install python-pip
sudo dnf install tk
sudo pip install youtube-dl
sudo dnf install ffmpeg

sudo cp vdown.py /usr/bin
sudo cp duck.ico /usr/share/icons/
sudo mkdir /usr/share/vdown/
sudo cp vdowninfo.png /usr/share/icons/
sudo chown $USER /usr/share/vdown/
sudo echo -e " \n[Desktop Entry]\nType=Application\nName=Vdown\nExec=python3 /usr/bin/vdown.py\nIcon=/usr/share/icons/duck.ico" > /home/$USER/Área\ de\ Trabalho/Vdown.desktop && sleep 0.5 && sudo chmod +x /home/$USER/Área\ de\ Trabalho/Vdown*
echo "[Instalação conluída]"
sudo python3 language.py
