# SSH

## Append file over SSH

`cat ~/.ssh/id_rsa.pub | ssh username@host.com "cat >> ~/.ssh/authorized_hosts"`
