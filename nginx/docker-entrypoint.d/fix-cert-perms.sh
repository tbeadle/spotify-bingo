#!/bin/sh

# nginx runs as the 'nginx' user but these directories are 700 root:root when created by certbot.
chmod -v 755 /etc/letsencrypt/live
chmod -v 755 /etc/letsencrypt/archive
