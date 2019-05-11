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





## Basemap 


```python
m = Basemap(projection='robin',lon_0=0,resolution='c')
    m.fillcontinents(color='white',lake_color='white')
    m.drawcoastlines()
    # Map (long, lat) to (x, y) for plotting
    for i in lonlat:
        x, y = m(i[0], i[1])
        plt.plot(x, y, 'ro', markersize=3)
    plt.title("Source of login attempts")
    plt.show()
```