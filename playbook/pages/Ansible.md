# Ansible

# Overview

Ansible gives us the ability to provision new infrastructure through the use of
automation. Using Ansible prevents administrators from having to actively manage
new or existing hosts and is particularly useful when used with large numbers of hosts.

It has five (5) primary concepts:

## Modules

  - these are the 'services' or 'packages' which are already configured and allow us to use certain functionality within Ansible.
  - the `git` module gives Ansible to power to do any `git` command programatically.
  - anyone can write a module. The complete [list](https://docs.ansible.com/ansible/latest/modules/modules_by_category.html)

### Tasks

  - this is the mechanism used to call modules within an Ansible playbook (more below)
  - organised by type of job/task that needs to be done; security and database could be two tasks

```yaml
# example of a task
- name: ensure Git is installed
  apt: name=git-core state=present update_cache=yes
  become: true
```

### Roles

- how we group tasks and variables
- allows reuse across environment and projects
- Ansible's super power


### Playbook

  - what needs to be done
  - top level collection full of tasks, variables and modules to accomplish task
  - referenced when running Ansible to indicate which "play" to run

### Inventory

  - where things need to be done; which server etc
  - typically assigned in a `hosts` file within the Ansible projects root directory.

```yaml
[common]
192.168.1.1
192.168.10.1

[database]
172.16.16.30

[webserver]
192.168.1.1
```

## Directory Layout

A rough guide to how an Ansible directory should be structured.

```shell
site.yml
webservers.yml
fooservers.yml
roles/
    common/
        tasks/
        handlers/
        files/
        templates/
        vars/
        defaults/
        meta/
    webservers/
        tasks/
        defaults/
        meta/
          main.yml <-- must be inside a folder being used
```
Any folders within the Roles must contain a `main.yml`. If any folder is not being
used, they can safely be removed. 

A break down of each folder within the template above.

- tasks - contains the main list of tasks to be executed by the role.
- handlers - contains handlers, which may be used by this role or even anywhere outside this role.
- defaults - default variables for the role.
- vars - other variables for the role.
- files - contains files which can be deployed via this role.
- templates - contains templates which can be deployed via this role.
- meta - defines some meta data for this role. See below for more details.

An example of how to use and structure Roles.

```shell
# roles/example/tasks/main.yml
- name: added in 2.4, previously you used 'include'
  import_tasks: redhat.yml
  when: ansible_facts['os_family']|lower == 'redhat'
- import_tasks: debian.yml
  when: ansible_facts['os_family']|lower == 'debian'

# roles/example/tasks/redhat.yml
- yum:
    name: "httpd"
    state: present

# roles/example/tasks/debian.yml
- apt:
    name: "apache2"
    state: present
```

## Commands

### Hello World

`ansible all -i "localhost," -m debug -a "msg='Hello World'"`

With inventory:

`ansible all -i ./inventory -m debug -a "msg='Now with an inventory!'"`

### Playbooks

Basic syntax

```yaml

---

  - name: Provision Vagrant
    hosts: all
    tasks:
    
      - name: Install Vim
        apt: name=vim state=present 
        become: sudo
      - name: Install [Git](Git)
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
```
