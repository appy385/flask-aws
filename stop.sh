#!/bin/sh
IMAGE_NAME='gunicorn_flask'
stop(){
  if [ $(docker ps | grep $IMAGE_NAME | wc -l) -gt 0 ]
  then
    docker container stop $(docker container ls -aq)
    echo "Removing running container at once"
  else
    echo "No running container"
  fi
}
remove(){
  if [ $(docker images | grep $IMAGE_NAME | wc -l) -gt 0 ]
  then
    docker image rm $IMAGE_NAME
  else
    echo "no image"
  fi
}

uninstall(){
  echo "Removing earlier version of application"
  stop
  remove

}
uninstall
