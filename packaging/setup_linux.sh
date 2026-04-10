#!/usr/bin/env bash

set -e

echo 'Install be used with sudo, confirm? [y/n]'
read -r answer
answer="${answer,,}"
if [[ "$answer" != "y" ]]; then
    echo 'Installation cancelled.'
    exit 1
fi

echo '1/4 : Installing rosorter with pipx.'
pipx install .

echo '2/4 : Creating /etc/rosorter and copying config.yaml.'
sudo mkdir /etc/rosorter
sudo cp config.yaml /etc/rosorter/
sudo chmod 644 /etc/rosorter/config.yaml

echo '3/4 : Creating .config/rosorter and copying config.yaml.'
mkdir -p ~/.config/rosorter
cp config.yaml ~/.config/rosorter/
chmod 644 ~/.config/rosorter/config.yaml

echo '4/4 : Installation complete!'
exit 0