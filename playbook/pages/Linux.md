# Linux 

Collections of `linux` related stuff

## Printers on Arch

Until printers just work, it'll never be _the year of the linux desktop_. These at a minimum should get printers working on Archlinux.

`sudo pacman -S cups cups-filters cups-pdf ghostscript gsfonts foomatic-db-engine foomatic-db foomatic-db-ppds foomatic-db-nonfree foomatic-db-nonfree-ppds gutenprint foomatic-db-gutenprint-ppds system-config-printer` 

## Soft and Hard links

![inode](https://github.com/danielmichaels/databank/playbook/blob/master/images/inode-links.jpg 'inode in soft and hardlinks')

__When to use Soft Links__

- When you want to link across the file system
- Directories cannot have hard links so must be soft linked

__When to use Hard Links__

- If you want to make sure your data is safe.
- Moving files, hard links won't break but soft links will
- Need to save storage space (soft links are ~4KB each)

