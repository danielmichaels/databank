# Linux 

<!-- vim-markdown-toc GFM -->

* [Linux General](#linux-general)
  - [Observability tools](#observability-tools)
  - [Soft and Hard links](#soft-and-hard-links)
  - [Count file in dir/](#count-file-in-dir)
* [Debian Specific](#debian-specific)
  - [Printers on Arch](#printers-on-arch)
  - [SSH Auth Logs](#ssh-auth-logs)
* [RHEL/CentOS/Fedora specific](#rhelcentosfedora-specific)
  - [SSH Auth Logs](#ssh-auth-logs-1)

<!-- vim-markdown-toc -->

Collections of `linux` related stuff

## Linux General

### Observability tools

![observability tools](https://raw.githubusercontent.com/danielmichaels/databank/master/playbook/images/linux-obserability-tools.png 'linux observabiliity tools')

### Soft and Hard links

![inode image](https://raw.githubusercontent.com/danielmichaels/databank/master/playbook/images/inode-links.jpg)

__When to use Soft Links__

- When you want to link across the file system
- Directories cannot have hard links so must be soft linked

__When to use Hard Links__

- If you want to make sure your data is safe.
- Moving files, hard links won't break but soft links will
- Need to save storage space (soft links are ~4KB each)

### Count file in dir/

two methods:

- `ls -la | wc -l`
- `find /DIRNAME -type f | wc -l`

## Debian Specific

### Printers on Arch

Until printers just work, it'll never be _the year of the linux desktop_. These at a minimum should get printers working on Archlinux.

`sudo pacman -S cups cups-filters cups-pdf ghostscript gsfonts foomatic-db-engine foomatic-db foomatic-db-ppds foomatic-db-nonfree foomatic-db-nonfree-ppds gutenprint foomatic-db-gutenprint-ppds system-config-printer` 


### SSH Auth Logs

- `cat /var/log/auth.log`

## RHEL/CentOS/Fedora specific

### SSH Auth Logs

- `cat /var/log/secure` ! may need sudo rights

