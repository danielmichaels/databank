#!/bin/bash

set -e

VERSION=1.0
VIMRC_DL=https://raw.githubusercontent.com/danielmichaels/databank/master/dotfiles/.vimrc
ZSHRC_DL=https://raw.githubusercontent.com/danielmichaels/databank/master/dotfiles/.zshrc
TMUX_DL=https://raw.githubusercontent.com/danielmichaels/databank/master/dotfiles/.tmux.conf.local
PKG_LIST=( ttf-liberation noto-fonts noto-fonts-emoji vim cmake go docker bat jq quake
  pipx tmux discord notion-app git nmap wireshark-qt pycharm-professional tcpdump rsync )
FAIL_LIST=( )
PIPX_PKGLIST=( tldr glances thefuck )


echo -e "[*] Provisioner ${VERSION} [*]"
echo -e "Arch Packages, Zsh, Vim and Python packages will be installed"

# setup trizen
echo -e "[!] Trizen AUR Package Manager Installing [!]\n"
sleep 2
if ! [ -x "$(command -v trizen)" ]; then
  echo -e "$HOME/Applications being created"
  cd && mkdir -p $HOME/Applications && cd $_
  echo -e "Trizen installed in ${$HOME/Applications}"
  git clone https://aur.archlinux.org/trizen.git && cd trizen && makepkg -si && cd
  echo -e "[!] Trizen Installed! [!]\n"
else
  echo -e "Trizen is installed. Skipping..."
fi
sleep 2 

echo -e "[!] Installing Packages [!]\n"
for i in "${PKG_LIST[@]}"
do
  if trizen -S $i; then
    echo "$i installed!"
  else
    echo "$i Failed to install"
    FAIL_LIST+="$i "
  fi
done
echo -e "[!!!] the following packages were not installed [!!!]\n"
echo -e $FAIL_LIST
echo -e "[!] Package Installation Completed [!]\n"

# curl oh-my-zsh vimplug vimrc zshrc zsh-syntax zsh-auto-suggest .tmux

# pacman via trizen to access AUR

echo -e "Now installing oh-my-zsh, its plugins and vim-plug."
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
echo - "oh-my-zsh installed"
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
echo -e "zsh-autosuggestions installed"
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
echo -e "zsh-syntax-hightlighting installed"
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
echo -e "vim-plug installed"

echo -e "creating $HOME/Code directory. This is needed for .zshrc alias'"
if ! [ -d $HOME/Code ]; then
  mkdir -p $HOME/Code
  echo -e "$HOME/Code created!"
else
  echo -e "$HOME/Code already exists\n...skipping"
fi

# .tmux
echo -e "setting up tmux"
cd && git clone https://github.com/gpakosz/.tmux.git && ln -s -f .tmux/.tmux.conf
cp .tmux/.tmux.conf.local .
curl ${TMUX_DL} > .tmux.conf.local
cd
echo -e "custom tmux setup complete."

# dotfiles
echo -e "creating custom .vimrc and .zshrc files"
curl ${VIMRC_DL} > ~/.vimrc
curl ${ZSHRC_DL} > ~/.zshrc
echo -e "...done"

# pipx
echo -e "pipx installing ${PIPX_PKGS}"
for i in "${PIPX_PKGLIST[@]}"
do
  if pipx install $i; then
    echo -e "$i installed"
  fi
done
echo -e "pipx finished installing packages"

# virtualenvwrapper
echo -e "virtualenvwrapper now being installed"
pip install virtualenvwrapper
echo -e "..done!"

# docker and docker-compose
echo -e "[*] Docker and Docker-Compose will now be setup [*]"
echo -e "Docker groups are being added.."
sudo groupadd docker && sudo usermod -aG docker $USER
#newgrp docker
echo -e "..done\nYoy may need to log out for this to take effect!\nConfigure docker to start on boot.."
sudo systemctl start docker
sudo systemctl enable docker
echo -e "..done!"
echo -e "Downloading Docker-Compose..."
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.5/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
echo -e "..done!"
echo -e "..applying permissions"
sudo chmod +x /usr/local/bin/docker-compose
echo -e "..done!"
sudo chmod +x /usr/local/bin/docker-compose

echo -e "[!] Provisioner Complete [!]\n\tEnjoy!"

