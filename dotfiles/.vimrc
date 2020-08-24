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
Plug 'fatih/vim-go', {'for': ['go', 'markdown'] } "Loads only when editing go files
Plug 'scrooloose/nerdtree'
", {'on': ['NERDTreeToggle', 'NERDTreeFind'] } "Loads only when opening NERDTree
" above was removed as it prevents NERDTree from loading when calling 'vim' 
Plug 'vimwiki/vimwiki', {'branch': 'dev'}
Plug 'mattn/calendar-vim'
Plug 'suan/vim-instant-markdown', {'for': 'markdown'}
Plug 'tpope/vim-fugitive'
"Plug 'Lokaltog/powerline', {'rtp': 'powerline/bindings/vim/'}
Plug 'jistr/vim-nerdtree-tabs'
Plug 'Valloric/YouCompleteMe', { 'do': './install.py' }
Plug 'airblade/vim-gitgutter'
Plug 'mzlogin/vim-markdown-toc'
Plug 'mattn/emmet-vim'
Plug 'majutsushi/tagbar'
" Language and File types
Plug 'machakann/vim-highlightedyank'
Plug 'junegunn/fzf.vim'
Plug 'cakebaker/scss-syntax.vim'
Plug 'chr4/nginx.vim'
Plug 'chrisbra/csv.vim'
Plug 'ekalinin/dockerfile.vim'
Plug 'elixir-editors/vim-elixir'
Plug 'Glench/Vim-Jinja2-Syntax'
Plug 'stephpy/vim-yaml'
Plug 'pearofducks/ansible-vim'
Plug 'lifepillar/pgsql.vim'
Plug 'othree/html5.vim'
" Colours and Themes
"Plug 'altercation/vim-colors-solarized'
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'
Plug 'joshdick/onedark.vim'
Plug 'junegunn/seoul256.vim'
Plug 'junegunn/goyo.vim'
Plug 'junegunn/limelight.vim'
" Automatically show Vim's complete menu while typing.
Plug 'vim-scripts/AutoComplPop'
" A bunch of useful language related snippets (ultisnips is the engine).
Plug 'SirVer/ultisnips' | Plug 'honza/vim-snippets'

call plug#end()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 02. Events                                                                 "
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
let mapleader=" "
"let mapleader = "\<Space>"
:set mouse=n

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

" Source Vim config file.
map <Leader>sc :source $MYVIMRC<CR>
" Edit Vim config file in a new tab.
map <Leader>ev :tabnew $MYVIMRC<CR>
"
" autocomplete
let g:ycm_autoclose_preview_window_after_completion=1
" Press * to search for the term under the cursor or a visual selection and
" " then press a key below to replace all instances of it in the current file.
nnoremap <Leader>r :%s///g<Left><Left>
nnoremap <Leader>rc :%s///gc<Left><Left><Left>
let g:UltiSnipsExpandTrigger="<F3>"
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
set complete+=kspell      " autocomplete for misspelt words
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

" maps <F9> to the run script in Python only
nnoremap <buffer> <F9> :exec '!python' shellescape(@%, 1)<cr>

" maps ;w as save as well as :w
nmap ;w :w<CR>

" Spelling
set spell spelllang=en_au
" Automatically fix the last misspelled word and jump back to where you were.
" "   Taken from this talk: https://www.youtube.com/watch?v=lwD8G1P52Sk
nnoremap <leader>sp :normal! mz[s1z=`z<CR>
:hi SpellBad cterm=underline ctermfg=red

"nnoremap <leader>f 1z=
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 06. Custom Commands                                                        "
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"
" Prettify JSON files making them easier to read
command PrettyJSON %!python -m json.tool
"
map <leader>g  :YcmCompleter GoToDefinitionElseDeclaration<CR>
inoremap jk <ESC>

" NERDTree
" Start NERDTree on calling 'vim'; must be enabled on startup to function.
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
" shut vim if only the NERDTree pane is open.
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" Hot keys
"nnoremap <silent> <expr> <Leader>n g:NERDTree.IsOpen() ? "\:NERDTreeClose<CR>" : bufexists(expand('%')) ? "\:NERDTreeFind<CR>" : "\:NERDTree<CR>"
nnoremap <Leader>n :NERDTreeToggle<Enter>

let g:NERDTreeShowHidden=1
let g:NERDTreeAutoDeleteBuffer=1
let g:NERDTreeQuitOnOpen=0
let NERDTreeIgnore=['\.pyc$', '\~$'] "ignore files in NERDTree
let g:NERDTreeWinSize=20

map <leader>t :TagbarToggle<CR>
" Toggle spell check
nmap <F5> :setlocal spell!<CR>
" Toggle relative line number and regular line number
nmap <F6> :set invrelativenumber<CR> 
"
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" 07. Hybrid line numbering
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
:set number relativenumber

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
