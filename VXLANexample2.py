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
	red2=net.addHost('red2',ip='10.0.0.2',mac='00:00:00:00:00:02')
	blue2=net.addHost('blue2',ip='10.0.0.2',mac='00:00:00:00:00:02')

	info('***Adding switch\n')
	s2=net.addSwitch('s2')

	info('***Creating links\n')
	net.addLink(red2,s2)
	net.addLink(blue2,s2)

	_intf=Intf(intfName,node=s2)
	info('***Starting the network\n')
	net.start()

	info('***Running CLI\n')
	CLI( net )

	info('***Stop networking\n')
	net.stop()

if __name__=='__main__':
	setLogLevel( 'info' )
	emptyNet()
