# legendary-enigma

[![Build Status](https://travis-ci.com/dustinlahr/legendary-enigma.svg?token=mtTH5HBaBtzTCpactyn1&branch=master)](https://travis-ci.com/dustinlahr/legendary-enigma)

## Build Docker Image
```
docker-compose build
```

## Run Project
```
docker-compose up
```

## Stop Project
Stop services
```
docker-compose stop
```

 Stop and remove containers, networks, images, and volumes
```
docker-compose down
```

## Run tests
Make sure you run `docker-compose up` before running tests
```
docker-compose run web python manage.py test
```

## Run migrations
```
docker-compose run web python3 manage.py migrate
```
