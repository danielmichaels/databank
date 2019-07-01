# Ansible

## Hello World

`ansible all -i "localhost," -m debug -a "msg='Hello World'"`

With inventory:

`ansible all -i ./inventory -m debug -a "msg='Now with an inventory!'"`

## Playbooks

Basic syntax

```yaml

---

  - name: Provision Vagrant
    hosts: all
    tasks:
    
      - name: Install Vim
        apt: name=vim state=present 
        become: sudo
      - name: Install Git
        apt: name=git state=latest
        become: sudo
```

In the above example we are using a `debian` based system that uses `apt` and we tell it what packages to install via the `name` argument. The two options in `state` are `present` which means, if it is on the system already, do nothing. Whereas, `latest` will update to the latest regardless.`apt` requires sudo privileges and this is set through the `become` option.

Packages can be removed with `state=absent`.

The above playbook can be simplified for multiple packages to this:

```yaml

---

  - name: Provision Vagrant
    hosts: all
    tasks:
    
      - name: Install Packages
        apt: name= state=present
        become: sudo
        with_items:
          - git
          - mtr
          - htop
          - ntp
          - vim
      - name: Remove Packages
        apt: name= state=absent
        become: sudo
        with_items:
          - emacs

```

Update and Upgrades

```yaml
