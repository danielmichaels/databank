# Vim

<!-- vim-markdown-toc GYM -->

* [Snippets](#snippets)
  - [Insert Date](#insert-date)
* [Tools/Plugins](#toolsplugins)
  - [Vim-Anywhere](#vim-anywhere)
  - [Vimwiki](#vimwiki)
  - [Vim-Plug](#vim-plug)
  - [seoul256](#seoul256)

<!-- vim-markdown-too -->

## Leader Mapping

**!! Important**

If you are mapping leader, if must come before
any calls to `<leader>` within `.vimrc` otherwise it cannot reference
the leader key. Always put the `let mapleader` be somewhere near the top, else
you will have to fix this unambiguous error.

## Snippets

### Insert Date

`!!date` from Normal mode.

## Tools/Plugins

### Vim-Anywhere

A great little tool that launches a terminal running vim. It saves the output to into `tmp`. 

I use it for:
- Writing emails 
- Writing documents - e.g, Word/ google docs at work

It defaults to an extensionless file. I changed it so extensionless files will automatically become markdown. Markdown suits my flow a lot better and integrates with the rest of my `vimrc`.

### Vimwiki

### Vim-Plug

### seoul256


