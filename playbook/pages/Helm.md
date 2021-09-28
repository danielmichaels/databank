# Helm

-[link](https://helm.sh)
- [artificatoryhub](https://artificatoryhub.io)

## Repos

Helm accepts repositories. To add one:

`helm repo add bitnami https://charts.bitnami.com/bitnami`

**check repo list** with `helm repo list`

To then install a chart from that repo:

`helm install my-release bitnami/drupal` for instance.

**release** is like a new app
