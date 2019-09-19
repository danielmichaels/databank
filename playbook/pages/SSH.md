# SSH

## Append file over SSH

`cat ~/.ssh/id_rsa.pub | ssh username@host.com "cat >> ~/.ssh/authorized_hosts"`

## Rysnc with SSH keyfile

`rsync -aznvP -e "ssh -i ~/ec2_keyfile.pem" ubuntu@ec2.ap-southeast-2.compute.amazonaws.com:/home/ubuntu/folder /tmp/new_folder`

