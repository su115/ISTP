FROM python:3.8

RUN pip3 install pipenv && pipenv install && mkdir /mylog
RUN git clone https://github.com/su115/ISTP.git
WORKDIR ISTP/Lab3/
RUN pipenv install requests
# in file monitoring.py localhost:8000 changes to serverHostname:8000
ENTRYPOINT ["pipenv","run","python3", "./monitoring.py"]
