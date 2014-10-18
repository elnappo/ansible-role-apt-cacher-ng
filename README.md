ansible-role-apt-cacher-ng
=========
[![Build Status](https://travis-ci.org/elnappo/ansible-role-apt-cacher-ng.svg?branch=master)](https://travis-ci.org/elnappo/ansible-role-apt-cacher-ng)
Simply installs and start apt-cacher-ng on boot. Get more informations about apt-cacher-ng at [https://www.unix-ag.uni-kl.de/~bloch/acng/]()

Requirements
------------

Ubuntu or Debian

Role Variables
--------------

None.

Dependencies
------------

None.

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: elnappo.apt-cacher-ng }

License
-------

MIT

Author Information
------------------

elnappo <elnappoo@gmail.com>
