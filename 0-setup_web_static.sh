#!/usr/bin/env bash
# A script that sets up your web servers for the deployment of web_static

# Install nginx
apt-get update && sudo apt-get install nginx -y
ufw allow 'Nginx HTTP'

# Create directories / folders
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Fake HTML file
echo "
<html>
<head>
<title></title>
</head>
<body> Hello Nginx Configured </body>
</html>
" > /data/web_static/releases/test/index.html

# Create symbolic link
LINK=/data/web_static/current
TARGET=/data/web_static/releases/test/
ln -sf "$TARGET" "$LINK"

# Ownership to User and Group
chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
NGINX_CONF="/etc/nginx/sites-available/default"
sed -i "/server_name _;/a \\\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}" "$NGINX_CONF"

# restart nginx service
service nginx restart