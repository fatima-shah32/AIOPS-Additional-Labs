#!/usr/bin/env python3

from mininet.net import Mininet
from mininet.node import Controller, OVSKernelSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink


def create_virtual_wan():
    """
    Simulated Azure Virtual WAN hub-and-spoke topology.

    Hub Network:
    h1, h2 = Datacenter hosts

    Branch Networks:
    h3 = Branch 1
    h4 = Branch 2
    h5 = Branch 3
    """

    net = Mininet(
        controller=Controller,
        switch=OVSKernelSwitch,
        link=TCLink
    )

    info("*** Adding controller\n")
    c0 = net.addController("c0")

    info("*** Adding Virtual WAN hub switch\n")
    hub_switch = net.addSwitch("s1", cls=OVSKernelSwitch)

    info("*** Adding branch office switches\n")
    branch1_switch = net.addSwitch("s2", cls=OVSKernelSwitch)
    branch2_switch = net.addSwitch("s3", cls=OVSKernelSwitch)
    branch3_switch = net.addSwitch("s4", cls=OVSKernelSwitch)

    info("*** Adding hosts\n")

    hub_host1 = net.addHost("h1", ip="10.0.1.10/24")
    hub_host2 = net.addHost("h2", ip="10.0.1.11/24")

    branch1_host = net.addHost("h3", ip="10.0.2.10/24")
    branch2_host = net.addHost("h4", ip="10.0.3.10/24")
    branch3_host = net.addHost("h5", ip="10.0.4.10/24")

    info("*** Creating host-to-switch links\n")

    net.addLink(hub_host1, hub_switch)
    net.addLink(hub_host2, hub_switch)

    net.addLink(branch1_host, branch1_switch)
    net.addLink(branch2_host, branch2_switch)
    net.addLink(branch3_host, branch3_switch)

    info("*** Creating WAN links with bandwidth and delay\n")

    net.addLink(hub_switch, branch1_switch, bw=100, delay="20ms")
    net.addLink(hub_switch, branch2_switch, bw=50, delay="30ms")
    net.addLink(hub_switch, branch3_switch, bw=75, delay="25ms")

    info("*** Starting network\n")

    net.build()
    c0.start()

    hub_switch.start([c0])
    branch1_switch.start([c0])
    branch2_switch.start([c0])
    branch3_switch.start([c0])

    info("*** Virtual WAN topology created successfully\n")
    info("*** Hub Network: 10.0.1.0/24\n")
    info("*** Branch 1 Network: 10.0.2.0/24\n")
    info("*** Branch 2 Network: 10.0.3.0/24\n")
    info("*** Branch 3 Network: 10.0.4.0/24\n")
    info("*** Use pingall to test basic connectivity\n")

    CLI(net)

    info("*** Stopping network\n")
    net.stop()


if __name__ == "__main__":
    setLogLevel("info")
    create_virtual_wan()
