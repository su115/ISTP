FROM python:3.8
RUN mkdir my_app
COPY ./ /my_app/
RUN pip3 install pipenv 

WORKDIR /my_app/
RUN pipenv install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["pipenv","run","python3","app.py"]
