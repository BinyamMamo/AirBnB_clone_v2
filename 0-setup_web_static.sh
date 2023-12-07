#!/usr/bin/env bash
# prepares the web servers for AirBnb static

config="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
file="/etc/nginx/sites-available/default"

sudo apt-get update
sudo apt-get install nginx -y

sudo mkdir -p "/data/web_static/releases/test/"
sudo mkdir "/data/web_static/shared/"
sudo chown -hR ubuntu:ubuntu "/data/"
ln -sf "/data/web_static/releases/test/" "/data/web_static/current"

echo "Hello world" > "/data/web_static/releases/test/index.html"
sudo sed -i "29i\ $config" "$file"

sudo service nginx restart
