#!/bin/sh

clear(){
   echo "clean container volumen and images"
   docker-compose down
   docker stop $(docker ps -aq)
}

build(){
   echo "build and remove unnecesary images like none"
   docker-compose down
   docker-compose up -d --build
   docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
}

start(){
   echo "Start container"
   docker-compose up -d
}


migrate(){
   docker-compose exec app python manage.py makemigrations
   docker-compose exec app python manage.py migrate
}

seed(){
   migrate
   echo "load seed"
}

full-start(){
   build
   migrate
   seed
}

test(){
   docker-compose exec app python manage.py test
}

deploy(){
   echo "deploy"
}

# First param is the function name example "build" or "deploy"
$1