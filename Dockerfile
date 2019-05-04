FROM python
LABEL autorh="avasdream"
RUN pip install matplotlib
RUN pip install numpy
RUN pip install requests
#RUN apt update && apt install -y python-mpltoolkits.basemap
#RUN pip install https://github.com/matplotlib/basemap/archive/v1.0.7rel.tar.gz
RUN echo 'alias e=exit' >> ~/.bashrc
RUN echo 'alias c=clear' >> ~/.bashrc
RUN echo 'alias run="python /home/pyauthlog/source/main.py"' >> ~/.bashrc
RUN mkdir /home/pyauthlog
WORKDIR /home/pyauthlog