#!/bin/bash
variable=$(date '+%Y%m%d_%H%M')
mkdir -p ~/docker_logs/$variable
cd ~/docker_logs/$variable
<<<<<<< HEAD
docker logs tsng-cuda > tsng-cuda
=======
docker logs tsng-tf > tsng-tf
>>>>>>> 5592f8e... Initial commit
