import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_apt_cacher_ng_server_is_installed(host):
    apt_cacher_ng = host.package('apt-cacher-ng')

    assert apt_cacher_ng.is_installed


def test_apt_cacher_ng_is_running(host):
    apt_cacher_ng = host.service('apt-cacher-ng')

    assert apt_cacher_ng.is_running
    assert apt_cacher_ng.is_enabled


def test_apt_cacher_ng_is_listening(host):
    assert host.socket("tcp://0.0.0.0:1337").is_listening
