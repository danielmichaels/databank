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
