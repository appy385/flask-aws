#!/bin/sh
gunicorn --chdir app application:application -b 0.0.0.0:80
