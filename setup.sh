#!/bin/sh
IMAGE_NAME='gunicorn_flask'
remove(){
  docker image rm $IMAGE_NAME
}
build() {
  docker build -t $IMAGE_NAME /home/ubuntu
}
run(){
   docker run --rm --detach --publish 80:80 $IMAGE_NAME
}
install() {
  echo "Installing full application at once"
  build
  run
}
install
