FROM python:3.8

RUN pip3 install pipenv
RUN git clone https://github.com/su115/ISTP.git
WORKDIR ISTP/Lab3/
EXPOSE 8000
RUN pipenv install 
ENTRYPOINT ["pipenv","run", "python3", "./manage.py", "runserver", "0.0.0.0:8000" ] 
