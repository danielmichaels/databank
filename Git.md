# Git

## Set username/password

I run two accounts, one for work and one personal.

All work accounts live within a folder structure, my personal repo's are much less organised! To make sure any git repo that is created within my work folders automatically commits under my work alias I do the following.

In the root directory folder.

```sh
# prob $HOME/.gitconfig
[user]
  name = itsme
  email = itsme@email.com
  
[includeIf "gitdir:~/workFolder/"]
  path = ~/workFolder/.gitconfig
```

In the `workFolder` create a `.gitconfig` file with the following:

```sh
[user]
  email = itsme@email.com
```
