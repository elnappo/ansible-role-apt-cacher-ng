# ansible-role-apt-cacher-ng
[![Build Status](https://travis-ci.org/elnappo/ansible-role-apt-cacher-ng.svg?branch=master)](https://travis-ci.org/elnappo/ansible-role-apt-cacher-ng)

Simply installs and start apt-cacher-ng on boot. Get more informations about apt-cacher-ng at https://www.unix-ag.uni-kl.de/~bloch/acng/

## Requirements
Ubuntu or Debian

## Role Variables
None.

## Dependencies
None.

## Example Playbook
    - hosts: servers
      roles:
         - { role: elnappo.apt-cacher-ng }

## Client configuration
### with ansible
Set apt_proxy as a host var

**For the whole system:**

	- name: Set up apt proxy
  	  template: src=templates/apt_proxy.conf dest=/etc/apt/apt.conf.d/01proxy owner=root group=root mode=0644
 	  when: ansible_os_family == "Debian" and apt_proxy
 	  
templates/apt_proxy.conf:

	Acquire::http { Proxy "http://{{apt_proxy}}"; };

**Only for one task:**

	- apt: name=cobbler state=installed
	  environment: apt_proxy
      
### without ansible
Replace server IP/FQDN!

	$ echo "Acquire::http { Proxy "http://127.0.0.1:3142"; };" > /etc/apt/apt.conf.d/01proxy

## License

MIT

## Author Information

elnappo <elnappoo@gmail.com>
