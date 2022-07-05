#!/bin/sh

docker pull postgres
docker-compose up -d
sleep 5
cd react-web-client
npm run start:all