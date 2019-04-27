FROM python

RUN cat /etc/issue

RUN pip install matplotlib
RUN pip install numpy
RUN apt update && apt install -y python-mpltoolkits.basemap

RUN echo 'alias e=exit' >> ~/.bashrc
RUN echo 'alias c=clear' >> ~/.bashrc

RUN mkdir /home/src
WORKDIR /home/src