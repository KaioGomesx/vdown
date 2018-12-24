sudo apt-get install figlet
figlet install
sleep 0.5
sudo apt-get install python3
sudo apt-get install python-pip
sudo apt-get install tk
sudo pip install youtube-dl
sudo apt-get install ffmpeg
sudo cp vdown.py /usr/bin
sudo cp duck.gif /usr/share/icons/
sudo mkdir /usr/share/vdown/
sudo echo -e " \n[Desktop Entry]\nType=Application\nName=Vdown\nExec=python3 /usr/bin/vdown.py\nIcon=/usr/share/icons/duck.ico" > /home/$USER/Desktop/Vdown.desktop && sleep 0.5 && chmod +x /home/$USER/Desktop/Vdown*
sudo echo -e " \n[Desktop Entry]\nType=Application\nName=Vdown\nExec=python3 /usr/bin/vdown.py\nIcon=/usr/share/icons/duck.ico" > /usr/share/applications/Vdown.desktop && sleep 0.5 && sudo chmod +x /usr/share/applications/Vdown*
