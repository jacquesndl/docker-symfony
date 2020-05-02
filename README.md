# docker-symfony
Docker starter kit for project bases on symfony latest version

## prerequisites 
- [docker](https://docs.docker.com/install/)
- [fabric](http://www.fabfile.org/installing.html)

## create project
```bash
wget https://github.com/jacquesndl/docker-symfony/archive/master.zip
unzip master.zip && rm master.zip
mv docker-symfony-master/* . && rm -R docker-symfony-master
fab up
fab create
fab configure
fab start
```

## start project
```bash
fab configure
fab start
```

## up project
```bash
fab up
```

## stop project
```bash
fab stop
```

## dev
http://localhost/

## mailcatcher
http://localhost:1080/

## adminer
http://localhost:8080/

## composer
```
fab composer:[...]
fab composer:install
fab composer:update
```
