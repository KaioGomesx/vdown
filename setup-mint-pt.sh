sudo apt-get install figlet
figlet install
sleep 0.5
sudo apt-get install python3
sudo apt-get install python-pip
sudo apt-get install tk
sudo pip install youtube-dl
sudo apt-get install ffmpeg
sudo cp vdown.py /usr/bin
sudo cp duck.ico /usr/share/icons/
sudo mkdir /usr/share/vdown/
sudo cp vdowninfo.png /usr/share/icons/
sudo chown $USER /usr/share/vdown/lang.conf
sudo echo -e " \n[Desktop Entry]\nType=Application\nName=Vdown\nExec=python3 /usr/bin/vdown.py\nIcon=/usr/share/icons/duck.ico" > /home/$USER/Área\ de\ Trabalho/Vdown.desktop && sleep 0.5 && sudo chmod +x /home/$USER/Área\ de\ Trabalho/Vdown*
echo "[Instalação conluída]"
python3 language.py
