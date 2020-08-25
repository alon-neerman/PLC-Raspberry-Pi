#!/bin/bash

echo "Please enter in the IP address of the Raspberry Pi"
read IP_ADDRESS

echo "Please enter in the default gateway of the network"
read GATEWAY

DNS=$GATEWAY

echo "interface eth0"  >> dhcpcd.conf

echo "static ip_address=$IP_ADDRESS/24" >> dhcpcd.conf
echo "static routers=$GATEWAY" >> dhcpcd.conf
echo "static domain_name_servers=$DNS" >> dhcpcd.conf

touch /Volumes/boot/ssh;
sudo mv -f dhcpcd.conf /Volumes/raspberry/etc/dhcpcd.conf;

#cat >wpa_supplicant.conf <<EOL
#country=US
#ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
#update_config=1
#network={
#    ssid="${SSID}"
#    psk="${PASSWORD}"
#}
#
#EOL
#
#
#sudo mv -f wpa_supplicant.conf /Volumes/boot/wpa_supplicant.conf
