IMAGE_NAME='gunicorn_flask'
build() {
  docker build -t $IMAGE_NAME .
}
run(){
   docker run --rm --detach --publish 80:80 $IMAGE_NAME
}
stop(){
  echo "Removing running container at once"
  docker container stop $(docker container ls -aq)
}
install() {
  echo "Installing full application at once"
  build
  run
}
$*
