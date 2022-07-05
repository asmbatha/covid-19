#!/bin/sh

docker pull postgres
docker-compose up -d

cd service
python3 -m pip install -r requirements.txt
cd ../react-web-client
npm i
sleep 20
npm run start:all