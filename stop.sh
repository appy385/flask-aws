stop(){
  echo "Removing running container at once"
  docker container stop $(docker container ls -aq)
}
stop
