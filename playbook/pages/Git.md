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

## Merge 

__Two projects together but keep histories__

To merge `ZZZ` into `YYY`:

```sh
cd path/to/YYY
git remote add YYY path/to/YYY
git fetch YYY --tags
get merge --allow-unrelated-histories YYY/master # or specific branch
git remote remove YYY
```

[link](https://stackoverflow.com/questions/1425892/how-do-you-merge-two-git-repositories)

Merging may cause conflicts.