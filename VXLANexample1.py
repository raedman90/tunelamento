#!/usr/bin/python
from mininet.net import Mininet
from mininet.link import Intf	
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def emptyNet():
	net=Mininet()

	info('***Adding controller\n')
	info('***Defining physical interface to change outside packets')
	intfName='eth1'

	info('***Adding hosts\n')
	red1=net.addHost('red1',ip='10.0.0.1',mac='00:00:00:00:00:01')
	blue1=net.addHost('blue1',ip='10.0.0.1',mac='00:00:00:00:00:01')

	info('***Adding switch\n')
	s1=net.addSwitch('s1')

	info('***Creating links\n')
	net.addLink(red1,s1)
	net.addLink(blue1,s1)

	_intf=Intf(intfName,node=s1)
	info('***Starting the network\n')
	net.start()

	info('***Running CLI\n')
	CLI( net )

	info('***Stop networking\n')
	net.stop()

if __name__=='__main__':
	setLogLevel( 'info' )
	emptyNet()
