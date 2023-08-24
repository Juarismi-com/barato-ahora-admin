#!/bin/sh

clear(){
   echo "clean container volumen and images"
   docker-compose down
   docker stop $(docker ps -aq)
}

build(){
   echo "build and remove unnecesary images like none"
   docker-compose down
   docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
   docker-compose up --build
}

deploy(){
   echo "deploy"
}

# First param is the function name example "build" or "deploy"
$1