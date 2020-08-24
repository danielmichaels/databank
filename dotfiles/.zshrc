# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
  export ZSH=/home/$USER/.oh-my-zsh
# Set name of the theme to load. Optionally, if you set this to "random"
# it'll load a random theme each time that oh-my-zsh is loaded.
# See https://github.com/robbyrussell/oh-my-zsh/wiki/Themes
#ZSH_THEME="spaceship"
ZSH_THEME="agnoster"
#ZSH_THEME="avit" # termtosvg minimal theme

# Set list of themes to load
# Setting this variable when ZSH_THEME=random
# cause zsh load theme from this variable instead of
# looking in ~/.oh-my-zsh/themes/
# An empty array have no effect
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion. Case
# sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# The optional three formats: "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
HIST_STAMPS="dd.mm.yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load? (plugins can be found in ~/.oh-my-zsh/plugins/*)
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(
  git
  tmux
  zsh-syntax-highlighting
  history
  z
  thefuck
#  dotenv
  zsh-autosuggestions
  poetry
  colored-man-pages
)
# git clone https://github.com/supercrabtree/k $ZSH_CUSTOM/plugins/k
# ^ for k (the new l, yo)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# ssh
# export SSH_KEY_PATH="~/.ssh/rsa_id"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
# alias zshconfig="mate ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"
#
#export PATH=$PATH:/go/bin
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
alias e="exa"
alias el="exa --oneline"
alias ee="exa --header --long"
alias ea="exa --header --long --git --all"
alias ssh="ssh -v"
alias nextdnsup="sudo nextdns install -config b29cfa -report-client-info && sudo nextdns activate"
alias nextdnsdown="sudo nextdns deactivate && sudo nextdns uninstall"
alias doc='docker-compose'
alias notes='code $HOME/Documents/notes/'
#alias history="history -E"
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

