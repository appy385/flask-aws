#!/bin/sh
IMAGE_NAME='appy385/flask-aws'
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

build() {
  docker pull appy385/flask-aws
}
run(){
   docker run --rm --detach  --publish 80:80 $IMAGE_NAME
}
setup() {
  echo "Installing full application at once"
  stop
  remove
  build
  run
}
setup
