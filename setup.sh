echo Please Allow Up To 2 Minutes....


apt update
sleep 2
apt upgrade
sleep 2
apt install python3 
sleep 2
apt install python3-pip
sleep 2
pip3 install -r /root/sexmaster/requirements.tx

cd sexmaster
python3 setup.py
sleep 20
rm -rf setup.py
