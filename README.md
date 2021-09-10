# CRUD REST API IN DOCKER

## Background

It was explosive experience to handle docker containers, reverse proxies, modeling database and so much between.

I used to doubt why dev project for security stuff but in end I really enjoyed.

## Start

Install `docker-compose` if you didn't:
``` bash
$ pip3 install docker-compose
```
Next clone and start container :
``` bash
$ cd REST-api

$ docker-compose -f docker-compose.prod.yml up -d --build
#Here -f for file ,up to initiate, -d to background

$ docker-compose -f docker-compose.prod.yml exec web python manage.py create_db
# exec : execute command in running container here to create tables
```
Once this finishes, Test it at http://localhost:1337 

Here Response will verify API up and ready

Once done bring it down :
``` bash
$ docker-compose -f docker-compose.prod.yml down -v
# down -v : bring container down with associated volumes
```

## Endpoints

* http://localhost:1337/playlist       : POST
* http://localhost:1337/playlist       : GET
* http://localhost:1337/playlist/<id\> : PUT
* http://localhost:1337/playlist/<id\> : DELETE

## Quick Notes 

Flask : To grow applications through extensions

Docker-compose : To define infrastructure such as services which include web, nginx and db and volumes

Gunicorn (Green-Unicorn) : Something that executes python but python is not best for all types of requests. It will listen on :5000 , later expose it to internal docker
`gunicorn --bind 0.0.0.0:5000 manage:app`

Nginx : Reverse proxy to forward request to gunicorn on :5000 

Nginx will receive the request and if it's dynamic request (which in our case is) it will pass it to gunicorn which in turn process it and return response to Nginx which then forwards the response back to flask client.

Entrypoint : Instruction to configure how container will run. Here we used it to verify status of db using netcat.

Dependencies:

Flask Cli tool : Provide access to flask applications command, Environment variable influence Python behaviour make sure to export FLASK_APP

Psycopg : Something that implement DB-API to connect to external Postgres database for python language.

Builder : Here Builder is used to build Python wheels which is built-package that don't need to recompile during every installations and to save final image size.

## References

* https://www.digitalocean.com/community/tutorials/how-to-build-and-deploy-a-flask-application-using-docker-on-ubuntu-18-04
* https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx
* https://docs.docker.com/develop/develop-images/multistage-build/

