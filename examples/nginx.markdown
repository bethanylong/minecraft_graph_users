Nginx reverse proxy example
---------------------------


In `http` section (most likely in `nginx.conf`):

```
# Caching settings
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=STATIC:10m
                                  inactive=24h max_size=500m;

# Main site
upstream minecraft-main {
    server 1.2.3.4:80;
}

# Bottle json
upstream minecraft-json {
    server 5.6.7.8:59000;
}
```


In `server` section (most likely in `sites-enabled/sitename.conf`):

```
# Reverse proxy to main site
location / {
    proxy_pass          http://minecraft-main;
    proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
    proxy_redirect      off;
    proxy_buffering     off;
    proxy_set_header    Host            $host;
    proxy_set_header    X-Real-IP       $remote_addr;
    proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
}

# Reverse proxy to Bottle json (with caching)
location /json {
    proxy_pass          http://minecraft-json;
    proxy_next_upstream error timeout invalid_header http_500 http_502 http_503 http_504;
    proxy_redirect      off;
    proxy_buffering     on;
    proxy_set_header    Host            $host;
    proxy_set_header    X-Real-IP       $remote_addr;
    proxy_set_header    X-Forwarded-For $proxy_add_x_forwarded_for;
    proxy_cache         STATIC;
    proxy_cache_valid   200 5m;
}

# Serve static files off of the reverse proxy!
location /graph/ {
    alias /srv/sitename/minecraft_graph_users/frontend/;
}
```
