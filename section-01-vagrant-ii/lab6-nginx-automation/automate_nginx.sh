#!/bin/bash

echo "=============================="
echo " FULL NGINX AUTOMATION"
echo "=============================="

# Step 1: Update system
sudo apt update -y

# Step 2: Install Nginx
sudo apt install nginx -y

# Step 3: Enable and start nginx
sudo systemctl enable nginx
sudo systemctl start nginx

# Step 4: Deploy HTML page
sudo bash -c 'cat > /var/www/html/index.html' <<EOF
<!DOCTYPE html>
<html>
<head>
    <title>Automated Nginx Server</title>
</head>
<body>
    <h1>🚀 Web Server Deployed Automatically</h1>
    <p>This page was created using a Bash automation script.</p>
</body>
</html>
EOF

# Step 5: Restart nginx
sudo systemctl restart nginx

# Step 6: Check status
sudo systemctl status nginx --no-pager

echo "=============================="
echo " Web Server Setup Complete!"
echo "=============================="

