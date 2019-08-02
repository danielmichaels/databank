# Snippets

Bash snippets or memory joggers.


### Guard clause

Check is argument is missing and exit if so.

```sh
if [ $# -eq 0 ]
  then
    echo "Missing argument"
    exit
fi
```

### Check arguments supplied

To check if arguments have been supplied when running argument from cli.

```sh
if [ -z "$1" ]
  then
    echo "Missing recipient argument \
      eg username@gmail.com"
    exit
elif [ -z "$2" ]
then
  echo "Missing from argument \
    eg me@myemail.com"
  exit
else
  <do command>
fi
```

### Uptime

`cat /proc/uptime`
`>> 2342.34 2100.2`
The first number is uptime in seconds and the second is the how much each core has spent in an idle state.

To get only the uptime, use `awk '{print $1} /proc/uptime`

### Set proxy

`export http_proxy=127.0.0.1:8080`
`export https_proxy=127.0.0.1:8080`

Remove proxy via `unset` commands

### While Loops

__Count down timer__

```sh
#!/bin/sh

secs=3600                         # Set interval (duration) in seconds.
endTime=$(( $(date +%s) + secs )) # Calculate end time.

while [ $(date +%s) -lt $endTime ]; do  # Loop until interval has elapsed.
    # ...
done
```
