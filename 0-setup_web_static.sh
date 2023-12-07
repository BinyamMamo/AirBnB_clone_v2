config="\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
file="/etc/nginx/sites-available/default"

apt-get update
apt-get install nginx -y

mkdir -p "/data/web_static/releases/test/"
mkdir "/data/web_static/shared/"
chown -hR ubuntu:ubuntu "/data/"
ln -sf "/data/web_static/releases/test/" "/data/web_static/current"

echo "Hello world" > "/data/web_static/releases/test/index.html"
sed -i "29i\ $config" "$file"

service nginx restart
