#!/usr/bin/env bash
# Script to set up web servers for "web_static" deployment

# Install Nginx if not already installed
sudo apt-get -y update
sudo apt-get install -y nginx

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
echo "<html><head></head><body>Colly-m hbnb</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
sudo rm -rf /data/web_static/current
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/
sudo chgrp -R ubuntu:ubuntu /data/

# Update Nginx configuration
printf %s 'server {
    listen 80 default_server;
    listen [::]:80 dfault_server;
    add_header X-Served-By $HOSTNAME;
    root /var/www/html;
    index index.html index.htm;

    location /hbnb_static {
        alias /data/web_static/current/;
	index index.html index.htm;
    }
    location /redirect_me {
	return 301 http://github.com/colly-m;
    }

    error_page 404 /404.html;
    location = /404.html {
        root /var/www/html;
        internal;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}' > sudo tee /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

exit 0
