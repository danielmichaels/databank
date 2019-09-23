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

## Gitea raw links

Gitea, a minimial git server built on top of `go` has slightly different raw image links to `github`.

- `https://<address>/<user>/<proj_name>/raw/branch/<master>/<image_locations>/<image_name.ext>`

## Credential save

On HTTP connections by default user credentials must be entered each time unless cached. 

- Set global cache to default (15 minutes):

`git config --global credential.helper cache`

- To set the local git repo to cache credentials for 1 day:

`git config --local credential.helper 'cache --timeout 86400'`
