sudo pacman -S figlet
figlet Install
sleep 0.5
sudo pacman -S python
sudo pacman -S python-pip
sudo pacman -S tk
sudo pip install youtube-dl
sudo cp vdown.py /usr/bin/
sudo cp duck.ico /usr/share/icons/
sudo echo -e " \n[Desktop Entry]\nType=Application\nName=Vdown\nExec=python3 /usr/bin/vdown.py\nIcon=/usr/share/icons/duck.ico" > /home/$USER/Desktop/Vdown.desktop && sleep 0.5 && chmod +x /home/$USER/Desktop/Vdown*
echo "[Instalação conluída]"