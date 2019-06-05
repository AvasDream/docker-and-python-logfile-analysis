## Dockpylog :snake: :whale: :mag_right:

Dockpylog can be used to automate the process of creating reports and graphs from your auth.log logfiles. It runs in a docker container and comes with an dockerfile to describe all dependencies. This project is mainly written in python, only the installation and the crontab scripts are in bash. 

## Example graph
![Example Graph](/examples/19-04-19-country.jpeg)

## Example report
[Example report](/examples/report-19-04-19.pdf)

## How it works

Dockpylog is triggered by a cronjob and does the following steps one time per day at 3am.

1. Grep all the IPs from failed ssh access attempts and store them in `/input/$(date +%d-%m-%y)_ips.txt`, also sort them by uniq. 

2. Start python programm in _non interactive_ docker container with all its dependencies and mount volume. 

3. Read IPs from `/input` folder.

4. Query the [IP geolocation API](http://ip-api.com/) for information about every IP and store responses in `data/`.

5. Create Barcharts and Report in `/output`.

6. Cleanup data

## Usage

Just check the `/output` folder for generated images and reports :)

## Installation

The installation is tested on a few debian derivates including Debain 9, Ubuntu 18, Kali Linux 2018.3.
Dockpylog requires Docker to be installed.

```bash
git clone https://github.com/AvasDream/dockpylog.git
cd dockpylog/scripts/ && sudo bash install.sh
```

What does the install script do? 

1. Check if it is running as root and check if docker is installed on host.

2. Create necessary directorys and change some file permissions.

3. Build the docker file.

4. Add cronjob to crontab. 


## Used Libraries

* [Matplotlib](https://matplotlib.org/)

* [Numpy](https://www.numpy.org/)

* [Reportlab](https://www.reportlab.com/opensource/)

* [Requests](https://2.python-requests.org/en/master/)

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Questions?

Write me on [twitter](https://twitter.com/samsepi0l_0d) :)

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Developement Notes:

* Add Worldmap with one dot per IP

* Add basemap in Dockerfile

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
* Add Timestamp parsing 

```
docker build . -t pyauthlog
# Developement
docker run --rm -it --volume="$(pwd):/home/src" pyauthlog /bin/bash
# Production
docker run -it --rm -e DATE="19-04-19"  -v "$(pwd):/home/pyauthlog" pyauthlog

# Delete all images

docker rm $(docker ps -a -q)

docker rmi $(docker images -q)

```
