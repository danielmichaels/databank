# Docker

<!-- vim-markdown-toc GFM -->

+ [Snippets](#snippets)
  * [Purging All Unused or Dangling Images, Containers, Volumes, and Networks](#purging-all-unused-or-dangling-images-containers-volumes-and-networks)
  * [Removing Docker Images](#removing-docker-images)

<!-- vim-markdown-toc -->

# Snippets

## Purging All Unused or Dangling Images, Containers, Volumes, and Networks

`docker system prune`

To remove _any_ stopped containers and all __unused__ images (not just dangling images) add the `-a` flag.

`docker system prune -a`

## Removing Docker Images

To remove a specific image, first list all the images with `docker images -a`. Then to remove an image run `docker rmi <image name>`
