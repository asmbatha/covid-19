#!/bin/sh

docker pull postgres
docker run --rm --name pg-docker -e POSTGRES_PASSWORD=docker -d -p 5432:5432 -v $HOME/docker/volumes/postgres:/var/lib/postgresql/data postgres

cd service
python3 -m pip install -r requirements.txt
cd ../react-web-client
npm i
npm run start:all