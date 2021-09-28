# Minikube and Kubectl

**Alias'** I use alias' heavily and the following commands are now referred to as:

`mk`: `minikube`
`k`: `minikub kubectl --` # this is for a local minikube where I don't have `kubectl` installed locally

## Minikube

`mk start --driver=virtualbox` or `kvm` or `docker`

`mk ip` get ip of the cluster

`mk ssh` ssh into the master 
## Kubectl

**create**

`k create deployment deployment-name --image=danielmichaels/kube-trg-hello-go:1.0.0`

**delete pod**

`k delete pod <name>`: deletes a pod

**edit**
`k edit deployment <deployment-name>`

this will drop into a yaml file where you can make changes to the deployment

**viewing pods**

`k get pods -A`: shows all pods

`k get deployment <name>` will give a basic overview of an individual deployment

`k get pod -l app=my-app` this gets a pod with a `label` of `my-app`

`k describe pod -l app=my-app` will give detailed information on that pod
^use a describe when checking errors

**exposing pods**

pods are not automatically exposed

`k expose deployment <name> --port=<host> --target-port=<containerPort> --type=NodePort`

`NodePort` will run in k8s and randomly assign port but correctly route traffic to that service.

check the service is exposed with: `k get service <name>`

to curl the service (in this case danielmichaels/kube-trg-hello-go:1.0.0) we would do the following:

1. `k get service <name>` (get the port) (`k get svc` is shortcut)
2. `mk ip` get ip
3. curl ip:port 

**logging**

`k logs -f -l app=<name>`: shows logs and follows
`k logs -f -l app=<name> --prefix=true`: prefix shows which pod routed the request

**yaml**

`k get svc -o yaml`: output the services `yaml` to the terminal

### Deployments

**update deployment**

you can edit a `yaml` file manually and change the container image. (least preferred)

`k set image deployment/<name> <containerName>=<newContainerImage>`

kubernetes will then fire this update by rolling (can be configured how you want but this is default) all the updates. It will pull and terminate as each on comes online.

**note:** issues can arise in applications if they aren't happy with running old/new at the same time. this is a app developer issue not kubernetes.

**revert deployment**

`k rollout history deployment <name>`
rollout will drop back to an older revision.

to do the actual rollout: `k rollout undo deployment <name>`

**note:** you app really needs to be able to actually roll out without exploding, a la django!

### Secrets

Setting docker registry creds for a kube can be done like so

`k create secret docker-registry regcred \
--docker-username=danielmichaels \
--docker-password=<token> \ # access token needs to be created
--docker-email=myemail@email`

Check the secrets with `k get secrets`
