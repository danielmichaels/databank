# Bash or shell scripts

A collection of useful bash or shell commands and snippets

## Disk usage

__Summary__

- Get current working directory and sub directories human readable total:
  - `du -sh`
- Print total with any other `du` command:
  - `du -h --total`

__Folders__

- find top 5 biggest folders by size:
  - `du -sH | sort -rh | head -n 5` 

__Files__

- find top 5 biggest files:
  - `find -type f -exec du -Sh {} + | sort -rh | head -n 5`

## 

