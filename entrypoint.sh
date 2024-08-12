#!/bin/bash

cd /Daamtu/Django-simple
apt-get install git -y
chmod 777 00-activate-scripts.sh
./00-activate-scripts.sh
./06-install-net-tools.sh
./08-socat-ipv6.sh
./03-create-venv.sh
source venv/bin/activate
pip install -r requirements.txt
python3 nohup.py

# Keep the container running (optional)
exec "$@"