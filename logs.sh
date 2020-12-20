#!/bin/bash
variable=$(date '+%Y%m%d_%H%M')
mkdir -p ~/docker_logs/$variable
cd ~/docker_logs/$variable
docker logs tsng-cuda > tsng-cuda