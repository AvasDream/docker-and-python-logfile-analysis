FROM python
LABEL autorh="avasdream"
RUN pip install matplotlib
RUN pip install numpy
RUN pip install requests
RUN pip install reportlab
RUN echo 'alias e=exit' >> ~/.bashrc
RUN echo 'alias c=clear' >> ~/.bashrc
RUN echo 'alias run="python /home/pyauthlog/source/main.py"' >> ~/.bashrc
RUN mkdir /home/pyauthlog
WORKDIR /home/pyauthlog