# Vagrant

## Basics 

- Install Ubuntu Trust 64bit:
  - `vagrant box add ubuntu/trusty64`
- Initialise it in current directory:
  - `vagrant init ubuntu/trust64`
- start vagrant box:
  - `vagrant up`
- self explanatory:
  - `vagrant status`
  - `vagrant suspend`
  - `vagrant shutdown`
  - `vagrant destroy`

## Vagrantfile

`Vagrantfile` can be altered. Here is an example of how we integrate it with `ansible` for testing.

```ruby
# -*- mode: ruby -*-
# vi: set ft=ruby :

# For a complete reference, please see the online documentation at
# https://docs.vagrantup.com.

Vagrant.configure(2) do |config|

  # VM Image - Ubuntu v14.04
  config.vm.box = "ubuntu/trusty64"

  # VM Resources
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus   = 1
  end

  # Provision with Ansible
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "vagrant.yml"
  end

end
```

