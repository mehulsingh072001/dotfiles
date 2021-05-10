set nocompatible              " be iMproved, required
filetype plugin on                  " required

" set the runtime path to include Vundle and initialize
set splitbelow
set rtp+=~/.vim/bundle/Vundle.vim
syntax on 
set  rtp+=/usr/local/lib/python3.8/dist-packages/powerline/bindings/vim/
au FileType * setlocal formatoptions-=c formatoptions-=r formatoptions-=o
set laststatus=2
set t_Co=256
set noerrorbells
set tabstop=4 softtabstop=4
set shiftwidth=4
set expandtab
set smartindent
set nu
set nowrap
set smartcase
set noswapfile
set nobackup
set undodir=~/.vim/undodir
set undofile
set incsearch
set relativenumber
set textwidth=100
set clipboard+=unnamedplus
set mouse=nv

"guifont
set guifontset="Droid Sans Mono"
highlight ColorColumn ctermbg=0 guibg=lightgrey

if (has('termguicolors'))
  set termguicolors
endif

call plug#begin('~/.vim/plugged')
Plug 'francoiscabrol/ranger.vim'
Plug 'prettier/vim-prettier', { 'do': 'yarn install' }
Plug 'ap/vim-css-color'
Plug 'morhetz/gruvbox'
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
Plug 'junegunn/fzf.vim'
"Plug 'vimwiki/vimwiki'
 Plug 'joshdick/onedark.vim'
Plug 'stsewd/fzf-checkout.vim'
Plug 'neoclide/coc.nvim', {'branch': 'release'}
Plug 'jremmen/vim-ripgrep'
Plug 'tpope/vim-fugitive'
"Plug 'jreybert/vimagit'
Plug 'ryanoasis/vim-devicons'
Plug 'terryma/vim-multiple-cursors'
Plug 'preservim/nerdcommenter'
Plug 'vim-utils/vim-man'
Plug 'preservim/nerdtree'
Plug 'mattn/emmet-vim'
"Plug 'itchyny/lightline.vim'
Plug 'sheerun/vim-polyglot'
Plug 'hzchirs/vim-material'
Plug 'StanAngeloff/php.vim'
"Plug 'wfxr/minimap.vim'
Plug 'dracula/vim', { 'as': 'dracula' }

call plug#end()

call vundle#begin()
"Plugin 'tomasiser/vim-code-dark'
"Plugin 'joshdick/onedark.vim'
Plugin 'eslint/eslint'
Plugin 'mbbill/undotree'
Plugin 'dense-analysis/ale'
Plugin 'isRuslan/vim-es6'
Plugin 'tpope/vim-commentary'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'Yggdroot/indentLine'
Plugin 'chrisbra/csv.vim'
Plugin 'alvan/vim-closetag'
call vundle#end()

set runtimepath^=~/.vim/bundle/ctrlp.vim

let g:material_style= 'palenight'
set background=dark
colorscheme onedark
"colorscheme dracula


if executable('rg')
    let g:rg_derive_root='true'
endif

let mapleader = " "
let g:netrw_browse_split=2
let g:newtrw_banner = 0
let g:netrw_winsize = 25
let g:ctrlp_use_caching = 0
set rtp+=$HOME/.local/lib/python3.8/site-packages/powerline/bindings/vim/

"remappings
imap jj <Esc>
nnoremap <leader>w :w <CR>
nnoremap <leader>1 :tabn 1 <CR> 
nnoremap <leader>2 :tabn 2 <CR> 
nnoremap <leader>3 :tabn 3 <CR> 
nnoremap <leader>4 :tabn 4 <CR> 
nnoremap <leader>5 :tabn 5 <CR> 
nnoremap <leader>t :tabn <CR> 
nnoremap <leader>T :tabN <CR> 
nnoremap <leader>h :wincmd h<CR>
nnoremap <leader>j :wincmd j<CR>
nnoremap <leader>k :wincmd k<CR>
nnoremap <leader>l :wincmd l<CR>
nnoremap <leader>u :UndotreeShow<CR>
nnoremap <leader>pv :wincmd v<bar> :Ex <bar> :vertical resize 30<CR>
nnoremap <leader>ps :Rg<SPACE>
nnoremap <silent> <Leader>+ :vertical resize +5<CR>
nnoremap <silent> <Leader>- :vertical resize +5<CR>
imap hh <C-y>,


"nerdtre settings
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
let g:NERDTreeGitStatusUpdateOnCursorHold = 1
map <leader><tab> :NERDTreeToggle<CR>
set completeopt+=menuone   " show the popup menu even when there is only 1 match
set completeopt+=preview

filetype plugin indent on
"let g:indentLine_char = "🡒"
let g:indentLine_char = "|"
let g:indentLine_setColors = 1
set runtimepath^=~/.vim/bundle/ctrlp.vim
let b:ale_linters = ['pyflakes', 'flake8', 'pylint']
let b:ale_fixers = ['eslint']

let b:ale_fix_on_save = 1

" Equivalent to the above.

let &t_SI = "\e[6 q"
let &t_EI = "\e[2 q"

" optional reset cursor on start:
augroup myCmds
au!
autocmd VimEnter * silent !echo -ne "\e[2 q"
augroup END

let g:ctrlp_map = '<leader>..'
let g:ctrlp_cmd = 'CtrlP'

"coc completions
" TextEdit might fail if hidden is not set.
set hidden

" Some servers have issues with backup files, see #649.
set nobackup
set nowritebackup

" Give more space for displaying messages.
set cmdheight=2

" Having longer updatetime (default is 4000 ms = 4 s) leads to noticeable
" delays and poor user experience.
set updatetime=300

" Don't pass messages to |ins-completion-menu|.
set shortmess+=c

" Always show the signcolumn, otherwise it would shift the text each time
" diagnostics appear/become resolved.
if has("patch-8.1.1564")
  " Recently vim can merge signcolumn and number column into one
  set signcolumn=number
else
  set signcolumn=yes
endif

" Use tab for trigger completion with characters ahead and navigate.
" NOTE: Use command ':verbose imap <tab>' to make sure tab is not mapped by
" other plugin before putting this into your config.
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction

" Use <c-space> to trigger completion.
if has('nvim')
  inoremap <silent><expr> <c-space> coc#refresh()
else
  inoremap <silent><expr> <c-@> coc#refresh()
endif

" Use <cr> to confirm completion, `<C-g>u` means break undo chain at current
" position. Coc only does snippet and additional edit on confirm.
" <cr> could be remapped by other vim plugin, try `:verbose imap <CR>`.
if exists('*complete_info')
  inoremap <expr> <cr> complete_info()["selected"] != "-1" ? "\<C-y>" : "\<C-g>u\<CR>"
else
  inoremap <expr> <cr> pumvisible() ? "\<C-y>" : "\<C-g>u\<CR>"
endif

" GoTo code navigation.
nmap <silent> gd <Plug>(coc-definition)
"stupid
nmap <silent> gy <Plug>(coc-type-definition) nmap <silent> gi <Plug>(coc-implementation) nmap <silent> gr <Plug>(coc-references)

"git
nmap <leader>gs :G<CR>
nmap <leader>gm :Gcommit<CR>
nmap <leader>gp :Gpush<CR>

" Use K to show documentation in preview window.
nnoremap <silent> K :call <SID>show_documentation()<CR>


" Highlight the symbol and its references when holding the cursor.
autocmd CursorHold * silent call CocActionAsync('highlight')

" Formatting selected code.
xmap <leader>f  <Plug>(coc-format-selected)
nmap <leader>f  <Plug>(coc-format-selected)

" Use CTRL-S for selections ranges.
" Requires 'textDocument/selectionRange' support of LS, ex: coc-tsserver
nmap <silent> <C-s> <Plug>(coc-range-select)
xmap <silent> <C-s> <Plug>(coc-range-select)

" Add (Neo)Vim's native statusline support.
" NOTE: Please see `:h coc-status` for integrations with external plugins that
" provide custom statusline: lightline.vim, vim-airline.
set statusline^=%{coc#status()}%{get(b:,'coc_current_function','')}

let g:airline_theme = 'onedark'

let g:airline_powerline_fonts = 1
let g:codedark_conservative = 1

let g:airline#extensions#tabline#enabled = 1
let g:airline#extensions#tabline#formatter = 'unique_tail'
let g:ctrlp_cache_dir = $HOME . '/.cache/ctrlp'
if executable('ag')
  let g:ctrlp_user_command = 'ag %s -l --nocolor -g ""'
endif
let g:ctrlp_user_command = ['.git/', 'git ls-files --cached --others  --exclude-standard %s']
let g:airline#extensions#tabline#show_buffers = 0

let g:ctrlp_custom_ignore = {
  \ 'dir':  './node_modules/',
  \ }

set runtimepath^=~/.vim/bundle/ctrlp.vim

"map <Leader>tt :new term://zsh<CR>

" Toggle 'default' terminal
nnoremap <Leader>ot :call ChooseTerm("term-slider", 1) <CR>

" Start terminal in current pane
nnoremap <Leader>nt :call ChooseTerm("term-pane", 0)<CR>

function! ChooseTerm(termname, slider)
	let pane = bufwinnr(a:termname)
	let buf = bufexists(a:termname)
	if pane > 0
		" pane is visible
		if a:slider > 0
			:exe pane . "wincmd c"
		else
			:exe "e #" 
		endif
	elseif buf > 0
		" buffer is not in pane
		if a:slider
			:exe "belowright split"
		endif
		:resize 14 | exe "buffer " . a:termname
	else
		" buffer is not loaded, create
		if a:slider
			:exe "belowright split"
		endif
		:startinsert | resize 14 | terminal 
		:exe "f " a:termname
	endif
endfunction
tnoremap jj <C-\><C-n>
