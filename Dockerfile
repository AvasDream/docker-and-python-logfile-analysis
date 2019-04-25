FROM python

RUN cat /etc/issue

RUN pip install matplotlib
RUN pip install numpy