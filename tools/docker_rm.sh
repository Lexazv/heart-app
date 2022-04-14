#!/usr/bin/bash

docker stop $(docker ps -a | grep heart)

docker rm $(docker ps -a | grep heart)

docker rmi $(docker images | grep 'py_ml\|postgres')

docker network rm $(docker network ls | grep py_ml)
