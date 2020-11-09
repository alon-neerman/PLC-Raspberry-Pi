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
