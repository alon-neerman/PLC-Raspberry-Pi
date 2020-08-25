sudo apt-get -y update;
sudo apt-get -y dist-upgrade;
sudo apt-get -y install bridge-utils;

sudo cat >/etc/network/interfaces.d/br0 <<EOL

auto eth0
allow-hotplug eth0
iface eth0 inet manual
   pre-up   ifconfig $IFACE up
   pre-down ifconfig $IFACE down

auto wlan0
allow-hotplug wlan0
iface wlan0 inet manual
   pre-up   ifconfig $IFACE up
   pre-down ifconfig $IFACE down

auto br0
iface br0 inet dhcp
bridge_ports eth0 wlan0


EOL

sudo service networking stop;
sudo service networking start;