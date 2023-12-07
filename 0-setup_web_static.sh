#!/usr/bin/env bash
# prepares the web server for deployment

sudo apt update -y
sudo apt install nginx -y

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared/
chown ubuntu:ubuntu -R /data

echo "hello world" > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

echo "
server {
	listen 80;
	server_name www.binyammamo.tech;
	location /hbnb_static {
		alias /data/web_static/current/;
	}
}
" > /etc/nginx/sites-available/hbnb_static.conf

sudo ln -sf /etc/nginx/sites-available/hbnb_static.conf /etc/nginx/sites-enabled/hbnb_static.conf

sudo service nginx restart
