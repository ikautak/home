
"set tags=~/.tags

set number
set ruler
set cmdheight=2
set laststatus=2
set title
set nowrap
set whichwrap=b,s,<,>,[,]
set backspace=indent,eol,start

set autoindent
set cindent
set showmatch

set tabstop=4
set shiftwidth=4
set shiftround
set expandtab
set smarttab

set ignorecase
set smartcase
set hlsearch

set wildmenu

set pastetoggle=<F12>

set fileformats=unix,dos,mac

"zenkaku
if exists('&ambiwidth')
    set ambiwidth=double
endif

"char code and linefeed code
set statusline=%<%f\%m%r%h%w%{'['.(&fenc!=''?&fenc:&enc).']['.&ff.']'}%y%=%l,%c%V%8P

"remember previous cursor pos
autocmd BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$") | exe "normal g`\"" | endif

"white space
highlight WhitespaceEOL ctermbg=red guibg=red
match WhitespaceEOL /\s\+$/
autocmd WinEnter * match WhitespaceEOL /\s\+$/

"cuda
au BufNewFile,BufRead *.cuh set ft=cuda

"golang
set rtp+=$HOME/go/misc/vim
filetype plugin indent on
syntax on

"diff with last saved state
command DiffOrig vert new | set bt=nofile | r # | 0d_ | diffthis | wincmd p | diffthis

