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

