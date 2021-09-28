# Kubernetes Theory

- [RaspberryPi_Cluster](RaspberryPi_Cluster.md)
- [Minikube and Kubectl](minikube_kubectl.md)
- [Helm](Helm.md)
- 

## Cluster

Consists of two parts:
1. Control Plane: co-ordinates the Cluster
2. Nodes: workers that run applications

Cluster > Control Plane > n * Nodes 

### Control Plane

Responsible for managing the cluster. Co-ordinates all the activities in your cluster.

Responsibilities:
- scheduling
- maintaining state
- scaling apps
- rolling out updates

### Node

Nodes are VM's or physical computers that act as worker machines. Each node has a 
Kubelet which is an agent for managing the node and communicating with the control plane

Nodes should have:

- container manager such as podman (containerd) or docker

There should be a minimum of three (3) nodes.


