FROM python:3.8
RUN mkdir my_tests
COPY ./ /my_tests/
RUN pip3 install pipenv 

WORKDIR /my_tests/
RUN pipenv install -r requirements.txt
ENTRYPOINT ["pipenv","run","pytest","test_app.py","--url","http://my_app:5000"]
