sudo pacman -S figlet
figlet Install
sleep 0.5
sudo pacman -S python
sudo pacman -S python-pip
sudo pacman -S tk
sudo pip install youtube-dl
sudo pacman -S ffmpeg
sudo cp vdown.py /usr/bin/
sudo cp duck.ico /usr/share/icons/
sudo mkdir /usr/share/vdown/
sudo echo -e " \n[Desktop Entry]\nType=Application\nName=Vdown\nExec=python3 /usr/bin/vdown.py\nIcon=/usr/share/icons/duck.ico" > /home/$USER/Desktop/Vdown.desktop && sleep 0.5 && sudo chmod +x /home/$USER/Desktop/Vdown*
sudo echo -e " \n[Desktop Entry]\nType=Application\nName=Vdown\nExec=python3 /usr/bin/vdown.py\nIcon=/usr/share/icons/duck.ico" > /usr/share/applications/Vdown.desktop && sleep 0.5 && sudo chmod +x /usr/share/applications/Vdown*
echo "[Instalação conluída]"
