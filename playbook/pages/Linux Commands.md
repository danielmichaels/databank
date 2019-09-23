# Assorted Linux Helpers

An assortment of helpful unix commands

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

## fg & bg

`CTRL-Z` to suspend a job to the background and then run `fg` to bring it back. 

If there are many jobs in the background you can identify the one you want to resume by calling `jobs`. This will output a reference `%job_id` e.g. `[1]` and `fg %1` will bring it back into the foreground.

`CTRL-Z` suspends a process to the background and `fg` resumes it. `bg` will push a process to the background but keep it running.

## Grep

`ps aux | grep <expr>` will always return `true` because it finds its own running process. Get around this by removing grep from the `ps` process list.

`ps aux | grep -v 'grep' | grep <expr>` or `ps aux | grep '[e]xpr'`

