## Docker 

DO NOT FORGET RM!!!
```
docker build . -t pyauthlog

docker run --rm -it --volume="C:/Users/Tyrell Wellick/git/pyAuthLog:/home/src" pyauthlog /bin/bash


# Delete all images

docker rm $(docker ps -a -q)

docker rmi $(docker images -q)

```


## Python 

* Because i get all the filepaths with getcwd script has to be executed from /home/pyauthlog!