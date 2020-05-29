#!/bin/sh
gunicorn application:application --log-level=debug --access-logfile logs/logfile.txt -b 0.0.0.0:80
