FROM python

RUN cat /etc/issue

RUN pip install matplotlib
RUN pip install numpy
RUN pip install requests
#RUN apt update && apt install -y python-mpltoolkits.basemap
RUN pip install https://github.com/matplotlib/basemap/archive/v1.0.7rel.tar.gz
RUN echo 'alias e=exit' >> ~/.bashrc
RUN echo 'alias c=clear' >> ~/.bashrc

RUN mkdir /home/src
WORKDIR /home/src