## Path to your oh-my-zsh configuration.
ZSH=$HOME/.oh-my-zsh
#ZSH_THEME="spaceship"
ZSH_THEME="agnoster"
#ZSH_THEME="avit" # termtosvg minimal theme

HIST_STAMPS="dd.mm.yyyy"

plugins=(
  git
  tmux
  zsh-syntax-highlighting
  history
  z
  thefuck
  zsh-autosuggestions
  poetry
  colored-man-pages
)

source $ZSH/oh-my-zsh.sh

#######################################################
#                  Exports                            #
#######################################################
#
export PATH=$PATH:~/.cargo/bin
export PATH=$PATH:~/.local/bin
export GOPATH=$HOME/Code/go
export PATH=$PATH:$(go env GOPATH)/bin
export PATH=~/.npm-global/bin:$PATH
export EDITOR=vim
#
#######################################################
#                  General Alias                      #
#######################################################
#
alias zs="vim ~/.zshrc"
alias sz="source ~/.zshrc"
alias vimrc="vim ~/.vimrc"
alias fzfp="fzf --preview='head -$LINES {}'"
alias TS="trizen -Syu"
alias inet="ip -br a"
alias wiki="vim $HOME/Code/github/databank/playbook/pages/index.md"
alias ls="exa"
alias el="exa --oneline"
alias ee="exa --header --long"
alias la="exa --header --long --git --all"
alias ssh="ssh -v"
alias nextdnsup="sudo nextdns install -config b29cfa -report-client-info && sudo nextdns activate"
alias nextdnsdown="sudo nextdns deactivate && sudo nextdns uninstall"
alias doc='docker-compose'
alias notes='code $HOME/Documents/notes/'
alias offdocker='docker run --rm -it --name my-offensive-docker aaaguirrep/offensive-docker /bin/zsh'
#
#######################################################
#                  Git Alias                          #
#######################################################
#
alias gs="git status"
alias gf="git fetch"
alias gl="git log --graph --oneline --decorate --all"
alias gc="git commit"
alias gac="git add . && git commit" # drop into EDITOR to confirm 'git add .'
alias gp="git push -v"
alias blog="cd $HOME/Code/github/danielms && code ."
alias gitignore="gi linux,python,visualstudiocode,node,react,vuejs,python,rust,jetbrains,go"
alias checkout="git checkout"
#
######################################################
#                Custom Functions                    #
######################################################
#
gi() { curl -sLw n https://www.gitignore.io/api/$@ ;}
cheat() { curl -s "cheat.sh/$1"; }
startvm() { VBoxManage startvm "$1" }
stopvm() { VBoxManage controlvm "$1" poweroff }
pw() {
  pwgen -sync "${1:-48}" -1
}
#
FTS() {
  echo -e "[*] Checking Flatpak for Updates [*]"
  flatpak update
  echo -e "[*] Running Pacman -Syu [*]"
  trizen -Syu
  echo -e "[!] Update Complete! [!]"
}
# cd and ls automatically
function cd {
  builtin cd "$@" && ls -F; 
}

mkdircd() {
  mkdir -p $1 && cd $_
}

gotest() {
  go test $* | sed ''/PASS/s//$(printf "\033[32mPASS\033[0m")/'' | sed ''/SKIP/s//$(printf "\033[34mSKIP\033[0m")/'' | sed ''/FAIL/s//$(printf "\033[31mFAIL\033[0m")/'' | sed ''/FAIL/s//$(printf "\033[31mFAIL\033[0m")/'' | GREP_COLOR="01;33" egrep --color=always '\s*[a-zA-Z0-9\-_.]+[:][0-9]+[:]|^'
}

poetryshell() {
  echo "Activating Poetry shell..."
  source "$( poetry env list --full-path | grep Activated | cut -d' ' -f1 )/bin/activate"
}


#######################################################
#                 VIM bindings                        #
#######################################################
#
set -o vi
bindkey -v
bindkey -M viins 'jk' vi-cmd-mode
bindkey '^R' history-incremental-search-backward
bindkey '^ ' autosuggest-accept
#
#######################################################
#                 VIRTUALENV                          #
#######################################################
#
VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
#source /usr/bin/virtualenvwrapper.sh
source $HOME/.local/bin/virtualenvwrapper.sh  #work around --user install
export WORKON_HOME=$HOME/.virtualenvs
alias mkvirtualenv="mkvirtualenv --python=/usr/bin/python3" # manually change for py2
#source /usr/share/nvm/init-nvm.sh
#

eval $(thefuck --alias)
eval "$(starship init zsh)"

source /usr/share/nvm/init-nvm.sh
