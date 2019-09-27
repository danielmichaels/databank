# SSH

<!-- vim-markdown-toc GFM -->

+ [SSH](#ssh)
  * [Append file over SSH](#append-file-over-ssh)
  * [Rsync with SSH keyfile](#rsync-with-ssh-keyfile)
+ [SCP](#scp)

<!-- vim-markdown-toc -->

# SSH

## Append file over SSH

`cat ~/.ssh/id_rsa.pub | ssh username@host.com "cat >> ~/.ssh/authorized_hosts"`

## Rsync with SSH keyfile

`rsync -aznvP -e "ssh -p 2220 -i ~/ec2_keyfile.pem" ubuntu@ec2.ap-southeast-2.compute.amazonaws.com:/home/ubuntu/folder /tmp/new_folder`

Also to get a detailed summary of what was send and in human readable form use `--stats -h`.


# SCP

- `scp` respects `.ssh/config`.

But, it doesn't understand wildcard matches for files. A workaround exists:

```sh
# will not work
scp -r target:/root/file-* /tmp/dir # fails

#works
scp -r 'target:/root/file-*' /tmp/dir # works
```
