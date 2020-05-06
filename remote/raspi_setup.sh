set -eu

# Input Password
read -p "Enter New Username [piuser]: " -s newusername
newusername=${newusername:-piuser}
read -p "New Password: " -s newpassword

# Add User and Set Password
sudo useradd --groups \
pi,adm,dialout,cdrom,sudo,audio,video,plugdev,\
games,users,netdev,input,spi,gpio -m $newusername -s /bin/bash
echo "$newusername:$newpassword" | sudo chpasswd

# ssh
echo "Port 50022" | sudo tee -a /etc/ssh/sshd_config
sudo systemctl restart ssh

# Lock pi user
sudo passwd --lock pi

# Disable Auto Login
sudo raspi-config nonint do_boot_behaviour B1