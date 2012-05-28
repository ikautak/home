
set tags=~/.tags

"previous cursor pos
autocmd BufReadPost * if line("'\"") > 0 && line("'\"") <= line("$") | exe "normal g`\"" | endif

"show char code and linefeed
set statusline=%<%f\%m%r%h%w%{'['.(&fenc!=''?&fenc:&enc).']['.&ff.']'}%y%=%l,%c%V%8P

"space
highlight WhitespaceEOL ctermbg=red guibg=red
match WhitespaceEOL /\s\+$/
autocmd WinEnter * match WhitespaceEOL /\s\+$/

"cuda
au BufNewFile,BufRead *.cuh set ft=cuda

"golang
set rtp+=$HOME/go/misc/vim
filetype plugin indent on
syntax on

set whichwrap=b,s,<,>,[,]

set number
set ruler
set cmdheight=2
set laststatus=2
set title
set linespace=0

set autoindent
set cindent
set showmatch
set backspace=indent,eol,start
set pastetoggle=<F12>

set tabstop=4
set expandtab
set smarttab
set shiftwidth=4
set shiftround
set nowrap

set hlsearch

"set list
"set listchars=tab:>\

set fileformats=unix,dos,mac

if exists('&ambiwidth')
    set ambiwidth=double
endif

