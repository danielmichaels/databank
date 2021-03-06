# Vimwiki Helpers

## Images

Place images in the `vimwiki` folder by prefixing the image file with the following link:

 `https://github.com/danielmichaels/dwiki/blob/master/images/` 

## Key bindings

Normal mode:

 * `<Leader>ww` -- Open default wiki index file.
 * `<Leader>wi` -- Open diary index
 * `<Leader>wt` -- Open default wiki index file in a new tab.
 * `<Leader>ws` -- Select and open wiki index file.
 * `<Leader>wd` -- Delete wiki file you are in.
 * `<Leader>wr` -- Rename wiki file you are in.
 * `<Enter>` -- Follow/Create wiki link
 * `<Shift-Enter>` -- Split and follow/create wiki link
 * `<Ctrl-Enter>` -- Vertical split and follow/create wiki link
 * `<Backspace>` -- Go back to parent(previous) wiki link
 * `<Tab>` -- Find next wiki link
 * `<Shift-Tab>` -- Find previous wiki link
 * `<gt>` -- Change to next tab
 * `<gT>` -- Change to previous tab
 * `<C-Space>` -- Create todo check box. Press again to mark complete.
 * `<Leader>dd` -- :Diary
 * `<Leader>ch` -- :CalendarH (Horizontal)
 * `<Leader>c` -- :Calendar (Vertical)
 * `<Leader>md` -- Starts markdown preview in default browser
 * `<Leader>img` -- Inserts the `vimwiki` GitHub image URL address

For more keys, see `:h vimwiki-mappings`

## Commands

 * `:VimWiki2HTML` -- Convert current wiki link to HTML
 * `:VimWikiAll2HTML` -- Convert all your wiki links to HTML
 * `:help vimwiki-commands` -- list all commands
 * `:help vimwiki` -- General vimwiki help docs
 * `:VWS /pattern/` -- Global search of vimwiki

## Changing Wiki Syntax

VimWiki currently ships with 3 syntaxes: VimWiki (default), Markdown
(markdown), and MediaWiki (media)

If you would prefer to use either Markdown or MediaWiki syntaxes, set the
following option in your .vimrc:

```vim

let g:vimwiki_list = [{'path': '~/vimwiki/',
                      \ 'syntax': 'markdown', 'ext': '.md'}]

```

## Getting help

**Have a question?**  
Visit the IRC channel [`#vimwiki`](https://webchat.freenode.net/?channels=#vimwiki) on Freenode ([webchat](https://webchat.freenode.net/?channels=#vimwiki), also synced to Matrix/Riot: `#vimwiki:matrix.org`) or post to the [mailing list](https://groups.google.com/forum/#!forum/vimwiki).

