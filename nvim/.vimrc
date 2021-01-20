"" GLOBAL CONFIGS
set number " set numer on the left
set mouse=a " allow using the mouse
set numberwidth=1 " change the size of the number select
set clipboard=unnamed " allow use the OS clipboard 
set showcmd " show comands selection
set ruler " show the actions
set encoding=utf-8
set showmatch " allow show parentheses
set relativenumber "show thge relative number to cursor
"set noshowmode "no show mode
set showmode
set cursorline "ersalt cursor line
set encoding=utf-8

"set sw=4 "cahnge tab to 2 spaces
"set expandtab "Convert tabs to spaces.
set noexpandtab "use tab no spaces
syntax enable " allow the sintax

set autoindent " New lines inherit the indentation of previous lines.

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" LAST STATUS
set laststatus=2 "show the bar

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"" PLUGINS

"call plug#begin('/home/yahir/.config/nvim/plugged/')
call plug#begin('/home/yahir/.config/vim/plugged/')

"Themes isntall
Plug 'morhetz/gruvbox'
"Plug 'arcticicestudio/nord-vim'
"Plug 'ayu-theme/ayu-vim'


"IDE
"Plug 'Yggdroot/indentLine
"NerdTree
Plug 'preservim/nerdtree'
"move files
Plug 'christoomey/vim-tmux-navigator'
"autocomplete IA
Plug 'zxqfl/tabnine-vim'

"Icons VIm
Plug 'ryanoasis/vim-devicons'
"indeline"	
"Plug 'Yggdroot/indentLine'
"Line"
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

"Plug 'codota/tabnine-vim'
"Git fujitive"
Plug 'tpope/vim-fugitive'

call plug#end()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
"Config Plugins

"""""" set theme
set termguicolors     " enable true colors support

" gruvbox
"g:gruvbox_contrast_dark
"g:gruvbox_contrast_light
" Possible values are soft, medium and hard.
set background=dark    " Setting dark mode
"set background=light   " Setting light mode
let g:gruvbox_contrast_dark = "hard"
"let g:gruvbox_contrast_light = "soft"
"let g:gruvbox_transparent_bg=1
colorscheme gruvbox


"nord
"colorscheme nord "so trasparent

"AYU
"let ayucolor="light"  " for light version of theme
"let ayucolor="mirage" " for mirage version of theme
"let ayucolor="dark"   " for dark version of theme
"colorscheme ayu


"""" lINEAS
set listchars=tab:
"set list lcs=tab:|a
"set list 
"set listchars=tab:> 
"set listchars=tab:.·,trail:·
"set listchars=eol:¬,tab:▸\
"set listchars=eol:·,tab:⍿·,trail:×
"set listchars=tab:┌┬,trail:·
":set listchars=eol:⏎,tab:␉·,trail:␠,nbsp:⎵
"set list
"set lcs=tab:\|\  " the last character is space!
"set listchars+=space:␣
"set listchars=eol:¬,tab:>·,trail:~,extends:>,precedes:<,space:␣
"set showbreak=↪\  
"set listchars=tab:-→,eol:↲,nbsp:␣,trail:•,extends:⟩,precedes:⟨,space:•
"set list



""""" NERD TREE
let NERDTreeQuitOnOpen=1

""""" VIM ICONS
" adding to vim-airline's tabline
"let g:webdevicons_enable_airline_tabline = 1
" adding to vim-airline's statusline
let g:webdevicons_enable_airline_statusline = 1


"""" AIRLINE
let g:airline_theme='atomic' 
let g:airline_theme='gruvbox'

"""""""TABNINE


""""""""""""""""""""""""""""""""""""""""""""""""""""""
" SHORTCUTS

let mapleader=" "

" nmap <Leader> s 	
map <C-s> :w  <CR>
nmap <A-k> :source % <CR>
nmap <C-w> :q <CR>
nmap <A-p> :PlugInstall <CR>
nmap <A-b> :NERDTreeFind <CR>

vmap <C-c> "+y 
nmap <A-j> :AirlineTheme random <CR>
nmap <A-l> :AirlineTheme <CR>


