#!/bin/sh
IMAGE_NAME='gunicorn_flask'
stop(){
  echo "Removing running container at once"
  docker container stop $(docker container ls -aq)
}
rmimage(){
  echo "Removing image"
  docker image rm $IMAGE_NAME


}
uninstall(){
  echo "Removing earlier version of application"
  stop
  rmimage

}
uninstall
