# Ansible become mysu

## Description

This ansible project present a way to wrap the `sudo su -` command as a `become_method` to be able to use `become` in some environments where only this command is allowed for privilege escalation.

## Configuration

By default, it will launch a `sudo su - root`, but if you need to go through a generic user (`sudo su - generic_user`), simply define the var `ansible_generic_user`.

## Test

```shell
ansible-playbook --inventory-file inventory playbook.yml
```
