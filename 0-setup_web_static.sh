#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

# Installation and updation of nginx
sudo apt-get update
sudo apt-get install -y nginx
sudo ufw allow 'Nginx HTTP'

# Creates necessary directories if not present
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Creates a fake html file
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html><head></head><body>Colly-m page</body></html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Gives ownership to ubuntu user ond group
sudo chown -R ubuntu /data/

# Updates Nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restarts nginx
sudo service nginx restart
