# INSTALL.md #

This document details the rough outline of things that are required when building a new system. Where applicable instructions will delineate between macOS and linux builds.

## 1. Homebrew

This very first thing install on a new macOS is homebrew.
Brew list file can be found on github:danielmichaels

## 2. Python3

On macOS this is facilitated via Homebrew thus ensuring the most recent python
distrubution. On linux, I opt to use the standard python3 installation.

* VIRTUALENV and VIRTUALENVWRAPPER

after installing python3 and pip-python3 I install virtualenv, and virtualenvwrapper
on the system wide python. I endevour to install minimal python packages on the
base system. Often I will install 'speedtest-cli' as I like to test the internet
speeds from time to time without launching a virtualenv.

macOS specific:
# taken from .zshrc
	VIRTUALENVWRAPPER_PYTHON='which python3'
	source /usr/local/bin/virtualenvwrapper.sh
	export WORKON_HOME=$HOME/.virtualenvs
	alias mkvirtualenv="mkvirtualenv --python=/usr/local/bin/python3"

I create an alias for virtualenvwrapper as seen above to force the creation of
a python3 virtualenv. Recently, macOS (or Homebrew) has necessitated this
whereas in the past only the first three lines would do the trick. The alias 
could be shortened or changed to delineate between python2 or python3 but I am
making a concerted effort to use python3 only going forward.

## 3. zsh

I prefer zsh over bash, and immediately change it to the default shell. Further,
I install oh-my-zsh. At this stage I do not have a set .zshrc file for use across 
all systems. I mostly use the default, and make changes depending on my needs
of the hour.

I use `dieter` as my default color scheme

I will make one that does include the Vim bindings and VIRTUALENVWRAPPER 

## 4. Vim

Vim is a compulsory installation for all systems. I cannot stand using awkward
key bindings or a trackpad to move the cursor around. 

I have an extensive .vimrc file which can be found at github: danielmichaels
This .vimrc does require the cloning of the Vundle package manager and installation
of several dependancies. YouCompleteMe can be a cantankerous install on some
systems and if so, can be commented out.

The shell defaults the emacs bindings. To switch to Vim bindings two lines are
amended to the .zshrc file:
  bindkey -v # this replaces emacs with vi
  bindkey -M viins 'jk' vi-cmd-mode # makes 'jk' the escape to cmd mode keys

## 5. Zsh-Syntax-Highlighting

This is a brilliant feature that is cloned from the github account of the same
name. It will highlight any command on the shell. It requires a source to the
install location in .zshrc or .bashrc

**# include this in the .zshrc file into GH**

## 6. Shell Profile

My current choice is the Solarized Dark theme from the Solarized website. Although,
the 'selection' setting is currently too similar to the background to be identified.
As such, it does require manual adjustment, lest it look like you cannot select
text within the shell.

## 7. Pycharm

Vim is a great tool and easily the most productive tool on the system (I am
writing this in it) but IDE's make coding simple. Pycharm is an excellent IDE,
although a resource hog. 

IdeaVIM is a must have plugin. To enable it to use the system .vimrc the following
must be created:

	# .ideavimrc
	source ~/.vimrc

## 8. Private Internet Access

A must have application

## 9. KeePassXC

Password manager that stores inside a local database.

## 10. Wireshark

Must have packet sniffer; GUI.

## 11. SublimeText and NeoVim

Recently, I have installed SublimeText and the various packages that extend its usefulness.
All packages are to be installed via the Package Control manager; it is the only package that 
requires manual installation.

Packages:
- Package Control
- ActualVim
- AutoPEP8
- GitGutter
- Git
- All Autocomplete
- Markdown Extended
- Markdown Preview
- Pylinter
- SideBarEhancement
- Theme - Soda Solarized
- Theme - Spacegray
- WordCount

	ActualVim requires NeoVim to be installed on the system. On macOS use Homebrew.
	Creation of ~/.config/nvim/init.vim is necessary.
  Also, the neovim path needs to be set inside ST3's ActualVim settings.
	~~(add init.vim to GH)~~

	
## 12. 

This is within BB private repo, currently only for linux.
