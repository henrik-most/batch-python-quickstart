#!/bin/bash

for (( c=0; c<60; c++))
do
	echo "Script has been running for $c seconds"
	sleep 1s
done

echo "Running apt update"
sudo apt update -y
echo "Running apt install software-properties-common -y"
sudo apt install software-properties-common -y
echo "Running add-apt-repository ppa:deadsnakes/ppa -y"
sudo add-apt-repository ppa:deadsnakes/ppa -y
echo "Running sudo apt update -y"
sudo apt update -y
echo "Running apt install python3.7 -y"
sudo apt install python3.7 -y
echo "Running apt install python3-pip -y"
sudo apt install python3-pip -y
echo "Running sudo -H python3 -m pip install pip --upgrade"
sudo -H python3 -m pip install pip --upgrade
echo "Running pip install poetry"
sudo -H python3 -m pip install poetry
echo "install blob fuse"
wget https://packages.microsoft.com/config/ubuntu/18.04/packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get update -y
sudo apt-get install blobfuse fuse-y
echo "All done - Good Luck!"
