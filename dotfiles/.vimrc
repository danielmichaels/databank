" Maintainer: Danielmichaels 
"        URL: https://github.com/danielmichaels
"                                                                            "
"                                                                            "
" Sections:                                                                  "
"   01. General ................. General Vim behavior                       "
"   02. Events .................. General autocmd events                     "
"   03. Theme/Colors ............ Colors, fonts, etc.                        "
"   04. Vim UI .................. User interface behavior                    "
"   05. Text Formatting/Layout .. Text, tab, indentation related             "
"   06. Custom Commands ......... Any custom command aliases                 "
"   07. Hybrid Line numbering.... Line numbering bingings
"   08. Vim-Go................... Vim-go specific bindings
"   09. Vimwiki.................. Vimwiki custom bindings
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 01. General/ Plugins                                                       "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set nocompatible         " get rid of Vi compatibility mode. SET FIRST!

call plug#begin()
Plug 'joshdick/onedark.vim'
Plug 'junegunn/seoul256.vim'
Plug 'junegunn/goyo.vim'
Plug 'junegunn/limelight.vim'
Plug 'fatih/vim-go', {'for': ['go', 'markdown'] } "Loads only when editing go files
Plug 'scrooloose/nerdtree', {'on': ['NERDTreeToggle', 'NERDTreeFind'] } "Loads only when opening NERDTree
Plug 'jistr/vim-nerdtree-tabs'
Plug 'vimwiki/vimwiki', {'branch': 'dev'}
Plug 'mattn/calendar-vim'
Plug 'suan/vim-instant-markdown', {'for': 'markdown'}
Plug 'tpope/vim-fugitive'
"Plug 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
Plug 'Valloric/YouCompleteMe', { 'do': './install.py' }
Plug 'airblade/vim-gitgutter'
Plug 'mzlogin/vim-markdown-toc'
Plug 'mattn/emmet-vim'
" Language and File types
Plug 'cakebaker/scss-syntax.vim'
Plug 'chr4/nginx.vim'
Plug 'chrisbra/csv.vim'
Plug 'ekalinin/dockerfile.vim'
Plug 'elixir-editors/vim-elixir'
Plug 'Glench/Vim-Jinja2-Syntax'
Plug 'stephpy/vim-yaml'
Plug 'pearofducks/ansible-vim'
"Plug 'altercation/vim-colors-solarized'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

call plug#end()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 02. Events                                                                 "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

filetype plugin indent on " filetype detection[ON] plugin[ON] indent[ON]
" :set paste is now macro'd to F2; this prevents 
" messed up pasting of HTML/CSS templates
set pastetoggle=<F2>
"call togglebg#map("<F5>")
" In Makefiles DO NOT use spaces instead of tabs
autocmd FileType make setlocal noexpandtab
" In Ruby files, use 2 spaces instead of 4 for tabs
autocmd FileType ruby setlocal sw=2 ts=2 sts=2
"
" Enable omnicompletion (to use, hold Ctrl+X then Ctrl+O while in Insert mode.
set ofu=syntaxcomplete#Complete
set clipboard=unnamed
"
let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree
"
"autocomplete
let g:ycm_autoclose_preview_window_after_completion=1
"
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 03. Theme/Colors                                                           "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
syntax enable             " enable syntax highlighting (previously syntax on).
set t_Co=256              " enable 256-color mode.
"set t_Co=16              " enable 16-color mode.
"colo seoul256
" Enable 24-bit true colors if your terminal supports it.
if (has("termguicolors"))
   " https://github.com/vim/vim/issues/993#issuecomment-255651605
     let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
     let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"

  set termguicolors
endif
colorscheme onedark
set background=dark

" Prettify JSON files
autocmd BufRead,BufNewFile *.json set filetype=json
"autocmd Syntax json sou ~/.vim/syntax/json.vim

" Prettify Vagrantfile
autocmd BufRead,BufNewFile Vagrantfile set filetype=ruby

" Prettify Markdown files
augroup markdown
  au!
  au BufNewFile,BufRead *.md,*.markdown setlocal filetype=ghmarkdown | set wrap | set linebreak
augroup END

"Highlight characters that go over 80 columns (by drawing a border on the 81st)
if exists('+colorcolumn')
  set colorcolumn=81
  highlight ColorColumn ctermbg=red
else
  highlight OverLength ctermbg=red ctermfg=white guibg=#592929
  match OverLength /\%81v.\+/
endif

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 04. Vim UI                                                                 "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set number                " show line numbers
set numberwidth=6         " make the number gutter 6 characters wide
set cul                   " highlight current line
set laststatus=2          " last window always has a statusline
set nohlsearch            " Don't continue to highlight searched phrases.
set incsearch             " But do highlight as you type your search.
set ignorecase            " Make searches case-insensitive.
set ruler                 " Always show info along bottom.
set showmatch
set statusline=%<%f\%h%m%r%=%-20.(line=%l\ \ col=%c%V\ \ totlin=%L%)\ \ \%h%m%r%=%-40(bytval=0x%B,%n%Y%)\%P
set visualbell

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 05. Text Formatting/Layout                                                 "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set autoindent            " auto-indent
set tabstop=2             " tab spacing
set softtabstop=2         " unify
set shiftwidth=2          " indent/outdent by 2 columns
set shiftround            " always indent/outdent to the nearest tabstop
set expandtab             " use spaces instead of tabs
set smartindent           " automatically insert one extra level of indentation
set smarttab              " use tabs at the start of a line, spaces elsewhere
set nowrap                " don't wrap text

"""""""""""""""""""""""""""""""""""""""""""""""""""""
"
"------------Start Python PEP 8 stuff----------------
" Number of spaces that a pre-existing tab is equal to.
au BufRead,BufNewFile *py,*pyw,*.c,*.h set tabstop=4

"spaces for indents
au BufRead,BufNewFile *.py,*pyw set shiftwidth=4
au BufRead,BufNewFile *.py,*.pyw set expandtab
au BufRead,BufNewFile *.py set softtabstop=4

" Use the below highlight group when displaying bad whitespace is desired.
highlight BadWhitespace ctermbg=red guibg=red

" Display tabs at the beginning of a line in Python mode as bad.
au BufRead,BufNewFile *.py,*.pyw match BadWhitespace /^\t\+/
" Make trailing whitespace be flagged as bad.
au BufRead,BufNewFile *.py,*.pyw,*.c,*.h match BadWhitespace /\s\+$/

" Wrap text after a certain number of characters
au BufRead,BufNewFile *.py,*.pyw, set textwidth=100

" Use UNIX (\n) line endings.
au BufNewFile *.py,*.pyw,*.c,*.h set fileformat=unix

au BufNewFile,BufRead *.js,*.html,*.css
    \ setlocal tabstop=2 softtabstop=2 shiftwidth=2

nnoremap <buffer> <F9> :exec '!python' shellescape(@%, 1)<cr>
" ^ maps <F9> to the run script in Python only
nmap ;w :w<CR>
" ^ maps ;w as save instead of :w
let g:NERDTreeWinSize=20
set spell spelllang=en_au
nnoremap <leader>f 1z=
nnoremap <leader>s :set spell!
:hi SpellBad cterm=underline ctermfg=red
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 06. Custom Commands                                                        "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"
" Prettify JSON files making them easier to read
command PrettyJSON %!python -m json.tool
"
let mapleader=" "
let mapleader = "\<Space>"
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>
inoremap jk <ESC>
""inoremap " ""<left>
""inoremap ' ''<left>
"inoremap ( ()<left>
"inoremap [ []<left>
"inoremap { {}<left>
"inoremap {<CR> {<CR>}<ESC>O
"inoremap {;<CR> {<CR>};<ESC>O
"
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 07. Hybrid line numbering
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
":set number relativenumber

:augroup numbertoggle
:  autocmd!
:  autocmd BufEnter,FocusGained,InsertLeave * set relativenumber
:  autocmd BufLeave,FocusLost,InsertEnter   * set norelativenumber
:augroup END
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 08. Go-Vim Custom
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set autowrite " autowrites file on func call.
set showcmd " shows the leader key bottom; auto timeout 1000ms 
" run :GoBuild or :GoTestCompile based on go file
function! s:build_go_files()
  let l:file = expand('%')
  if l:file =~# '^\f\+_test\.go$'
    call go#test#Test(0,1)
  elseif l:file =~# '^\f\+\.go$'
    call go#cmd#Build(0)
  endif
endfunction
"
map <C-n> :cnext<CR>
map <C-m> :cprevious<CR>
nnoremap <leader>a :cclose<CR>
au FileType go nmap <leader>r  :<C-u>GoRun<cr>
autocmd FileType go nmap <leader>t <Plug>(go-test) 
autocmd FileType go nmap <leader>c <Plug>(go-coverage-toggle)
autocmd FileType go nmap <leader>b :<C-u>call <SID>build_go_files()<CR>
" Prettify stuff below, can be removed if performance suffers
let g:go_list_type = "quickfix" " so it doesn't use 'location list'
let g:go_fmt_command = "goimports"
let g:go_highlight_types = 1
let g:go_highlight_fields = 1
let g:go_highlight_functions = 1
let g:go_highlight_operators = 1


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 09. Vimwiki Custom
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" vimwiki syntax
let g:vimwiki_list = [{'path': '$HOME/Code/github/databank/playbook/pages/', 'syntax': 'markdown', 'ext':'.md'}]

command! Diary VimwikiDiaryIndex
augroup vimwikigroup
    autocmd!
    " automatically update links on read diary
    autocmd BufRead,BufNewFile diary.md VimwikiDiaryGenerateLinks
augroup end
nnoremap <leader>dd :Diary<CR>
nnoremap <leader>ch :CalendarH<CR>
nnoremap <leader>c :Calendar<CR>
nnoremap <leader>md :InstantMarkdownPreview<CR>
nnoremap <leader>mdx :InstantMarkdownStop<CR>
" Insert the image URL for dwiki/images
nnoremap <leader>img <INSERT>https://github.com/danielmichaels/dwiki/blob/master/images/<CR>

" vim-instant-preview
"Uncomment to override defaults:
"let g:instant_markdown_slow = 1
let g:instant_markdown_autostart = 0
"let g:instant_markdown_open_to_the_world = 1 
"let g:instant_markdown_allow_unsafe_content = 1
"let g:instant_markdown_allow_external_content = 0
"let g:instant_markdown_mathjax = 1
let g:instant_markdown_browser = "firefox --new-window"
let g:vmt_cycle_list_item_markers = 1
let g:vimwiki_markdown_link_ext = 1
let g:vimwiki_dir_link = 'index'
"let g:vimwiki_auto_toc = 1
let g:instant_markdown_logfile = "/tmp/instant_markdown.log"
"
" Aggregate all vim swap files to one place. Vimwiki constant swp issues.
" Folder '.vim/swapfiles' must be created first!!
set directory^=$HOME/.vim/swapfiles//
