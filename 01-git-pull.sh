#!/bin/bash

git fetch --all
git reset --hard origin/main
git pull origin main
chmod 777 00-activate-scripts.sh
./00-activate-scripts.sh
mv 02-git-clone.sh ../
