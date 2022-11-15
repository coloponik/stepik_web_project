cd /home/user1/web/ask/ask
gunicorn --pythonpath="/home/user1/web/ask" -b 0.0.0.0:8080 wsgi:application --reload
cd /etc/nginx/sites-enabled
sudo fuser -k 80/tcp
sudo unlink default
sudo nginx -c /etc/nginx/sites-enabled/test.conf
sudo service nginx restart
