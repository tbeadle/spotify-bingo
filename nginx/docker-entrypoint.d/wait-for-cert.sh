#!/bin/sh

echo "Waiting for certificate to exist."
while true; do
	if [ -f /etc/letsencrypt/live/letsencrypt/fullchain.pem	]; then
		echo "Found!"
		break
	fi
	sleep 1
done
