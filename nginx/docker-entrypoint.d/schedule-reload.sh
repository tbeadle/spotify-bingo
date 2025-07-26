#!/bin/sh

while true; do
	sleep 6h
	echo "$(date) Reloading nginx."
	nginx -s reload
done &
