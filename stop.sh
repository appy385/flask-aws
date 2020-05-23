#!/bin/sh
IMAGE_NAME='gunicorn_flask'
stop(){
  echo "Removing running container at once"
  if [ $(docker container ls -aq) > 0 ]
  then
    docker container stop $(docker container ls -aq)
  fi
}

uninstall(){
  echo "Removing earlier version of application"
  stop

}
uninstall
